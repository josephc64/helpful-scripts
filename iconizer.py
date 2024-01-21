# Joseph Peterson
# 01/06/2024
# Iconizer - Converts PNG file to multi-size ICO file


import os
import shutil
from PIL import Image


def convertPngToIco(filename):
    if filename.lower().endswith('.png'):
        img = Image.open(filename)
        icon_sizes = [(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]
        img.save(filename.replace('.png', '.ico'), sizes=icon_sizes)


def main():
    for file in os.listdir('.'):
        convert_and_move_png(file)


if __name__ == "__main__":
    main()

