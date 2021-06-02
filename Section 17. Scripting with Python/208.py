from PIL import Image, ImageFilter

img = Image.open('208_astro.jpg')
img.thumbnail((400, 400))
img.save('new_astro.jpg')
print(img.size)
