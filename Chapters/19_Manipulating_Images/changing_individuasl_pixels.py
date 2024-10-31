from PIL import Image

#getpixel() and putpixel(methods)

image = Image.new('RGBA', (100,100))
print(image.getpixel((0,0)))

for x in range(100):
    for y in range(50):
        image.putpixel((x,y), (210,210,210))

from PIL import ImageColor

for x in range(100):
    for y in range(50,100):
        image.putpixel((x,y), ImageColor.getcolor('darkgray', 'RGBA'))

print(image.getpixel((0,0)))

print(image.getpixel((0,50)))

image.save('put_pixel.png')