

"""
 Name:        automation.py
 Purpose:     Automating yolo image training on linux
 Author:      Andrew Kubal
 Created:     01/04/2018

NOTES:
py script for automating yolo train and test.
Drop this .py script next to folder with images, usually in the BBox Label folder.
Include the main.py file at the same directory as this file.

"""



##import lib
import os 
import sys
import commands
import subprocess
from os import walk, getcwd
from PIL import Image
from subprocess import call
import glob
from time import sleep
import platform


def find(path, matchFunc=os.path.isfile):
    for dirname in sys.path:
        candidate = os.path.join(dirname, '')
        return candidate


def subprocess_cmd(command):
    procedure = subprocess.Popen(command,stdout=subprocess.PIPE, shell=True)
    process = procedure.communicate()[0].strip()
    print process
    
def replace_line(file_name, line_num, text):
    lines = open(file_name, 'r').readlines()
    lines[line_num] = text
    f_out = open(file_name, 'w')
    f_out.writelines(lines)
    f_out.close()

def seeking(nm):
	for r,d,f in os.walk("/"):
			for files in f:
				if files == nm:
					  print os.path.join(r,"")
					  return os.path.join(r,"")

def searching(NM):
	for r,d,f in os.walk("/"):
		for files in f:
			 if files == NM:
				  print os.path.join(r,"")
				  



##-------------------------------convert txt files---------------------
def conversion():
	print("\n converting txt files to yolo format \n")

	classes = ["wave"]

	def convert(size, box):
		dw = 1./size[0]
		dh = 1./size[1]
		x = (box[0] + box[1])/2.0
		y = (box[2] + box[3])/2.0
		w = box[1] - box[0]
		h = box[3] - box[2]
		x = x*dw
		w = w*dw
		y = y*dh
		h = h*dh
		return (x,y,w,h)
		
		
	##___________________________________________

	# Configure directories  
	folderLabels = raw_input('Enter the folder name where the txt files are stored in Labels folder (example: 001 or 002) >>> ')

	mypath = "/home/akubal/src/HowToTrainYoloExample/BBox-Label-Tool-Multi-Class/Labels/%s/" % str(folderLabels)
	outpath = "/home/akubal/src/HowToTrainYoloExample/BBox-Label-Tool-Multi-Class/Labels/converted/"
	print(mypath + '\n')


	#The class. cls = "wave"
	if cls not in classes:
		exit(0)
	identity1 = classes.index(cls)

	DD = getcwd()
	list_file = open('%s/%s_list.txt'%(DD, cls), 'w')

	# Retreive input text file list
	txt_name_list = []
	for (dirpath, dirnames, filenames) in walk(mypath):
		txt_name_list.extend(filenames)
		break
	print(txt_name_list)

	# Go through list 
	for txt_name in txt_name_list:
		
		
		#Open files
		txt_dir = mypath + txt_name
		txt_file = open(txt_dir, 'r')
		f_lines = txt_file.read().split('\r\n')   
		#for ubuntu put in "\r\n" rather than "\n"
		
		# Open files 
		txt_outpath = outpath + txt_name
		print("Output:" + txt_outpath)
		txt_outfile = open(txt_outpath, "w")
		
		
		# translate data to YOLO format 
		C=1
		cnt = 0
		for dataOne in f_lines:
			
			if(len(dataOne) >= 2):
				cnt = cnt + 1
				
				feature = dataOne.replace('\n', ' ').split(' ')
				const=int(feature[0])
				for z in range(0,const):
					Val=(C*5)-5
					
					xmin = feature[(1+Val)]
					xmax = feature[(3+Val)]
					ymin = feature[(2+Val)]
					ymax = feature[(4+Val)]

					photo_path = str('%s/ALLrecentJpgTxt/%s.jpg'%(DD, os.path.splitext(txt_name)[0]) )
					im=Image.open(photo_path)
					w= int(im.size[0])
					h= int(im.size[1])
					
					b = (float(xmin), float(xmax), float(ymin), float(ymax))
					bag33 = convert((w,h), b)
					
					txt_outfile.write(str(identity1) + " " + " ".join([str(a) for a in bag33]) + '\n')
					C=C+1
					
		# Saving images as bag33 in list
		
##------------------------------test and train set----------------------

def test_train():
	
	
	dirr="".join([os.path.dirname(os.path.abspath("ALLrecentJpgTxt")),"/ALLrecentJpgTxt" ])

	# Current Directory
	directory_current = "".join([os.path.dirname(os.path.abspath("ALLrecentJpgTxt")),"/ALLrecentJpgTxt" ])


	# The path where the data will be at, with respect to 'darknet.exe'
	data_of_path = 'ALLrecentJpgTxt/'

	# Create train.txt and test.txt files
	train_files = open('train.txt', 'w')
	test_files = open('test.txt', 'w')
	
	# Percentage of total images utilized for the test set (between 10-20 recommended)(f_import/pathlib)
	test_percent = 11;

	# Fill in train.txt and test.txt
	counting = 1  
	test_numb = round(100 / test_percent)  
	for pathAndFilename in glob.iglob(os.path.join(directory_current, "*.jpg")): 
		title, ext = os.path.splitext(os.path.basename(pathAndFilename))
		if (counting == test_numb):
			counting = 1
			test_files.write(data_of_path + title + '.jpg' + "\n")
		else:
			train_files.write(data_of_path + title + '.jpg' + "\n")
			counting = counting + 1
        
      



