import cv2 as cv
import numpy as np
import argparse
import os
import resources as rs
from enum import Enum

parser = argparse.ArgumentParser(description="Process image into ciphered ones based on visual cryptography.")
parser.add_argument("-f", "--file", help="Specify relative path of the file from inside folder original that will be ciphered")
parser.add_argument("-o", "--output", help="Specify the path for output file")
parser.add_argument("-p", "--pixel", type=int, default=2, help="Set different pixel size")
args = parser.parse_args()

def amplify(img, p):
    new_size = (img.shape[0]*p, img.shape[1]*p)
    bigger_img = np.zeros(new_size)
    for r in range(0, img.shape[0]):
        for c in range(0, img.shape[1]):
            for r_prime in range(p*r, p*(r+1)):
                for c_prime in range(p*c, p*(c+1)):
                    bigger_img[r_prime][c_prime] = img[r][c]
    return bigger_img

def process():
    img = rs.load_img(args.file)
    a_img = amplify(img, args.pixel)
    rs.save_img(a_img, args.output)

if __name__ == '__main__':
    process()