#! python3
# Resizes all images in current working directory to fit
# in a 300x300 square, and adds catlogo.jpg
# to the lower-right corner.

import os

import PIL.ImageOps
from PIL import Image

square_fit_size = 300
logo_filename = 'catlogo.jpg'
process_filetypes = ['png', 'jpg', 'gif', 'bmp']

logo_image = Image.open(logo_filename).convert('RGBA')
logo_width, logo_height = logo_image.size
halved_logo_image = logo_image.resize((int(logo_width / 2), int(logo_height / 2)))
#halved_logo_image = PIL.ImageOps.fit(logo_image, (120,120) )
logo_width, logo_height = halved_logo_image.size


os.makedirs('with_logo', exist_ok=True)

# Loop over all files in the working directory.

file_names_current_folder = (os.listdir('.'))

for filename in file_names_current_folder:
    if filename.split('.')[-1].lower() not in process_filetypes or filename == logo_filename:
        continue # skips non-image files and the logo file itself

    image = Image.open(filename)
    print(f'opening {filename}')
    width, height = image.size

    # Check if the image is too small  - less than 2x size of the logo image
    if (logo_width * 2 > width) or (logo_height * 2 > height):
        print(f'{filename} too small! Width is {width} and height is {height}  - logo size is {logo_width} x {logo_height}')
        continue

    # Check if image needs to be resized.
    if width > square_fit_size and height > square_fit_size:

    # Calculate the new width and height to resize to.

        if width > height:
            height = int((square_fit_size / width) * height)
            width = square_fit_size
        else:
            width = int((square_fit_size / height) * width)
            height = square_fit_size

        # Resize the image.

        print('Resizing %s...' % (filename))

        image = image.resize((width, height))

        # Add the logo.
        print('Adding logo to %s...' % (filename))
        image.paste(halved_logo_image, (width - logo_width, height - logo_height), halved_logo_image)


        # Save changes.
        image.save(os.path.join('with_logo', filename))