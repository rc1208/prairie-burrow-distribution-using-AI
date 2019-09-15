# prarie-burrow-distribution-using-AI
> An AI project to leverage state-of-the-art neural networks to detect prarie burrows in aerial images. Project undertaken at  > University of Colorado, Boulder for [Laboratory for Interdisciplinary Statistical Analysis](https://www.colorado.edu/lab/lisa/). For more information, contact:
> 1. Rahul Chowdhury <rach4930@colorado.edu>
> 2. Patricia Todd <pato7216@colorado.edu>
 



## Resources:

1. The main motivation found from this Medium article: [Link](https://towardsdatascience.com/creating-your-own-object-detector-ad69dda69c85)
2. Oh, such a cool raccoon detector :) [Link](https://github.com/datitran/raccoon_dataset) 
3. LabelImg for image annotation. [Link](https://github.com/tzutalin/labelImg)
4. Tensorflow Object Detection API [Link](https://github.com/tensorflow/models/tree/master/research/object_detection)



## Code Shenanigans:

1. `transform_files.py` -> Python foo to easily map and correlate the annotated xml files to the corresponding image. Dump images and annotated files as specified in `src_images` and `src_annotated` variables. Finally, it dumps the annotated images in `data/images/` and annotated files in `data/tagged` 
