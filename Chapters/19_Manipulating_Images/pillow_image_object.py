from PIL import Image

cat_image = Image.open('zophie.jpg')

print(cat_image.size)
width, height = cat_image.size
print(width)
print(height)

print(cat_image.filename)
print(cat_image.format)
print(cat_image.format_description)

cat_image.save('zophie.png')