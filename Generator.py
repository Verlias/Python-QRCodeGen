import qrcode

def Generate(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    return img 

if __name__ == "__main__":
    data = input("Enter the data to be encoded (Or Link): ")
    img = Generate(data)
    img.show()