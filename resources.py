import cv2 as cv
import numpy as np
import argparse
import os
from enum import Enum

class Color(Enum):
    BLACK = 0
    WHITE = 255

class FourChannelColor(Enum):
    BLACK = (0, 0, 0, 255)
    WHITE = (255, 255, 255, 255)
    TRANSPARENT = (255, 255, 255, 0)

def load_img(name, load_type = 0):
    path = os.getcwd() + "/" + name
    img = cv.imread(path, load_type)
    return img

def save_img(img, output=""):
    path = os.getcwd() + "/" + output
    cv.imwrite( path, img )

def show(img):
    cv.imshow('image',img)
    cv.waitKey(0)
    cv.destroyAllWindows()

def img_to_binary_img(img):
    ret,thresh1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
    return thresh1

def resize(rows, cols, img):
    return cv.resize(img, (rows, cols))

def transparent_to_white(img):
    shape = (img.shape[0], img.shape[1])
    whitened_img = np.zeros(shape)
    whitened_img = img[:,:,3]
    whitened_img = 255 - whitened_img
    whitened_img[whitened_img<=127] = 0
    whitened_img[whitened_img>127] = 255
    return whitened_img