__author__ = "Rahul Chowdhury"
import os
import shutil
class CleanTraining:
    def __init__(self, path_to_training):
        self.path_to_training = path_to_training

    def clean(self):
        for file in os.listdir(self.path_to_training):
            file_path = os.path.join(folder, the_file)
            print(file_path)
            '''
            try:
            if os.path.isfile(file_path) and file:
                os.unlink(file_path)
            '''
            ## TO DO ##


obj = CleanTraining("../data/training")
