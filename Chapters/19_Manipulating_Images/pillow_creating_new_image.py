from PIL import Image

image = Image.new('RGBA', (100,200), 'purple')
image.save('purple_image.png')

image2 = Image.new('RGBA', (20,20))
image2.save('transparent_image.png')