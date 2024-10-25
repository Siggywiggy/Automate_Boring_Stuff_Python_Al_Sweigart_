from PIL import Image
cat_image = Image.open('zophie.jpg')
cat_image_copy = cat_image.copy()

cat_face_image = cat_image.crop((124, 138, 234, 220))
print(cat_face_image.size)

cat_image_copy.paste(cat_face_image,(0,0))
cat_image_copy.paste(cat_face_image,(202,293))
cat_image_copy.save('pasted.png')