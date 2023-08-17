from PIL import Image

file_dir = "/Users/roxyyujin/Desktop/Profile/"
image = Image.open(file_dir + "IMG_9995.JPG")

xsize, ysize = image.size
resized = image.resize((xsize // 4, ysize // 4))
resized.save(file_dir + "IMG_9995_resized.JPG")

cropped = image.crop((0, 0, xsize // 2, ysize // 2))
cropped.save(file_dir + "IMG_9995_cropped.JPG")
