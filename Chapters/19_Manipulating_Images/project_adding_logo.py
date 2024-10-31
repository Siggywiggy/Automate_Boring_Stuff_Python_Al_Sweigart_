#! python3
# Resizes all images in current working directory to fit
# in a 300x300 square, and adds catlogo.jpg
# to the lower-right corner.

import os
from PIL import Image

square_fit_size = 300
logo_filename = 'catlogo.jpg'

logo_image = Image.open(logo_filename)
logo_width, logo_height = logo_image.size

# TODO: Loop over all files in the working directory.

for filename in os.listdir('.'):
    if not (filename.endswith('.png') or filename.endswith('.jpg')) or filename == logo_filename:
        continue # skips non-image files and the logo file itself

    image = Image.open(filename)
    width, height = image.size

# TODO: Check if image needs to be resized.

# TODO: Calculate the new width and height to resize to.

# TODO: Resize the image.

# TODO: Add the logo.

# TODO: Save changes.