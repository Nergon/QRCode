from qrcode.qrcode import QRCode
from qrcode.enums import QRErrorCorrectionLevel

if __name__ == "__main__":
    QRCode("HELLO WORLD", QRErrorCorrectionLevel.Q).make()