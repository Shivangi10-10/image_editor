from PIL import Image, ImageEnhance, ImageFilter
import os

path = './assets'
pathOut = './editedImgs'

# Create the output directory if it doesn't exist
os.makedirs(pathOut, exist_ok=True)

for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")
    edit = img.filter(ImageFilter.SHARPEN).convert('L')
    clean_name = os.path.splitext(filename)[0]
    edit.save(f"{pathOut}/{clean_name}_edited.jpg")
