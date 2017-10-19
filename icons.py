import os
import re
import math
from itertools import zip_longest

global icons
global default_icon
icons = []
global grid

_nsre = re.compile('([0-9]+)')
def natural_sort_key(s):
    return [int(text) if text.isdigit() else text.lower()
            for text in re.split(_nsre, s)]


for root, dirs, files in os.walk("icons/"):
    for file in files:
        if file.endswith('.png'):
            icons.append(file)

icons.sort(key=natural_sort_key)

default_icon = icons[63]

grid = [icons[5*i:5*i+5] for i in range(0,math.ceil(len(icons)/5))]
