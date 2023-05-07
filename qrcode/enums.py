from enum import Enum

class QRMode (Enum):
    """Enum of QR Code modes."""
    NUMERIC = 0
    ALPHANUMERIC = 1
    BYTE = 2
    KANJI = 3

class QRErrorCorrectionLevel (Enum):
    """Enum of QR Code error correction levels."""
    L = 0
    M = 1
    Q = 2
    H = 3