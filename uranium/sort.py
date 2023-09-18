import os
import shutil
from PIL import Image

directories = {"gen5": [], "gen5-back": [], "gen5-shiny": [], "gen5-back-shiny": []}

for directory in directories.keys():
    for filename in os.listdir(directory):
        if filename.endswith(".png"):
            directories[directory].append(filename.lower())
            im = Image.open(directory + "/" + filename)
            width, height = im.size
            if width != height:
                im = im.crop((0, 0, 80, 80))
                im.save(directory + "/" + filename)
        
def compare(list1, list2):
    for item in list2:
        if item not in list1:
            print(item)



compare(directories["gen5-shiny"], directories["gen5"])