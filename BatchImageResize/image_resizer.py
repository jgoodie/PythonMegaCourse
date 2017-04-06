#!/usr/local/opt/python3/bin/python3

import cv2, os
from re import split

orig = "/Users/jgoodman/Documents/HCP Anywhere/workspaces/PythonMegaCourse/BatchImageResize/originals/"
resized = "/Users/jgoodman/Documents/HCP Anywhere/workspaces/PythonMegaCourse/BatchImageResize/resized/"
factor = 2

os.chdir(orig)
files = os.listdir(os.getcwd())
for x in files:
    os.chdir(orig)
    img = cv2.imread(x, 0)
    if x == ".DS_Store":
        pass
    else:
        resizedimg = cv2.resize(img,(int(img.shape[1]/factor),int(img.shape[0]/factor)))
        #print(x.split('.')[0]+"_resized.jpg")
        os.chdir(resized)
        cv2.imwrite(x.split('.')[0]+"_resized.jpg", resizedimg)