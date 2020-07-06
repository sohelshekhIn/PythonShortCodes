import pyqrcode
import png
from pyqrcode import QRCode

message = input("Enter qr message: ")
url = pyqrcode.create(message)
url.svg("qrcode.svg", scale=8)
