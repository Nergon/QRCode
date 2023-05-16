import PIL

from typing import List
from .enums import QRMode, QRErrorCorrectionLevel
from .utils import calculate_best_qrmode, calculate_smallest_version, get_character_count_bits
from .constants import ALPHANUMERIC_TABLE, MAX_DATA_CODEWORDS, BLOCKS_TABLE, REMAINDER_BITS
from .reed_solomon import rs_encode_msg

from bitstring import BitArray

from reedsolo import RSCodec

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
        else:
            raise ValueError("Invalid QRMode")
        
        # Add character count indicator
        neededBits : int = get_character_count_bits(self.mode, self.version)

        characterCount = BitArray(uint=len(self.data), length=neededBits)

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
        print(max_length)
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
        utf8 = self.data.encode("utf-8")
        return BitArray(bytes=utf8)
    
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
        
        
        for i in range(group2_blocks_count):
            group2.append([int(data[i * group2_blocks_datawords + j].uint) for j in range(group2_blocks_datawords)])

        # Add error correction to each block
        for i in range(len(group1)):
            group1_codewords.append(rs_encode_msg(group1[i], codewords))

        if BLOCKS_TABLE[self.version][self.correction.value][2] is not None:
            for i in range(len(group2)):
                group2_codewords.append(rs_encode_msg(group2[i], codewords))
        
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

            print(codewords_data)

            # Interleave the blocks
            # First get max length of blocks
            max_length = max(len(block) for block in blocks)
            for i in range(max_length):
                for block in blocks:
                    if i < len(block):
                        interleaved_data.append(block[i])

            # Interleave the codewords
            max_length = max(len(codewords) for codewords in codewords_data)
            for i in range(max_length):
                for codewords in codewords_data:
                    if i < len(codewords):
                        interleaved_data.append(codewords[i])


        print(interleaved_data)
        # Convert into BitArray
        encoded_data = BitArray()
        for i in range(len(interleaved_data)):
            encoded_data.append(BitArray(uint=interleaved_data[i], length=8))

        # Add remainder bits
        if REMAINDER_BITS[self.version] != 0:
            encoded_data.append(BitArray(length=REMAINDER_BITS[self.version], uint=0))

        return encoded_data
            
        

    def make(self):
        """Make the QR Code. Returns a 2D array of booleans."""
        # First encode data
        encoded_data : List[BitArray] = self.__encode_data()
        # Second add error correction
        encoded_data = self.__add_error_correction(encoded_data)

        print(encoded_data)
        # Third generate matrix



class QRCodeRenderer:
    
    @staticmethod
    def save(qrcode : 'QRCode', path : str) -> None:
        """Save the QR Code to a .png file."""
        if(qrcode.List[List[bool]] == None):
            raise ValueError("QRCode has not been made yet.")
        
        image = PIL.Image.new("RGB", (len(qrcode.List[List[bool]]), len(qrcode.List[List[bool]])))
        pixels = image.load()

        for i in range(len(qrcode.List[List[bool]])):
            for j in range(len(qrcode.List[List[bool]])):
                if qrcode.List[List[bool]][i][j]:
                    pixels[i, j] = (0, 0, 0)
                else:
                    pixels[i, j] = (255, 255, 255)

        image.save(path)
        image.show()

        
