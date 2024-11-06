#! python 3

import os

import PIL
from PIL import Image, UnidentifiedImageError

process_filetypes = ['jpg']

for folder_name, subfolders, filenames in os.walk('C:\\'):
    #print(f'{subfolders}')
    #print(f'{folder_name}')
    num_photo_files = 0
    num_non_photo_files = 0
    for filename in filenames:
        # check if file extension NOT .png or jpg
        if filename.split('.')[-1].lower() not in process_filetypes:
            #print('not a photo file!')
            num_non_photo_files += 1
            continue
        image_path = os.path.join(folder_name, filename)
        # else open file with Pillow
        try:
            with Image.open(image_path) as image:

                # image = Image.open(image_path)
                width, height = image.size

                # check if width & height are larger than 500
                if width > 500 and height > 500:
                    num_photo_files += 1
                else:
                    num_non_photo_files += 1

        except PIL.UnidentifiedImageError as exception:
            print(f"cannot open {filename}")
            pass


    if num_photo_files / 2 > num_non_photo_files:
        #print(os.path.join(os.getcwd(), filename))
        print(f'photos in {folder_name}')