if __name__ == "__main__":


	OS = platform.system()
	
	if OS != 'Linux':
		quit()
	
	print(" OS System verified" )

	path1 = raw_input('\n Enter unique folder name where labeled images are stored >>> ')
	print('...')
	
	searching(path1)
	pathn = find(path1)
	
	print(' The path to your file is \n')
	print(find(path1))
	
	value2=raw_input('\n Are images labeled?  y/n >>> ')
	if (value2.lower()=='n' or  value2.lower()=='no'):
		call(["python", "main.py"])
		quit()

	print(' Make sure all images are labeled \n')
	print("\n convert png images to jpg \n Please have (image labeled) txt files in image_and_txt folder\n")
	raw_input('\n press enter \n')
	
	subprocess_cmd(' mkdir Newimages; cp -r %s/%s/* %s/Newimages ' % (pathn,path1,pathn) )
	print(" Please wait... \n")

	subprocess_cmd( ' cd Newimages; mkdir Converted_img; for i in *.png; do convert "$i" "Converted_img/${i%.*}.jpg"; done '  )
	subprocess_cmd(' cd Newimages ; for x in *.JPG; do mv "$x" "${x%.JPG}.jpg"; done  ' )
	subprocess_cmd(' cd Newimages ; for x in *.JPEG; do mv "$x" "${x%.JPEG}.jpg"; done  ' )
	subprocess_cmd('mkdir ALLrecentJpgTxt; cp -r %s/Newimages/Converted_img/* %s/ALLrecentJpgTxt; cp -r %s/Newimages/*.jpg %s/ALLrecentJpgTxt '  % (pathn,pathn,pathn,pathn) )
	subprocess_cmd(' rm -r Newimages;')
	subprocess_cmd('cd Labels ; mkdir converted;  '   )

	#class, predefined
	classOne = "wave"
	cls = classOne
	
	##converting
	conversion()
	subprocess_cmd(' cp -r %s/Labels/converted/* %s/ALLrecentJpgTxt ; rm -r converted ' % (pathn,pathn))

	value3=raw_input('\n Is darknet installed?  y/n >>> ')
	if (value3.lower()=='n' or value3.lower()=='no'):
		quit()
	
	batch =raw_input("\n batch number? (64 recommended) >>> ")
	subdiv=raw_input("\n subdivisions number? (8,6,or 4 recommended) >>> ")
	print("... ")

	
	#test and train 
	test_train() 


	##----create files used for training----

	# train files are
	f = open("obj.data", "w+")
	f.write("classes= 1 \ntrain  = train.txt \nvalid  = test.txt \nnames = obj.names \nbackup = backup/ ")
	f.close()

	# classes
	f = open("obj.names", "w+")
	f.write("%s " % cls)
	f.close()

	# find voc file			
	trainingSpecsPath = seeking("yolo-voc.cfg")		
		 
	# move files												
	subprocess_cmd(' cp -r %s/yolo-voc.cfg .' % trainingSpecsPath )				
	subprocess_cmd(' mv  yolo-voc.cfg yolo-obj.cfg')

	# parameters for training
	print("Setting parameters for training\n")


	# replace numbers in file
	replace_line('yolo-obj.cfg', 2, 'batch=%i\n' % int(batch))
	replace_line('yolo-obj.cfg', 3, 'subdivisions=%i\n' % int(subdiv))
	replace_line('yolo-obj.cfg', 243, 'classes=1\n')
	replace_line('yolo-obj.cfg', 236, 'filters=30\n')


	##----- move files and start training ------			  
	searching("darknet19_448.conv.23")
	pathDark= raw_input(" Which path holds darknet executable file? paste here >>> ")

	print("\nmoving files\n")

	subprocess_cmd(' cp -r %sdarknet .' % pathDark)
	subprocess_cmd(' cp -r %sdarknet19_448.conv.23 .' % pathDark)
	
	
	print(' number of files: ')
	DIR="".join([os.path.dirname(os.path.abspath("ALLrecentJpgTxt")),"/ALLrecentJpgTxt" ])
	numb_files = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
	print(numb_files)
	
	if ( (numb_files%2)!= 0 ):
		print('WARNING!\n odd number of files in folder ALLrecentJpgTxt\n Please make sure each image file has a txt file\n')
		
	
	print('\n done...')
	print('\ncheck for weights file  when done training (usually a .backup)\n')
	print("Run this command to start training: \n")
	print('>>>  ./darknet detector train obj.data yolo-obj.cfg darknet19_448.conv.23  ')	
	print('\nQuit')
	quit()

##end
