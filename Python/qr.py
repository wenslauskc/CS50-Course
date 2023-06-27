import os
import qrcode

img = qrcode.make("https://youtube.com/watch?v=GvjdOdXr1fc") 

img.save("qr.png", "PNG")

os.system("open qr.png")