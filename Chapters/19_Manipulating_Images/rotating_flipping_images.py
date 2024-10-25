from PIL import Image

cat_image = Image.open('zophie.png')
cat_image.rotate(90).save('rotated90.png')
cat_image.rotate(180).save('rotated180.png')
cat_image.rotate(270).save('rotated270.png')

cat_image.rotate(6).save('rotated6.png')
cat_image.rotate(6, expand = True).save('rotate6_expanded.png')

cat_image.transpose(Image.FLIP_LEFT_RIGHT).save('horizontal_flip.png')
cat_image.transpose(Image.FLIP_TOP_BOTTOM).save('vertical_flip.png')