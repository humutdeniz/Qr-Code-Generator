import qrcode

def create_qr_code(link):
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(link)
    qr.make(fit=True)
    qr_img = qr.make_image(fill="black", back_color="white")
    return qr_img

link = input("Enter the link: ")

qr_code = create_qr_code(link)

qr_code.save("qrcode.png")

print("QR code saved in the default location")