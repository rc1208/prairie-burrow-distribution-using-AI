#!/usr/bin/python

import sys
import os
import shutil
import math

def main():
    if len(sys.argv) == 2:
        split_ratio = float(sys.argv[1])

        #remove previous directories if they exist and create new ones
        data_folder_str = "../data/"
        dir_list = ['images_train','images_test','tagged_train','tagged_test']
        new_dir_list = [data_folder_str + s for s in dir_list]
        for dir in new_dir_list:
            if os.path.exists(dir):
                shutil.rmtree(dir)
            os.mkdir(dir)

        #split images
        image_files = os.listdir(data_folder_str + "images/")
        #print(len(image_files))
        training_image_num = math.ceil(split_ratio * len(image_files))

        i = 1
        for file in image_files:
            print(file)
            xml_file = file[:file.find('.')] +'.xml'
            print(xml_file)
            if i <= training_image_num:
                shutil.copyfile(data_folder_str+'/images/'+file, data_folder_str+'/images_train/'+file)
                shutil.copyfile(data_folder_str+'/tagged/'+xml_file, data_folder_str+'/tagged_train/'+xml_file)
            else:
                shutil.copyfile(data_folder_str+'/images/'+file, data_folder_str+'/images_test/'+file)
                shutil.copyfile(data_folder_str+'/tagged/'+xml_file, data_folder_str+'/tagged_test/'+xml_file)

            i+=1


    else:
        print("****ERROR**** \n PROPER USAGE: python split_data.py split_ratio")
        return


if __name__ == "__main__":
    main()
