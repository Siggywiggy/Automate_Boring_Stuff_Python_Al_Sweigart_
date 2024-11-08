from PIL import Image

image = Image.new('RGBA', (100, 100))

print(image.getpixel((0, 0)))