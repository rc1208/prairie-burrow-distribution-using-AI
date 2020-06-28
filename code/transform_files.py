#!/usr/bin/env python3
__author__ = "Rahul Chowdhury"

import os
import re
import shutil

class TransformFiles:
    def __init__(self, src_images, src_annotated, images_dir, tagged_dir):
        self.src_images = src_images
        self.src_annotated = src_annotated
        self.images_dir = images_dir
        self.tagged_dir = tagged_dir

    #clean images folder and tagged folder if either already exists
    def cleanFolders(self):
       if os.path.exists(self.images_dir):
           shutil.rmtree(self.images_dir)
       if os.path.exists(self.tagged_dir):
           shutil.rmtree(self.tagged_dir)

    # create images dir with all the data from downloaded image folder
    def createFolders(self):
       os.mkdir(self.images_dir)
       os.mkdir(self.tagged_dir)

    #copy the annotated files from annotated folder into tagged/ only if there is a corresponding_image_file
    def copyAndRenameFiles(self):
       src_annotated_files = os.listdir(self.src_annotated)
       src_images_files = os.listdir(self.src_images)

       i = 1
       for file in src_annotated_files:
           #print(file)

           full_file_name = os.path.join(self.src_annotated,file)
           corresponding_image_name_substring = file[:file.find('.xml')]

           #matching[0] will contain the corrresponding image file name
           matching = list(filter(lambda x: corresponding_image_name_substring in x, src_images_files))


           #copy xml file to tagged/
           shutil.copyfile(self.src_annotated+file,self.tagged_dir+file)

           #replace the contents of the <filename> tag in the xml file with proper name
           with open(self.tagged_dir+file) as f:

                readText = f.read()
                newText = re.sub(r"<filename>.*</filename>", "<filename>"+ str(i) + ".jpg" + "</filename>", readText)

           with open(self.tagged_dir+file, "w") as f:
                f.write(newText)


           #rename the file
           os.rename(self.tagged_dir+file,self.tagged_dir + str(i) + ".xml")

           #copy image files to images/
           if len(matching) != 0: #there is a matching image file
               shutil.copyfile(self.src_images+matching[0],self.images_dir+matching[0])
               #rename the file
               os.rename(self.images_dir+matching[0],self.images_dir + str(i) + ".jpg")
               i+=1


# place variables here -> (downloaded image folder, downloaded annotated folder, dumping image folder, dumping annotated folder)
obj = TransformFiles("../data/2018/", "../data/clean_annotated/", "../data/images/", "../data/tagged/")
obj.cleanFolders()
obj.createFolders()
obj.copyAndRenameFiles()
