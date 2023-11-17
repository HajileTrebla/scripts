#!/usr/bin/env python

import os
import re
from PIL import Image

def convImg(path, newPath):
    img = Image.open(path)
    img.save(newPath)
    print(newPath + ' has been converted')

def getPngPath(path):
    match = re.search(r'(^.+)\.jpg', path) 
    if match:
        newPath = f"{os.getcwd()}/data/{match.group(1)}.png"
        return os.path.normpath(newPath)
    return

def isJpg(path):
    match = re.search(r'^.+\.jpg', path) 
    if match:
        return path
    return

def findImg(path):
    imgPaths = []

    lsDir = os.listdir(path)
    for child in lsDir:
        if isJpg(child):
            imgPaths.append(child)

    return imgPaths

def main():
    dir = os.getcwd()
    jpgImgs = findImg(dir)
    for img in jpgImgs:
        newPath = getPngPath(img)
        convImg(img, newPath)
    
if __name__ == "__main__":
    main()
