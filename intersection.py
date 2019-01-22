import cv2 as cv
import numpy as np
import argparse
import os
import resources as rs
from enum import Enum

parser = argparse.ArgumentParser(description="Process image into ciphered ones based on visual cryptography.")
parser.add_argument("-a", "--all", action="store_true", help="Turn all the images inside folder Original into ciphered images.")
parser.add_argument("-f", "--file", help="Specify name of the file from inside folder original that will be ciphered")
parser.add_argument("-s", "--size", nargs=2, type=int, help="final size of ciphered img")
args = parser.parse_args()

destination_folder = "/arrows/ciphered"

def cipher_img(img, p_size):
    c_size = (img.shape[0]*2*p_size, img.shape[1]*2*p_size)
    c_img_1 = np.zeros(c_size)
    c_img_2 = np.zeros(c_size)
    
    for col in range(0, img.shape[1]):
        for row in range(0, img.shape[0]):
            coin = np.random.random_sample()
            if coin < 0.5:
                if img[row][col] == 0:
                    paint_pattern_1(c_img_1, row, col, p_size)
                    paint_pattern_2(c_img_2, row, col, p_size)
                if img[row][col] == 255:
                    paint_pattern_1(c_img_1, row, col, p_size)
                    paint_pattern_1(c_img_2, row, col, p_size)
            else:
                if img[row][col] == 0:
                    paint_pattern_2(c_img_1, row, col, p_size)
                    paint_pattern_1(c_img_2, row, col, p_size)
                if img[row][col] == 255:
                    paint_pattern_2(c_img_1, row, col, p_size)
                    paint_pattern_2(c_img_2, row, col, p_size)
    return c_img_1, c_img_2

def resize(rows, cols, img):
    return cv.resize(img, (rows, cols))

def save_img(c_img_1, c_img_2, name):
    img_1_name = "cipher1" + name + ".png"
    img_2_name = "cipher2" + name + ".png"
    summed_name = "summed" + name + ".png"

    summed = c_img_1 + c_img_2
    summed[summed==255] = 0
    summed[summed>255] = 255

    img_folder = os.getcwd() + destination_folder + "/" + name
    print(img_folder)
    if not os.path.isdir(img_folder):
        os.makedirs(img_folder)
        
    cv.imwrite( img_folder + "/" + img_1_name, c_img_1 )
    cv.imwrite( img_folder + "/" + img_2_name, c_img_2 )
    cv.imwrite( img_folder + "/" + summed_name, summed )

def copy_pattern(img, base, r, c):
    img[2*r][2*c] = base[2*r][2*c]
    img[2*r][2*c+1] = base[2*r][2*c+1]
    img[2*r+1][2*c] = base[2*r+1][2*c]
    img[2*r+1][2*c+1] = base[2*r+1][2*c+1]

def copy_complement(img, base, r, c):
    img[2*r][2*c] = 255-base[2*r][2*c]
    img[2*r][2*c+1] = 255-base[2*r][2*c+1]
    img[2*r+1][2*c] = 255-base[2*r+1][2*c]
    img[2*r+1][2*c+1] = 255-base[2*r+1][2*c+1]
    

def intersection(img_p, img_k, base, complement):
    new_shape = (img_p.shape[0]*2, img_p.shape[1]*2)
    new_ciphered_img = np.zeros(new_shape)

    for r in range(0, img_p.shape[0]):
        for c in range(0, img_p.shape[1]):

            if img_p[r][c] == rs.Color.BLACK.value and img_k[r][c] == rs.Color.BLACK.value:
                copy_pattern(new_ciphered_img, complement, r, c)

            if img_p[r][c] == rs.Color.BLACK.value and img_k[r][c] == rs.Color.WHITE.value:
                copy_complement( new_ciphered_img, base, r, c )

            if img_p[r][c] == rs.Color.WHITE.value and img_k[r][c] == rs.Color.BLACK.value:
                copy_pattern(new_ciphered_img, base, r, c)

            if img_p[r][c] == rs.Color.WHITE.value and img_k[r][c] == rs.Color.WHITE.value:
                copy_pattern(new_ciphered_img, base, r, c)
    rs.show(new_ciphered_img)
    return new_ciphered_img
                

def process():
    file_names = []
    img = []


if __name__ == '__main__':
    process()