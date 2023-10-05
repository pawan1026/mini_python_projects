import pyqrcode
from pyqrcode import create
import tkinter as tk
from tkinter import *
from PIL import Image

my_w=tk.Tk()
my_w.geometry("400x400")
my_w.title("QRCODE USING TKINTER")

e1=tk.Entry(my_w,font=21,bg='white',width=15)
e1.grid(row=0,column=0,padx=10,pady=10)
b1=tk.Button(my_w,font=21,text="Generate QR Code",command=lambda:my_generate())
b1.grid(row=0,column=1,padx=5,pady=10)

l1=tk.Label(my_w,text="QR Code")
l1.grid(row=1,column=0,columnspan=2)

def my_generate():
    global my_img
    my_qr=pyqrcode.create(e1.get())
    #my_qr.show() # This can be used to display the QR code in a separate window
    my_qr=my_qr.xbm(scale=10)
    my_img=tk.BitmapImage(data=my_qr)
    l1.config(image=my_img) #Show the QR code in Tkinter window itself

my_w.mainloop()