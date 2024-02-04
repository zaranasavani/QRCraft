import qrcode as qr
img = qr.make("https://www.youtube.com/@milansavani3742")   #give the link where you want to go from QR-code
img.save("milan_youtube.png")        #file type for saving generated QR-code
