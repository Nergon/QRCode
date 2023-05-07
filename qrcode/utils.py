from enums import QRMode, QRErrorCorrectionLevel

alphanumeric_characters = set("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ $%*+-./:")

def calculate_best_qrmode(data : str):
    """Calculate the best QRMode for the given data. Kanji is not implemented."""
    if data.isdigit():
        return QRMode.NUMERIC
    elif set(data).issubset(alphanumeric_characters):
        return QRMode.ALPHANUMERIC
    else:
        return QRMode.BYTE
    

