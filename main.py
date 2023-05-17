from qrcode.qrcode import QRCode, QRCodeRenderer
from qrcode.enums import QRErrorCorrectionLevel

if __name__ == "__main__":
    qr = QRCode("Hello World 123!", QRErrorCorrectionLevel.H)
    qr.make()
    QRCodeRenderer.save(qr, "test.png")