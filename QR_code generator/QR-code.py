import qrcode
from PILTools import Image

qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_H,
                   box_size=10, border=5, )
qr.add_data("Paste link")
qr.make(fit=True)
img = qr.make_image(fill_color="green", back_color="black")
img.save("YT-Channel.gif")
img.save("YT-Channel.png")

