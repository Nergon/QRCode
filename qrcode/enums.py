from enum import Enum

class QRMode (Enum):
    """Enum of QR Code modes."""
    NUMERIC = 0
    ALPHANUMERIC = 1
    BYTE = 2
    KANJI = 3


    @staticmethod  
    def to_string(mode : 'QRMode') -> str:
        """Converts a QRMode into String"""
        if mode == QRMode.NUMERIC:
            return "NUMERIC"
        elif mode == QRMode.ALPHANUMERIC:
            return "ALPHANUMERIC"
        elif mode == QRMode.BYTE:
            return "BYTE"
        elif mode == QRMode.KANJI:
            return "KANJI"
        else:
            raise ValueError("Invalid QRMode")

class QRErrorCorrectionLevel (Enum):
    """Enum of QR Code error correction levels."""
    L = 0
    M = 1
    Q = 2
    H = 3

    @staticmethod
    def to_bit_integer(correction : 'QRErrorCorrectionLevel'):
        """Converts the mode into the integer equivalent of the bit code representation used in qr codes"""
        if correction == QRErrorCorrectionLevel.L:
            return 1 # 01
        elif correction == QRErrorCorrectionLevel.M:
            return 0 # 00
        elif correction == QRErrorCorrectionLevel.Q:
            return 3 # 11
        elif correction == QRErrorCorrectionLevel.H:
            return 2 # 10
        else:
            raise ValueError("Invalid QRErrorCorrectionLevel")