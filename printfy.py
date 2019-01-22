import cv2 as cv
import numpy as np
import argparse
import os
import resources as rs
from enum import Enum

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
    print("not implemented")


if __name__ == '__main__':
    process()