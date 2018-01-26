# Automating-YOLOv2-training

A script that automates the tedious task of training YOLOv2. This works on linux systems


## Overview

This is a script that automates the tedious task of training YOLOv2. This works on linux systems. YOLO (you only look once) is a fast object detection system. The script is intended to reduce the amount of time spent training the YOLO system. This repository comes with the main.py file and the automation.py file. 
The automation.py script supports one class currently.
The main.py file runs indepedently and can convert .png images on linux systems to .jpg for labeling. The automation.py script will also convert .png files.


## Running the file automation.py

1) Make sure you have BBox Label Tool Multi class and Darknet. The script will not work without the BBox Label Tools folders
```
    https://github.com/jxgu1016/BBox-Label-Tool-Multi-Class
    https://github.com/pjreddie/darknet/wiki/YOLO:-Real-Time-Object-Detection
```

2) Clone or download main.py and automation.py. Place main.py and automation.py into the BBox Label Tool folder.

3) Open a new Shell. GO to BBOX LABEL directory. Type " Python automation.py " without the quotations. Make sure to use the python version that works on your system

4) The python script will inquiry the user:
  
```
  Enter unique folder name where labeled images are stored >>>
        (write the name of the folder with your images)
       
  Are images labeled?  y/n >>> 
        (did you use BBox to box the objects of interest? Write yes or no. You can write y or n also)
        
  Enter the folder name where the txt files are stored in Labels folder (example: 001 or 002) >>>
        (BBox Label Tool will place the .txt files in a folder called Labels and another one called 001 or 002 or etc. Write the  
        folder name. It starts with two zeroes usually and a number)

  Is darknet installed?  y/n >>>

  batch number? (64 recommended) >>>
        (write 64)
        
  subdivisions number? (8,6,or 4 recommended) >>>
        (write 8 or 6 or 4)
        
  Which path holds darknet executable file? paste here >>>
        (In the shell, copy path provided from above and paste into here. You may have several darknets)
        
        
```

(Mind the WARNING if one appears)

6) Move the backup folder from darknet with the weights file so that it saves your weights when training.

### Additional Details

You will find your images and files in the ALLrecentJpgTxt folder.

If everything is done right, paste this line into the shell to train:
```
./darknet detector train obj.data yolo-obj.cfg darknet19_448.conv.23
```

You can use ' -gpus0,1 ' if you have more than one gpu at your disposal:
```
./darknet detector train obj.data yolo-obj.cfg darknet19_448.conv.23 -gpus0,1 
```
### Notes

* The script will only handle one file at a time, so if you have multiple folders with images the script will need to be ran multiple times. Every time it runs, the script will place all images into the ALLrecentJpgTxt folder.

* The script will only handle one file at a time. If there are multiple folders with labled .txt files in them (for example Labels/001/, Labels/002/ ... etc) the script will need to be ran multiple times. Every time it runs, the script will place all .txt files into the ALLrecentJpgTxt folder.

* Currently the script handles one class. This can be easily changed.

* Batch number is 64. Better performing GPUs can take on 128 and so on.

* Subdivisions number is standard 8. Decreasing it may cause a seg fault. The GPU may run out of memory. However 6 is a good number to use on better GPUs.

* Make sure each jpg file has a corresponding .txt file before training!
* (For now) Make sure you dont have multiple folders of BBox label tool multi class. Ensure that the image folder with your images has a unique name. Ensure that there is not another folder called "Labels".
