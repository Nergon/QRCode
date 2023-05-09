import PIL

from typing import List
from .enums import QRMode, QRErrorCorrectionLevel
from .utils import calculate_best_qrmode, calculate_smallest_version, get_character_count_bits
from .constants import ALPHANUMERIC_TABLE, MAX_DATA_CODEWORDS

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
        """Encode the data into UTF-8 and then into Binary using BitArray.s"""
        utf8 = self.data.encode("utf-8")
        return BitArray(bytes=utf8)
    
    def __add_error_correction(self, data : List[BitArray]) -> List[BitArray]:
        pass

 

    def make(self):
        """Make the QR Code. Returns a 2D array of booleans."""
        # First encode data
        encoded_data : List[BitArray] = self.__encode_data()
        # Second add error correction
        encoded_data = self.__add_error_correction(encoded_data)
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

        
