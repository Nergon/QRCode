from PIL import Image

from typing import List
from .enums import QRMode, QRErrorCorrectionLevel
from .utils import calculate_best_qrmode, calculate_smallest_version, get_character_count_bits, calc_mask, calculate_penalty_score
from .constants import ALPHANUMERIC_TABLE, MAX_DATA_CODEWORDS, BLOCKS_TABLE, REMAINDER_BITS, ALIGNMENT_PATTERN_POSITIONS
from .reed_solomon import rs_encode_msg

from bitstring import BitArray

from reedsolo import RSCodec

import math

import itertools

class QRCode:
    
    data : str = None
    mode : 'QRMode' = None
    version: int = None
    correction: 'QRErrorCorrectionLevel' = None

    matrix: List[List[bool]] = None

    def __init__(self, data : str, correction: QRErrorCorrectionLevel = QRErrorCorrectionLevel.L) -> None:
        self.data = data
        self.correction = correction
        self.mode = calculate_best_qrmode(data)
        self.version = calculate_smallest_version(data, self.mode, correction)

    def __encode_data(self) -> List[BitArray]:
        """Encode the data into a list of 8-bit bytes"""
        data = BitArray()

        # Add mode indicator
        if self.mode == QRMode.NUMERIC:
            data.append(BitArray(bin="0001"))
        elif self.mode == QRMode.ALPHANUMERIC:
            data.append(BitArray(bin="0010"))
        elif self.mode == QRMode.BYTE:
            data.append(BitArray(bin="0100"))
            self.data = self.data.encode("utf-8")
        else:
            raise ValueError("Invalid QRMode")
        
        # Add character count indicator
        neededBits : int = get_character_count_bits(self.mode, self.version)

        characterCount = BitArray(uint=int(len(self.data)), length=neededBits)

        data.append(characterCount)

        # Encode data
        if self.mode == QRMode.NUMERIC:
            data.append(self.__encode_data_numeric())
        elif self.mode == QRMode.ALPHANUMERIC:
            data.append(self.__encode_data_alphanumeric())
        elif self.mode == QRMode.BYTE:
            data.append(self.__encode_data_byte())
        else:
            raise ValueError("Invalid QRMode")
        
        # Pad bits
        # The QR Code specification defines that the data must use the full aviable length of bits
        # First determine the maximum length of the data
        max_length = MAX_DATA_CODEWORDS[self.version][self.correction.value] * 8

        # Add up to 4 zeros at the end if the data is too short
        if len(data) <= max_length - 4:
            data.append(BitArray(bin="0000"))
        elif len(data) <= max_length - 3:
            data.append(BitArray(bin="000"))
        elif len(data) <= max_length - 2:
            data.append(BitArray(bin="00"))
        elif len(data) <= max_length - 1:
            data.append(BitArray(bin="0"))
        
        # If the data is still to short add zeros until multiple of 8
        if len(data)  < max_length:
            while len(data) % 8 != 0:
                data.append(BitArray(bin="0"))

        # If the data is still to short add 11101100 00010001 until filled
        while len(data) < max_length:
            data.append(BitArray(bin="11101100"))
            if len(data) < max_length:
                data.append(BitArray(bin="00010001"))

        # Split data into chunks of 8 bits (necessary for the Reed-Solomon error correction)
        data_array = []

        for i in range(0, len(data), 8):
            data_array.append(data[i:i+8])
        
        return data_array
        

    def __encode_data_numeric(self) -> BitArray:
        """Splits the data up into numbers of 3 and then encodes each one of them into 10 bits."""
        encoded_data = BitArray()
        for i in range(0, len(self.data), 3):
            if i == len(self.data) - 1:
                # If there is only one number left, convert it to 4 bits
                number = int(self.data[i])
                encoded_data.append(BitArray(uint=number, length=4))
            elif i == len(self.data) - 2:
                # If there are two numbers left, convert them to 7 bits
                number = int(self.data[i:i+2])
                encoded_data.append(BitArray(uint=number, length=7))
            else:
                number = int(self.data[i:i+3])
                encoded_data.append(BitArray(uint=number, length=10))
        return encoded_data
    
    def __encode_data_alphanumeric(self) -> BitArray:
        """Take two pairs of alphanumeric characters and encode them into 11 bits by multiplying 
        the first character with 45 and then adding the second one. If there is an odd number convert the last character to 6 bits."""
        encoded_data = BitArray()
        for i in range(0, len(self.data), 2):
            if i == len(self.data) - 1:
                number = ALPHANUMERIC_TABLE[self.data[i]]
                encoded_data.append(BitArray(uint=number, length=6))
            else:
                number = ALPHANUMERIC_TABLE[self.data[i]] * 45 + ALPHANUMERIC_TABLE[self.data[i+1]]
                encoded_data.append(BitArray(uint=number, length=11))
        return encoded_data
    
    def __encode_data_byte(self) -> BitArray:
        """Encode the data into UTF-8 and then into Binary using BitArray."""
        return BitArray(bytes=self.data)
    
    def __add_error_correction(self, data : List[BitArray]) -> List[BitArray]:
        """Add error correction to the data using Reed-Solomon."""
        group1 = []
        group2 = []

        group1_codewords = []
        group2_codewords = []

        # Split the data into blocks according to BLOCKS_TABLE
        codewords = BLOCKS_TABLE[self.version][self.correction.value][1]["EC_CODEWORDS"]
        group1_blocks_count = BLOCKS_TABLE[self.version][self.correction.value][1]["BLOCKS"]
        group1_blocks_datawords = BLOCKS_TABLE[self.version][self.correction.value][1]["DATA_CODEWORDS"]

        if BLOCKS_TABLE[self.version][self.correction.value][2] is not None:
            group2_blocks_count = BLOCKS_TABLE[self.version][self.correction.value][2]["BLOCKS"]
            group2_blocks_datawords = BLOCKS_TABLE[self.version][self.correction.value][2]["DATA_CODEWORDS"]
        else:
            group2_blocks_datawords = 0
            group2_blocks_count = 0

        for i in range(group1_blocks_count):
            group1.append([int(data[i * group1_blocks_datawords + j].uint) for j in range(group1_blocks_datawords)])

        already_placed = (group1_blocks_count * group1_blocks_datawords)

        for i in range(group2_blocks_count):
            group2.append([int(data[already_placed + i * group2_blocks_datawords + j].uint) for j in range(group2_blocks_datawords)])

        # Add error correction to each block
        for i in range(len(group1)):
            group1_codewords.append(rs_encode_msg(group1[i], codewords))

        if BLOCKS_TABLE[self.version][self.correction.value][2] is not None:
            for i in range(len(group2)):
                group2_codewords.append(rs_encode_msg(group2[i], codewords))
                print(group2_codewords)
        
        # Struture the data into a list of BitArrays with the correct order
        interleaved_data = []

        # If only one block no interleaving is necessary

        if group1_blocks_count == 1 and group2_blocks_count == 0:
            for dataword in group1[0]:
                interleaved_data.append(dataword)

            for codeword in group1_codewords[0]:
                interleaved_data.append(codeword)
            
        else:
            # Otherwise take the first codeword from the first block, then the first codeword from the second block and so on
            blocks = group1 + group2
            codewords_data = group1_codewords + group2_codewords

            # Interleave the blocks
            # First get max length of blocks
            max_length = max(len(block) for block in blocks)
            for i in range(max_length):
                for block in blocks:
                    if i < len(block):
                        print(hex(block[i]))
                        interleaved_data.append(block[i])

            # Interleave the codewords
            max_length = max(len(codewords) for codewords in codewords_data)
            for i in range(max_length):
                for codewords in codewords_data:
                    if i < len(codewords):
                        interleaved_data.append(codewords[i])

        # Convert into BitArray
        encoded_data = BitArray()
        for i in range(len(interleaved_data)):
            encoded_data.append(BitArray(uint=interleaved_data[i], length=8))

        # Add remainder bits
        if REMAINDER_BITS[self.version] != 0:
            encoded_data.append(BitArray(length=REMAINDER_BITS[self.version], uint=0))

        print(encoded_data.bin)
        return encoded_data
            
    def __calculate_size(self) -> int:
        """Returns the size of the QR Code in modules"""
        # Formula: ((version - 1) * 4) + 21
        return (((self.version - 1) * 4) + 21)
    
    def __setup_matrix(self) -> None:
        """Creates the matrix and places finder patterns and alignment patterns and timing patterns."""
        # Create matrix (-2) for empty (-3) for do not change black and (-4) for do not change black white
        self.matrix = [[-2 for i in range(self.__calculate_size())] for j in range(self.__calculate_size())]
        # Place finder patterns
        self.__place_finder_pattern(0, 0)
        self.__place_finder_pattern(self.__calculate_size() - 7, 0)
        self.__place_finder_pattern(0, self.__calculate_size() - 7)
        # Add seperators
        for i in range(8):
            self.matrix[7][i] = -4
            self.matrix[i][7] = -4
            self.matrix[self.__calculate_size() - 8][i] = -4
            self.matrix[self.__calculate_size() - 8 + i][7] = -4
            self.matrix[7][self.__calculate_size() - 8 + i] = -4
            self.matrix[i][self.__calculate_size() - 8] = -4

        # Place alignment patterns
        cathesian = itertools.product(ALIGNMENT_PATTERN_POSITIONS[self.version], ALIGNMENT_PATTERN_POSITIONS[self.version])
        for p in cathesian:
            # Check if alignment pattern is not placed on finder pattern
            if not (p[0] == 6 and p[1] == 6) and not (p[0] == 6 and p[1] == self.__calculate_size() - 7) and not (p[0] == self.__calculate_size() - 7 and p[1] == 6):
                self.__place_alignment_pattern(p[0], p[1])

        # Place timing patterns
        for i in range(8, self.__calculate_size() - 8):
            # If colliding with finder pattern skip
            if len(ALIGNMENT_PATTERN_POSITIONS[self.version]) != 0:
                for p in ALIGNMENT_PATTERN_POSITIONS[self.version]:
                    if i > p-2 and i < p +2:
                        continue
                    if i % 2 == 0:
                        self.matrix[6][i] = -3
                        self.matrix[i][6] = -3
                    else:
                        self.matrix[6][i] = -4
                        self.matrix[i][6] = -4
            else:
                if i % 2 == 0:
                    self.matrix[6][i] = -3
                    self.matrix[i][6] = -3
                else:
                    self.matrix[6][i] = -4
                    self.matrix[i][6] = -4

        # Reserve space for format information (-1)
        
         # If Version < 7 reserve a strip around the finder patterns    
        for i in range(9):
            if i < 8:
                self.matrix[self.__calculate_size() - 8 + i][8] = -1
                self.matrix[8][self.__calculate_size() - 8 + i] = -1
            # Skip alignment pattern
            if i == 6:
                continue

            self.matrix[8][i] = -1
            self.matrix[i][8] = -1
            # One Black Pixel at
            self.matrix[8][self.__calculate_size() -8] = -3
                    
        if self.version >= 7:
            # Reserve 6x3 above bottom left and 3x6 on top right
            for i in range(6):
                for j in range(3):
                    self.matrix[self.__calculate_size() - 11 + j][i] = -1
                    self.matrix[i][self.__calculate_size() - 11 + j] = -1 

    def __place_alignment_pattern(self, x : int, y: int) -> None:
        x -= 2
        y -= 2
        for i in range(5):
            for j in range(5):
                if i == 0 or i == 4 or j == 0 or j == 4:
                    self.matrix[x+i][y+j] = -3
                elif i == 2 and j == 2:
                    self.matrix[x+i][y+j] = -3
                else:
                    self.matrix[x+i][y+j] = -4

    def __place_finder_pattern(self, x : int, y : int) -> None:
        """Places a finder pattern at (x,y) in matrix and adds"""
        for i in range(7):
            for j in range(7):
                if i % 6 == 0 or j % 6 == 0:
                    self.matrix[x+i][y+j] = -3
                elif i > 1 and i < 5 and j > 1 and j < 5:
                    self.matrix[x+i][y+j] = -3
                else:
                    self.matrix[x+i][y+j] = -4

    def __place_data(self, encoded_data) -> None:
        """Places the encoded data in the matrix"""
        # Data is placed in a zigzag pattern starting from the bottom
        # -1 for upwars, 1 for downwards
        direction = -1
        col = self.__calculate_size() -1
        row = self.__calculate_size() -1
        data_bit_index = 0
        is_left = False

        # If vertical alignment pattern is present skip column
        placecount = 0

        while col >= 0:
            if col == 6:
                col -= 1

            if self.matrix[col][row] == -2:
                self.matrix[col][row] = encoded_data[data_bit_index]
                data_bit_index += 1
                placecount +=1 
                

            if is_left:
                col += 1
                row += direction
            else:
                col -= 1

            is_left = not is_left

            if row < 0 or row == self.__calculate_size():
                direction = -direction
                row += direction
                if is_left:
                    col -= 1
                    is_left = False
                else:
                    col -= 2

    def __choose_mask(self):
        # TODO: Fix masking penatly calculation
        min_penalty = -1
        best_mask = None
        best_mask_index = -1
        for i in range(8):
            mask = calc_mask(i, self.matrix)
            penalty = calculate_penalty_score(mask)
            if min_penalty == -1 or penalty < min_penalty:
                min_penalty = penalty
                best_mask = mask
                best_mask_index = i

        #self.matrix = calc_mask(2, self.matrix)
        
        self.matrix = best_mask
        self.mask = best_mask_index

        print("Best mask: " + str(best_mask_index))

    def __add_format_information(self):
        encoded_info = BitArray(uint=QRErrorCorrectionLevel.to_bit_integer(self.correction), length=2)
        encoded_info.append(BitArray(uint=self.mask, length=3))

        encoded_info.append(self.__generate_error_correction_format(encoded_info))

        # QR Code specification says to XOR with this string 101010000010010
        xor_string = BitArray(bin="101010000010010")
        encoded_info ^= xor_string

        # Place top left under finder pattern
        for i in range(8):
            if i < 6:
                self.matrix[i][8] = int(encoded_info[i])
            else:
                self.matrix[i+1][8] = int(encoded_info[i])

        # Place top left at the right side of the finder pattern
        for i in range(8):
            if i < 2:
                self.matrix[8][8-i] = int(encoded_info[i+7])
            else:
                self.matrix[8][8-i-1] = int(encoded_info[i+7])

        # Place top right at the bottom of the finder pattern
        for i in range(8):
            self.matrix[self.__calculate_size() - i - 1][8] = int(encoded_info[i+7])

        # Place bottom left at the right side of the finder pattern
        for i in range(7):
            self.matrix[8][self.__calculate_size() - i - 1] = int(encoded_info[i])

        
    def __generate_error_correction_format(self, info):
        # Generatorpolynomial is 10100110111
        polonomial = BitArray(bin="10100110111")
        # Make 15 Bits long
        info = BitArray(bin=info.bin)
        info.append(BitArray(uint=0, length=10))

        self.remove_leading_zeros(info)

        # Divide by generator polynomial
        while len(info) >= len(polonomial):
            # Pad generator string with zeros to make it same lenght as the current format string
            appended_polonomial = BitArray(bin=polonomial.bin)
            if len(info) -  len(polonomial) > 0:
                appended_polonomial.append(BitArray(uint=0, length=len(info) - len(polonomial)))
            
            # XOR
            info ^= appended_polonomial
            # Remove leading zeros
            info = self.remove_leading_zeros(info)

        # Pad with zeros to make it 10 bits long
        if abs(10-len(info)) > 0:
            info.prepend(BitArray(uint=0, length=abs(10-len(info))))
        
        return info

    def remove_leading_zeros(self, bit_array):
        # Convert BitArray to string
        bit_string = bit_array.bin

        # Remove leading zeros
        trimmed_bit_string = bit_string.lstrip('0')

        # Convert back to BitArray
        trimmed_bit_array = BitArray(bin=trimmed_bit_string)

        return trimmed_bit_array
    
    def __add_version_information(self):
        encoded_info = BitArray(uint=self.version, length=6)
        encoded_info.append(self.__generate_error_correction_version(encoded_info))
        
        # Place bottom left at the top of the finder pattern with the right bits being the first
        for i in range(6):
            for j in range(3):
                self.matrix[i][self.__calculate_size() - 7 - (3 - j) - 1] = encoded_info[len(encoded_info) - 1 - (i*3 + j)]

        # Place at the top right of the finder pattern with the right bits being the first
        for i in range(6):
            for j in range(3):
                self.matrix[self.__calculate_size() - 7 - (3 - j) - 1][i] = encoded_info[len(encoded_info) - 1 - (i*3 + j)]


    def __generate_error_correction_version(self, info):
        # Generator poloynomial is 1111100100101
        polonomial = BitArray(bin="1111100100101")
        # Pad to 18 bits
        info = BitArray(bin=info.bin)
        info.append(BitArray(uint=0, length=12))

        self.remove_leading_zeros(info)

        while len(info) >= len(polonomial):
            # Pad generator string with zeros to make it same lenght as the current format string
            appended_polonomial = BitArray(bin=polonomial.bin)
            if len(info) -  len(polonomial) > 0:
                appended_polonomial.append(BitArray(uint=0, length=len(info) - len(polonomial)))
            
            # XOR
            info ^= appended_polonomial
            # Remove leading zeros
            info = self.remove_leading_zeros(info)

        # Pad with zeros to make it 10 bits long
        if abs(12-len(info)) > 0:
            info.prepend(BitArray(uint=0, length=abs(12-len(info))))
        
        return info



    def make(self):
        """Make the QR Code. Returns a 2D array of booleans."""
        # First encode data
        encoded_data : List[BitArray] = self.__encode_data()
        # Second add error correction
        encoded_data = self.__add_error_correction(encoded_data)
        print(encoded_data)
        # Setup Matrix
        self.__setup_matrix()
        # Place Data in Matrix
        self.__place_data(encoded_data)
        # Masking
        self.__choose_mask()
        # Add format information
        self.__add_format_information()
        # Add version information if needed
        if self.version >= 7:
            self.__add_version_information()


class QRCodeRenderer:
    
    @staticmethod
    def save(qrcode : 'QRCode', path : str, size = 1) -> None:
        """Save the QR Code to a .png file. Size is the size of each module in pixels."""
        if(qrcode.matrix == None):
            raise ValueError("QRCode has not been made yet.")
        
        image = Image.new("RGB", (len(qrcode.matrix)*size, len(qrcode.matrix)*size))
        pixels = image.load()

        for i in range(len(qrcode.matrix)):
            for j in range(len(qrcode.matrix)):
                if qrcode.matrix[i][j] == 1 or qrcode.matrix[i][j] == -3: 
                    for x in range(size):
                        for y in range(size):
                            pixels[i*size+x, j*size+y] = (0, 0, 0)
                elif qrcode.matrix[i][j] == -1:
                    for x in range(size):
                        for y in range(size):
                            pixels[i*size+x, j*size+y] = (0, 0, 255)
                elif qrcode.matrix[i][j] == -2:
                    for x in range(size):
                        for y in range(size):
                            pixels[i*size+x, j*size+y] = (0, 255, 255)
                else:
                    for x in range(size):
                        for y in range(size):
                            pixels[i*size+x, j*size+y] = (255, 255, 255)

        image.save(path)
        image.show()

        
