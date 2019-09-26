# prarie-burrow-distribution-using-AI
<img src="https://github.com/rc1208/prarie-burrow-distribution-using-AI/blob/master/Wikipedia-Black-Tailed_Prairie_Dog.jpg" width="250">
> An AI project to leverage state-of-the-art neural networks to detect prarie burrows in aerial images. Project undertaken at   University of Colorado, Boulder for [Laboratory for Interdisciplinary Statistical Analysis](https://www.colorado.edu/lab/lisa/). For more information, contact:
> 1. Patricia Todd <pato7216@colorado.edu>
> 2. Rahul Chowdhury <rach4930@colorado.edu>

 



## Resources:

1. The main motivation found from this Medium article: [Link](https://towardsdatascience.com/creating-your-own-object-detector-ad69dda69c85)
2. Oh, such a cool raccoon detector :) [Link](https://github.com/datitran/raccoon_dataset) 
3. LabelImg for image annotation. [Link](https://github.com/tzutalin/labelImg)
4. Tensorflow Object Detection API [Link](https://github.com/tensorflow/models/tree/master/research/object_detection)



## Code Shenanigans:

1. `transform_files.py` -> Python foo to easily map and correlate the annotated xml files to the corresponding image. Dump images and annotated files as specified in `src_images` and `src_annotated` variables. Also, makes sure that the `<filename></filename>` tag in the xml file has the corresponding consistent file name. Finally, it dumps the annotated images in `data/images/` and annotated files in `data/tagged` 

2. `split_data.py` -> *Usage: python split_data.py split_ratio* <br />
Example: `python split_data.py .80` will split the data and annotated folders into 80% and 20% for training and testing purposes and dump them into respective folders -> `['images_train','images_test','tagged_train','tagged_test']`

3. `xml_to_csv.py` -> Coverts the xml information in the `tagged_train` and `tagged_test` folders into corresponding `csv` files.

4. `generate_tfrecord.py` -> Adopted this guy from this awesome raccoon detector project [Check it out!](https://github.com/datitran/raccoon_dataset). This code will create the TFRecords for each data point in our training and testing data set. To read more why this step is essential, read more about TFRecords [here](https://medium.com/mostly-ai/tensorflow-records-what-they-are-and-how-to-use-them-c46bc4bbb564) <br />
*Usage: python generate_tfrecord.py --csv_input=../data/tagged_train_labels.csv --image_dir=../data/images_train/ --output_path=../data/train.record <br />
python generate_tfrecord.py --csv_input=../data/tagged_test_labels.csv --image_dir=../data/images_test/ --output_path=../data/test.record*

5. To train the model -> `python model_main.py --logtostderr --train_dir=../../data/training/ --pipeline_config_path=../../data/training/faster_rcnn_inception_v2_pets.config` NOTE: Facing issues here of conversion of sparse matrix into dense matrix.
