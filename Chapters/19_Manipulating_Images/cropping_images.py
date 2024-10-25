from PIL import Image

cat_image = Image.open('zophie.png')
cropped_image = cat_image.crop((124, 138, 234, 220))

cropped_image.save('cropped_zophie.png')