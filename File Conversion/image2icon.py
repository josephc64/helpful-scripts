# Joseph Peterson
# 01/06/2024
# Image2Icon - Converts any image file to multi-size ICO file

import os
import sys
from PIL import Image

def convertImageToIco(filename):
    try:
        img = Image.open(filename)
        icon_sizes = [(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]
        img.save(filename.rsplit('.', 1)[0] + '.ico', sizes=icon_sizes)
    except IOError:
        print(f"Cannot convert {filename}. Unsupported file format.")

def main():
    if len(sys.argv) > 1: #If there are files specified, process them
        for file in sys.argv[1:]:
            convertImageToIco(file)
    else: #If there are no files, run in the current directory
        for file in os.listdir('.'):
            if '.' in file:
                convertImageToIco(file)

if __name__ == "__main__":
    main()
