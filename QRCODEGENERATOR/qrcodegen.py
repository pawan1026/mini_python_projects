"""
QRCODE
"""
import qrcode
from PIL import Image

#USED TO GENERATE CODE

def qrcodegenerator(name,pan):
    qr=qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=10,border=10,)
    qr.add_data(pan)
    qr.make(fit=True)
    img=qr.make_image(fill_color="black",back_color="white")
    img.save(name+"'s PAN Number"+".png")
NAME=str(input("Provide your Name "))
PAN=str(input("Provide your PAN number "))

qrcodegenerator(NAME,PAN)
