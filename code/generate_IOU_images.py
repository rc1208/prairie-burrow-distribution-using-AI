for image_path in TEST_IMAGE_PATHS[:1]:
    print(image_path)
    image = Image.open(image_path)
    plt.figure(figsize=IMAGE_SIZE)
    image_np = load_image_into_numpy_array(image) #a numpy array with shape [height, width, 3]
    image_np_expanded = np.expand_dims(image_np, axis=0)
    # Actual detection.
    output_dict = run_inference_for_single_image(image_np_expanded, detection_graph)
    #TODO - Design python foo to read this from the XML file
    '''
    <xmin>42</xmin>
	<ymin>90</ymin>
	<xmax>87</xmax>
	<ymax>125</ymax>
    
    <xmin>159</xmin>
	<ymin>148</ymin>
	<xmax>250</xmax>
	<ymax>234</ymax>
    '''
    vis_util.draw_bounding_box_on_image_array(image_np, 90, 42, 125, 87, color='red', thickness = 2, use_normalized_coordinates = False)
    vis_util.draw_bounding_box_on_image_array(image_np, 148, 159, 234, 250, color='red', thickness = 2, use_normalized_coordinates = False)
    
    
    vis_util.visualize_boxes_and_labels_on_image_array(
      image_np,
      output_dict['detection_boxes'],
      output_dict['detection_classes'],
      output_dict['detection_scores'],
      category_index,
      instance_masks=output_dict.get('detection_masks'),
      use_normalized_coordinates=True,
      line_thickness=2)
    plt.figure(figsize=IMAGE_SIZE)
    plt.imshow(image_np)
    plt.show()
