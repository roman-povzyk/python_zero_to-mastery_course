from PIL import Image, ImageFilter

img = Image.open('Pokedex/206_pikachu.jpg')
filtered_img = img.filter(ImageFilter.SMOOTH)
filtered_img.save('blur', 'png')

filtered_img = img.convert('L')
filtered_img.save('grey.png', 'png')
# filtered_img.show()

print(img.format)
print(img.size)
print(img.mode)
print(dir(img))