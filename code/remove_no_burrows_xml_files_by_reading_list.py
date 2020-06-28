__author__ = "Rahul Chowdhury"

import sys
import os
import shutil

def main():
	
	PATH_TO_TEST_XML_DIR = sys.argv[1]
	empty_list_str = sys.argv[2]
	empty_list = list(map(int, empty_list_str.strip('[]').split(',')))
	#print(PATH_TO_TEST_XML_DIR)
	
	xml_file_list = os.listdir(PATH_TO_TEST_XML_DIR)
	#print(xml_file_list)
	
	#saving the xml files with burrow annotation to clean_annotated dir
	PATH_TO_CLEAN = '../data/clean_annotated/'
	
	if os.path.exists(PATH_TO_CLEAN):
          shutil.rmtree(PATH_TO_CLEAN)

	os.mkdir(PATH_TO_CLEAN)
	
	print("empty list =" , empty_list)
	not_empty_list = []
	
	for xml_file in xml_file_list:
		
		if not xml_file.startswith('.'): #ignore .DS_Store files
			PATH_TO_TEST_XML_FILE = PATH_TO_TEST_XML_DIR + xml_file
			#print(PATH_TO_TEST_XML_FILE)
			first_dot = xml_file.find('.')
			second_dot = xml_file.find('.',first_dot+1)
			file_num = int(xml_file[first_dot+1:second_dot])
			if file_num not in empty_list:
				shutil.copyfile(PATH_TO_TEST_XML_FILE,PATH_TO_CLEAN + xml_file)
				#print(file_num)
				not_empty_list.append(file_num)

	print("not_empty=" ,not_empty_list)







if __name__ == "__main__":
    main()
