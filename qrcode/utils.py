from .enums import QRMode, QRErrorCorrectionLevel
from .constants import QR_CODE_VERSIONS

alphanumeric_characters = set("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ $%*+-./:")

def calculate_best_qrmode(data : str):
    """Calculate the best QRMode for the given data. Kanji is not implemented."""
    if data.isdigit():
        return QRMode.NUMERIC
    elif set(data).issubset(alphanumeric_characters):
        return QRMode.ALPHANUMERIC
    else:
        return QRMode.BYTE
    

def calculate_smallest_version(data : str, mode : QRMode,correction : QRErrorCorrectionLevel):
    char_count = len(data)
    for i in range(1,40):
        if char_count <= QR_CODE_VERSIONS[i][QRMode.to_string(mode)][correction.value]:
            return i
    raise ValueError("Data too long for QR Code")


def get_character_count_bits(mode: QRMode, version: int):
    if version <= 9:
        if mode == QRMode.NUMERIC:
            return 10
        elif mode == QRMode.ALPHANUMERIC:
            return 9
        elif mode == QRMode.BYTE:
            return 8
        else:
            raise ValueError("Invalid QRMode")
    elif version <= 26:
        if mode == QRMode.NUMERIC:
            return 12
        elif mode == QRMode.ALPHANUMERIC:
            return 11
        elif mode == QRMode.BYTE:
            return 16
        else:
            raise ValueError("Invalid QRMode")
    else:
        if mode == QRMode.NUMERIC:
            return 14
        elif mode == QRMode.ALPHANUMERIC:
            return 13
        elif mode == QRMode.BYTE:
            return 16
        else:
            raise ValueError("Invalid QRMode")