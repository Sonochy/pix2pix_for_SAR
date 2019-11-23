from PIL import Image
import sys
import os
import re

input_path = "./png_to_jpg/input/"
output_path = "./png_to_jpg/output/"
files = os.listdir(input_path)
print(files)
count = 1

for file in files:
    if file[-4:] == ".png":
        input_im = Image.open(input_path + file)
        rgb_im = input_im.convert('RGB')
        rgb_im.save(output_path + os.path.splitext(file)[0] + ".jpg",quality=100)
        count = count + 1
        print("transaction finished" + str(count))
