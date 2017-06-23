During the training and testing of my custom dataset with YOLOv2, I realised I had to write my own program to get the Mean average precision value. 
1. Change the code src/detector.c to replace voc.2007.test.txt(In the validate function) with custom txt file containing the path to test Images.
2. Use the ./darknet detector valid data/obj.data cfg/obj.cfg backup/weights (Change accordingly) command to get the predictions on the test Images
3. Use toXML.py(after appropriate changes, I tried my best to comment where ver necessary) to convert the ground truth YOLO format bounding box to the Annotations in the XML format.(Thank you Shiyang Lu)
4. Use map.py(I have combined the voc_eval.py and the pascal_voc.py files from https://github.com/rbgirshick into map.py) with the necessary changes to get the mAP value.

The code is not completely polished(I have my doubts as I got a 98% mAP). Any suggestions and/or changes are welcome.


ResNet configuration file for YOLOV2. Work in Progress.
