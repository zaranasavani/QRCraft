import qrcode as qr
img = qr.make("https://www.youtube.com/@milansavani3742")   #qr code thi jena par javanu hoy teni link aapvani
img.save("milan_youtube.png")        #generate thayelo qr code ne je save karavo hoy te file type
