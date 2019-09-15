__author__ = "Rahul Chowdhury"
import os
import shutil
def main():
    src_images = "../data/Corresponding Images/"
    src_annotated = "../data/Annotated  2/"
    images_dir = "../data/images/"
    tagged_dir = "../data/tagged/"

    #clean images folder and tagged folder if either already exists
    if os.path.exists(images_dir):
        shutil.rmtree(images_dir)
    if os.path.exists(tagged_dir):
        shutil.rmtree(tagged_dir)
    # else create images dir with all the data from downloaded image folder
    os.mkdir(images_dir)
    os.mkdir(tagged_dir)

    #copy the annotated files from annotated folder into tagged/ only if there is a corresponding_image_file
    src_annotated_files = os.listdir(src_annotated)
    src_images_files = os.listdir(src_images)


    i = 1
    for file in src_annotated_files:
        #print(file)

        full_file_name = os.path.join(src_annotated,file)
        corresponding_image_name_substring = file[:file.find('.xml')]

        #matching[0] will contain the corrresponding image file name
        matching = list(filter(lambda x: corresponding_image_name_substring in x, src_images_files))


        #copy xml file to the tagged/
        shutil.copyfile(src_annotated+file,tagged_dir+file)
        #rename the file
        os.rename(tagged_dir+file,tagged_dir + str(i) + ".xml")

        #copy image files to images/
        if len(matching) != 0: #there is a matching image file
            shutil.copyfile(src_images+matching[0],images_dir+matching[0])
            #rename the file
            os.rename(images_dir+matching[0],images_dir + str(i) + ".jpg")
            i+=1






#driver code
if __name__ == "__main__":
    main()
