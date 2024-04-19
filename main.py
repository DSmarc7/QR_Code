import qrcode

# The URL where the PDF is hosted
url = 'http://127.0.0.1:5000/'

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save('static/pdf_qrcode.png')
