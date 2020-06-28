__author__ = "Rahul Chowdhury"

import sys
import os
import shutil
import xml.etree.ElementTree as ET

def main():
	
	PATH_TO_TEST_XML_DIR = sys.argv[1]
	
	
	xml_file_list = os.listdir(PATH_TO_TEST_XML_DIR)
	#print(xml_file_list)
	
	#saving the xml files with burrow annotation to clean_annotated dir
	PATH_TO_CLEAN = '../data/clean_annotated/'
	
	if os.path.exists(PATH_TO_CLEAN):
          shutil.rmtree(PATH_TO_CLEAN)

	os.mkdir(PATH_TO_CLEAN)

	
	for xml_file in xml_file_list:
		
		if not xml_file.startswith('.'): #ignore .DS_Store files
			PATH_TO_TEST_XML_FILE = PATH_TO_TEST_XML_DIR + xml_file
			
			root = ET.parse(PATH_TO_TEST_XML_FILE).getroot()
			
			if root.findall('object')[0][0].text != 'NO BURROWS':
				print(PATH_TO_TEST_XML_FILE)
				shutil.copyfile(PATH_TO_TEST_XML_FILE,PATH_TO_CLEAN + xml_file)









if __name__ == "__main__":
    main()
