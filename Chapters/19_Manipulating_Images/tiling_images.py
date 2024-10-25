from PIL import Image

cat_image = Image.open('zophie.png')

print(cat_image.size)

cat_face_image = cat_image.crop((124, 138, 234, 220))

print(cat_face_image.size)

cat_image_copy = cat_image.copy()

width, height = cat_image.size

for left in range(0, cat_image_copy.width, cat_face_image.width):
    for top in range(0, cat_image_copy.height, cat_face_image.height):
        print(left, top)
        cat_image_copy.paste(cat_face_image, (left, top))

cat_image_copy.save('tiled.png')