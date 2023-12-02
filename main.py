import qrcode

qr = qrcode.QRCode(
    version = 10,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=2,
    border=3
)

data = input("Entre com a url: ")
name_file = input("Entre com o nome do arquivo: ")

if not name_file:
    name_file = "file.png"

if not "." in name_file:
    name_file = f"{name_file}.png"

qr.add_data(data)

qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save(name_file)