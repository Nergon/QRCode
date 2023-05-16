from qrcode.qrcode import QRCode
from qrcode.enums import QRErrorCorrectionLevel

if __name__ == "__main__":
    QRCode("Hello World 123!", QRErrorCorrectionLevel.H).make()