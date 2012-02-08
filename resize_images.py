#!/usr/bin/env python

import os
from PIL import Image

path = 'images/'
percent = 12;
for infile in os.listdir(path):
    image = Image.open(path + infile)
    width, height = image.size
    resized = image.resize((percent * width / 100, percent * height / 100), Image.ANTIALIAS)
    resized.save(path + infile + "_" + str(percent), "PNG")
