import cipher
import resources
import intersection
import amplify
import printfy
import overlap
import os
import numpy as np
import cv2 as cv

def process():

    # create empty matrix with size 600x400
    card = np.zeros((400, 600))

    # for each folder in folder people
    path = "./people"
    folders = os.listdir(path)

    for folder in folders:
        if "ciphered" in folder:
            continue
        person_path = path + "/" + folder 
        files = os.listdir(person_path)
        files = sorted(files)
        
        # img_1 receives frst image
        img_1 = resources.load_img( person_path + "/" + files[0] )
        img_1 = resources.img_to_binary_img(img_1)
        
        parser = cipher.get_parser()
        args = parser.parse_args(['-f', person_path + "/" + files[0], '-p', '1'])
        base, complement = cipher.execute(args, parser)

        amplified_base = amplify.amplify(base, 2)
        amplified_complement = amplify.amplify(complement, 2)
        summed = amplified_complement + amplified_base
        summed[summed==255] = 0
        summed[summed>255] = 255
        resources.save_img(amplified_complement, person_path + "_ciphered/" + files[0].split(".")[0].split("/")[-1] + ".png")
        resources.save_img(summed, person_path + "_ciphered/" + files[0].split(".")[0].split("/")[-1] + "_summed.png")
        
        # first object of the map
        overlap.overlap(card, amplified_complement, 0, 0)

        print(files)
        j = 0
        # for each img of the rest
        for i in range(1, len(files)):
            source = person_path + "/" + files[i]
            img = resources.load_img( source )
            img = resources.img_to_binary_img(img)
            print(files[i])

            # intersection share from img
            img = intersection.intersection(img, img_1, base, complement)
            img = amplify.amplify(img, 2) 

            summed = img + amplified_base
            summed[summed==255] = 0
            summed[summed>255] = 255
            resources.save_img(img, person_path + "_ciphered/" + files[i].split(".")[0].split("/")[-1] + ".png")
            resources.save_img(summed, person_path + "_ciphered/" + files[i].split(".")[0].split("/")[-1] + "_summed.png")

            if i%3 == 0:
                j = 1
            overlap.overlap(card, img, j*200, (i%3)*200)
        
        amplified_base = printfy.img_to_printed(amplified_base)
        resources.save_img(amplified_base, person_path + "_ciphered/ciphered_base.png" )
        resources.save_img(card,person_path + "_ciphered/final_map.png" )
        

process()