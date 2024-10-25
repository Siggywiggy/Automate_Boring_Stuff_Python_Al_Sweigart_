from PIL import Image
cat_image = Image.open('zophie.png')

width, height = cat_image.size

quarter_sized_image = cat_image.resize((int(width / 2), int(height / 2)))

quarter_sized_image.save('quartersized.png')

svelte_image = cat_image.resize((width, height + 300))

svelte_image.save('svelte.png')