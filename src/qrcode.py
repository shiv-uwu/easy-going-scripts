# ---------------- #
# MADE BY SHIV-UWU #
# ---------------- #

import qrcode  # Import the qrcode library

# Define the link that you want to encode in the QR code
link = "https://www.example.com"

# Create a QR code instance with the link
qr = qrcode.QRCode(
    # Choose the QR code version (1-40, larger numbers mean more data capacity)
    version=1,
    # Choose the error correction level (L, M, Q, H)
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    # Choose the size of each box in the QR code image (in pixels)
    box_size=10,
    border=4,  # Choose the size of the border around the QR code (in boxes)
)

qr.add_data(link)  # Add the data (the link) to the QR code instance
qr.make(fit=True)  # Generate the QR code image based on the data

# Create the QR code image with black boxes and white background
img = qr.make_image(fill_color="black", back_color="white")

img.save("qrcode.png")  # Save the QR code image as a PNG file
