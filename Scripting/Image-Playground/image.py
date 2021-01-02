from PIL import Image, ImageFilter

img = Image.open('.\\Pokedex\\bulbasaur.jpg')
filtered_img = img.filter(ImageFilter.SMOOTH)
gray_img = img.convert("L")

filtered_img.save("smooth.png", "png")
gray_img.save("gray.png", "png")
