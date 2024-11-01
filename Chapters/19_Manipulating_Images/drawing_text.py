from PIL import ImageFont
import os

from PIL import ImageDraw, Image, ImageFont

image = Image.new('RGBA', (200, 200), 'white')
draw = ImageDraw.Draw(image)

draw.text((20,150), 'Hello', fill = 'purple')
fonts_folder = r"C:\Windows\Fonts"

arial_font = ImageFont.truetype(os.path.join(fonts_folder, 'arial.ttf'), 32)

draw.text((100, 150), 'Howdy', fill = 'gray', font = arial_font)

image.save('text.png')