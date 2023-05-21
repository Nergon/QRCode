from qrcode.qrcode import QRCode, QRCodeRenderer
from qrcode.enums import QRErrorCorrectionLevel

if __name__ == "__main__":
    print("QR Code Generator")
    data = input("Enter a string to encode: ")
    ec_string = input("Enter an error correction level (L, M, Q, H): ")
    ec = None
    if ec_string == "L":
        ec = QRErrorCorrectionLevel.L
    elif ec_string == "M":
        ec = QRErrorCorrectionLevel.M
    elif ec_string == "Q":
        ec = QRErrorCorrectionLevel.Q
    elif ec_string == "H":
        ec = QRErrorCorrectionLevel.H
    else:
        print("Invalid error correction level")
        exit(1)
    qr = QRCode(data, ec)
    qr.make()
    QRCodeRenderer.save(qr, "test.png", 10)