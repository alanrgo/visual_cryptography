import cv2 as cv
import numpy as np
import argparse
import os
import resources as rs
import printfy
from enum import Enum

class Color(Enum):
    BLACK = 0
    WHITE = 255

class FourChannelColor(Enum):
    BLACK = (0, 0, 0, 255)
    WHITE = (255, 255, 255, 1)
    TRANSPARENT = (255, 255, 255, 0)

destination_folder = "ciphered"

def paint_pattern_1(c_img, row, col, p_size):

    for r in range(p_size*2*row, p_size*(2*row+1)):
        for c in range(p_size*2*col, p_size*(2*col+1)):
            c_img[r][c] = Color.WHITE.value

    for r in range( p_size*2*row, p_size*(2*row+1) ):
        for c in range( p_size*(2*col+1), p_size*(2*col+2) ):
            c_img[r][c] = Color.BLACK.value
    
    for r in range( p_size*(2*row+1), p_size*(2*row+2)):
        for c in range( p_size*2*col, p_size*(2*col+1)):
            c_img[r][c] = Color.BLACK.value

    for r in range( p_size*(2*row+1), p_size*(2*row+2) ):
        for c in range( p_size*(2*col+1), p_size*(2*col+2) ):
            c_img[r][c] = Color.WHITE.value

def paint_pattern_2(c_img, row, col, p_size):

    for r in range(p_size*2*row, p_size*(2*row+1)):
        for c in range(p_size*2*col, p_size*(2*col+1)):
            c_img[r][c] = Color.BLACK.value

    for r in range( p_size*2*row, p_size*(2*row+1) ):
        for c in range( p_size*(2*col+1), p_size*(2*col+2) ):
            c_img[r][c] = Color.WHITE.value
    
    for r in range( p_size*(2*row+1), p_size*(2*row+2)):
        for c in range( p_size*2*col, p_size*(2*col+1)):
            c_img[r][c] = Color.WHITE.value

    for r in range( p_size*(2*row+1), p_size*(2*row+2) ):
        for c in range( p_size*(2*col+1), p_size*(2*col+2) ):
            c_img[r][c] = Color.BLACK.value


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

def save_img(c_img_1, c_img_2, name):
    img_1_name = name + "_cipher1.png"
    img_2_name = name + "_cipher2.png"
    summed_name = name + "_summed.png"

    summed = c_img_1 + c_img_2
    summed[summed==255] = 0
    summed[summed>255] = 255

    img_folder = destination_folder + "/" + name 
    if not os.path.isdir(img_folder):
        os.makedirs(img_folder)
    
    rs.save_img(c_img_1, img_folder + "/" + img_1_name)
    rs.save_img(c_img_2, img_folder  + "/" + img_2_name)
    rs.save_img(summed, img_folder  + "/" + summed_name)
    return

def execute(args, parser):
    file_names = []

    if args.file:
        file_names.append(args.file)

    size_factor = args.pixelsize*2
    if args.size:
        original_resize = (int (args.size[0]/size_factor), int(args.size[1]/size_factor))

    for file in file_names:

        # set reading options
        options = 0
        if args.istransparent:
            options = cv.IMREAD_UNCHANGED
        img = rs.load_img(file, options)

        if args.istransparent:
            img = rs.transparent_to_white(img)
        if args.size:
            img = rs.resize( original_resize[0], original_resize[1], img)
        img = rs.img_to_binary_img(img)

        c_img_1, c_img_2 = cipher_img(img, args.pixelsize)
        return c_img_1, c_img_2

def get_parser():
    parser = argparse.ArgumentParser(description="Process image into ciphered ones based on visual cryptography.")
    parser.add_argument("-f", "--file", help="Specify name of the file from inside folder original that will be ciphered")
    parser.add_argument("-s", "--size", nargs=2, type=int, help="final size of ciphered img")
    parser.add_argument("-p", "--pixelsize", type=int, default=1, help="make the pixels 'bigger'")
    parser.add_argument("-t", "--istransparent", type=bool, default=False, help="inform whether img has alpha channel")
    return parser

if __name__ == '__main__':
    parser = get_parser()
    execute(parser.parse_args, parser)