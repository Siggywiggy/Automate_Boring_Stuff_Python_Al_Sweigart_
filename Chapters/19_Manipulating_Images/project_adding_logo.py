#! python3
# Resizes all images in current working directory to fit
# in a 300x300 square, and adds catlogo.jpg
# to the lower-right corner.

import os

import PIL.ImageOps
from PIL import Image

square_fit_size = 300
logo_filename = 'catlogo.jpg'

logo_image = Image.open(logo_filename).convert('RGBA')
logo_width, logo_height = logo_image.size
halved_logo_image = logo_image.resize((int(logo_width / 2), int(logo_height / 2)))
#halved_logo_image = PIL.ImageOps.fit(logo_image, (120,120) )
logo_width, logo_height = halved_logo_image.size


os.makedirs('with_logo', exist_ok=True)

# TODO: Loop over all files in the working directory.

for filename in os.listdir('.'):
    if not (filename.endswith('.png') or filename.endswith('.jpg')) or filename == logo_filename:
        continue # skips non-image files and the logo file itself

    image = Image.open(filename)
    width, height = image.size

    # TODO: Check if image needs to be resized.
    if width > square_fit_size and height > square_fit_size:

    # TODO: Calculate the new width and height to resize to.

        if width > height:
            height = int((square_fit_size / width) * height)
            width = square_fit_size
        else:
            width = int((square_fit_size / height) * width)
            height = square_fit_size

        # TODO: Resize the image.

        print('Resizing %s...' % (filename))

        image = image.resize((width, height))

        # TODO: Add the logo.
        print('Adding logo to %s...' % (filename))
        image.paste(halved_logo_image, (width - logo_width, height - logo_height), halved_logo_image)


        # TODO: Save changes.
        image.save(os.path.join('with_logo', filename))