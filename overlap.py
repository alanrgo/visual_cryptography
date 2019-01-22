import cv2 as cv
import numpy as np
import argparse
import os
import resources as rs
from enum import Enum

parser = argparse.ArgumentParser(description="Process image into ciphered ones based on visual cryptography.")
parser.add_argument("-b", "--base", help="Specify relative path of the file from inside folder original that will be ciphered")
parser.add_argument("-i", "--input", help="Image that will replace part of the base")
parser.add_argument("-s", "--size", nargs=2, type=int, help="final size of ciphered img")
parser.add_argument("-o", "--output", help="Specify the path for output file")
args = parser.parse_args()

def overlap(base, img, r_o, c_o):
    for r in range(0, img.shape[0]):
        for c in range(0, img.shape[1]):
            base[ r_o + r ][ c_o + c ] = img[r][c]
    return base

def img_to_printed(img):
    shape = (img.shape[0], img.shape[1], 4)
    printed_img = np.zeros(shape)

    for r in range(0, img.shape[0]):
        for c in range(0, img.shape[1]):
            if img[r][c] == rs.Color.WHITE.value:
                printed_img[r][c][0] = rs.FourChannelColor.TRANSPARENT.value[0]
                printed_img[r][c][1] = rs.FourChannelColor.TRANSPARENT.value[1]
                printed_img[r][c][2] = rs.FourChannelColor.TRANSPARENT.value[2]
                printed_img[r][c][3] = rs.FourChannelColor.TRANSPARENT.value[3]
            if img[r][c] == rs.Color.BLACK.value:
                printed_img[r][c][0] = rs.FourChannelColor.BLACK.value[0]
                printed_img[r][c][1] = rs.FourChannelColor.BLACK.value[1]
                printed_img[r][c][2] = rs.FourChannelColor.BLACK.value[2]
                printed_img[r][c][3] = rs.FourChannelColor.BLACK.value[3]
    return printed_img

def process():
    base = load_img(args.base)
    img = load_img(args.input)
    final = overlap(base, img, args.size[0], args.size[1])
    return final

if __name__ == '__main__':
    process()