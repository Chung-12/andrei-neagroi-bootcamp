import sys
import os
from PIL import Image

parent_dir  = sys.argv[1]
new_dir = sys.argv[2]
path = '.\\' + parent_dir + new_dir

print(path)

if not os.path.exists(new_dir):
    os.mkdir(new_dir)

for filename in os.listdir(parent_dir):
    img = Image.open(f"{parent_dir}{filename}")
    clean_name = os.path.splitext(filename)[0]
    img.save(f"{new_dir}{clean_name}.png", "png")
    print("all done!")