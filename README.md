# Automating-YOLOv2-training

A script that automates the tedious task of training YOLOv2. This works on linux systems


## Overview

This is a script that automates the tedious task of training YOLOv2. This works on linux systems. YOLO (you only look once) is a fast object detection system. The script is intended to reduce the amount of time spent training the YOLO system. This repository comes with the main.py file and the automation.py file. 
The automation.py script supports one class currently.
The main.py file runs indepedently and can convert .png images on linux systems to .jpg for labeling. 


## Running the file automation.py

1) Make sure you have BBox Label Tool mulit class and Darknet. The script will not work without the BBox Label Tools folders
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


You will find your images and files in the ALLrecentJpgTxt folder.

If everything is done right, past this line into the shell to train:

./darknet detector train obj.data yolo-obj.cfg darknet19_448.conv.23


You can use ' -gpus0,1 ' if you have more than one gpu at your disposal:

./darknet detector train obj.data yolo-obj.cfg darknet19_448.conv.23 -gpus0,1 

