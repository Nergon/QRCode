from qrcode.qrcode import QRCode, QRCodeRenderer
from qrcode.enums import QRErrorCorrectionLevel

if __name__ == "__main__":
    qr = QRCode("HELLO WORLD", QRErrorCorrectionLevel.H)
    qr.make()
    QRCodeRenderer.save(qr, "test.png")