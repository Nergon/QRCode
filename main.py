from qrcode.qrcode import QRCode, QRCodeRenderer
from qrcode.enums import QRErrorCorrectionLevel

if __name__ == "__main__":
    qr = QRCode("HELLO WORLD! HELLO WORLD! HELLO WORLD! HELLO WORLD! HELLO WORLD! HELLO WORLD! HELLO WORLD! HELLO WORLD!", QRErrorCorrectionLevel.L)
    qr.make()
    QRCodeRenderer.save(qr, "test.png", 10)