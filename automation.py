

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
from os import walk, getcwd
import os
import sys
import platform
from subprocess import call
import subprocess
import glob
from PIL import Image

def find(path):
    for dirname in sys.path:
        candidate = os.path.join(dirname, '')
        return candidate

def subprocess_cmd(command):
    procedure = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    processq = procedure.communicate()[0].strip()
    print processq

def replace_line(file_name, line_num, text):
    lines = open(file_name, 'r').readlines()
    lines[line_num] = text
    f_out = open(file_name, 'w')
    f_out.writelines(lines)
    f_out.close()

def seeking(nme):
    for roo, din, fil in os.walk("/"):
        for files in fil:
            if files == nme:
                print os.path.join(roo, "")
                return os.path.join(roo, "")

def searching(nmee):
    for rin, din, fin in os.walk("/"):
        for files in fin:
            if files == nmee:
                print os.path.join(rin, "")

def dir_search(nmq):
    for roo, din, _ in os.walk("/"):
        for dirr in din:
            if dirr == nmq and dirr is not None:
				print os.path.join(roo, dirr)
				default = os.path.join(roo, "")
    return default

#print os.path.join(r, dirr)
##-------------------------------convert txt files---------------------
def conversion():
    print "\n converting txt files to yolo format \n"

    classes = ["wave"]

    def convert(size, box):
        dww = 1./size[0]
        dhh = 1./size[1]
        xxx = (box[0] + box[1])/2.0
        yyy = (box[2] + box[3])/2.0
        wwa = box[1] - box[0]
        hhh = box[3] - box[2]
        xxx = xxx*dww
        wwa = wwa*dww
        yyy = yyy*dhh
        hhh = hhh*dhh
        return (xxx, yyy, wwa, hhh)

    ##___________________________________________


    lpath = dir_search("Labels")

    dir_labels = "".join([lpath, "Labels"])
    print dir_labels + " \n the path to Labels folder is above \n"
    #raw_input("\n press enter ")

    # Configure directories
    folderr = raw_input('Enter the folder name where the txt files are stored'
                        ' in Labels folder (example: 001 or 002) >>> ')

    mypath = "%s/%s/" % (dir_labels, str(folderr))
    ##mypath = "/home/user/src/HowToTrainYoloExample/BBox-Label-Tool-Multi-Class/Labels/%s/" % str(folderr)
    ##outpath = "/home/user/src/HowToTrainYoloExample/BBox-Label-Tool-Multi-Class/Labels/converted/"
    outpath = "%s/converted/" % dir_labels
    print mypath + '\n'

    #The class. cls = "wave"
    if cls not in classes:
        exit(0)
    identity1 = classes.index(cls)

    pathname = getcwd()
    #list_file = open('%s/%s_list.txt'%(pathname, cls), 'w')

    # Retreive input text file list
    txt_name_list = []
    for (_, _, filenames) in walk(mypath):
        txt_name_list.extend(filenames)
        break
    print txt_name_list

    # Go through list
    for txt_name in txt_name_list:

        #Open files
        txt_dir = mypath + txt_name
        txt_file = open(txt_dir, 'r')
        f_lines = txt_file.read().split('\r\n')
        #for ubuntu put in "\r\n" rather than "\n"

        # Open files
        txt_outpath = outpath + txt_name
        print "Output:" + txt_outpath
        txt_outfile = open(txt_outpath, "w")

        # translate data to YOLO format
        cou = 1
        cnt = 0
        for datai in f_lines:

            if len(datai) >= 2:
                cnt = cnt + 1

                feature = datai.replace('\n', ' ').split(' ')
                const = int(feature[0])
                for _ in range(0, const):
                    valu = (cou*5)-5

                    xmin = feature[(1+valu)]
                    xmax = feature[(3+valu)]
                    ymin = feature[(2+valu)]
                    ymax = feature[(4+valu)]

                    photo_path = str('%s/ALLrecentJpgTxt/%s.jpg'%(pathname, os.path.splitext(txt_name)[0]))
                    pic = Image.open(photo_path)
                    wid = int(pic.size[0])
                    hght = int(pic.size[1])

                    bbb = (float(xmin), float(xmax), float(ymin), float(ymax))
                    bag33 = convert((wid, hght), bbb)

                    txt_outfile.write(str(identity1) + " " + " ".join([str(a) for a in bag33]) + '\n')
                    cou = cou+1

        # Saving images as bag33 in list

##------------------------------test and train set----------------------

def test_train():

    # Current Directory
    directory_current = "".join([os.path.dirname(os.path.abspath("ALLrecentJpgTxt")), "/ALLrecentJpgTxt"])

    # The path where the data will be at, with respect to 'darknet.exe'
    data_of_path = 'ALLrecentJpgTxt/'

    # Create train.txt and test.txt files
    train_files = open('train.txt', 'w')
    test_files = open('test.txt', 'w')

    # Percentage of total images utilized for the test set
    #(between 10-20 recommended)(f_import/pathlib)
    test_percent = 11

    # Fill in train.txt and test.txt
    counting = 1
    test_numb = round(100 / test_percent)
    for path_filename in glob.iglob(os.path.join(directory_current, "*.jpg")):
        title, _ = os.path.splitext(os.path.basename(path_filename))
        if counting == test_numb:
            counting = 1
            test_files.write(data_of_path + title + '.jpg' + "\n")
        else:
            train_files.write(data_of_path + title + '.jpg' + "\n")
            counting = counting + 1

if __name__ == "__main__":

    OS = platform.system()

    if OS != 'Linux':
        quit()

    print " OS System verified"
    P = raw_input('\n Enter unique folder name where labeled images are stored >>> ')
    print '...'

    #print dir_search(P)
    #print find(P)


    print ' The path to your file is \n'
    PATHN = dir_search(P)
    print PATHN 

    print "\n Path to BBOX Label Tool \n"
    PATHB = dir_search("BBox-Label-Tool-Multi-Class")
    PATH2B = os.path.join(PATHB, "BBox-Label-Tool-Multi-Class/")
    print PATH2B

    VAL1 = raw_input('\n Are images labeled?  y/n >>> ')
    if VAL1.lower() == 'n' or  VAL1.lower() == 'no':
        call(["python", "main.py"])
        quit()

    print ' Make sure all images are labeled \n'
    print ("\n convert png images to jpg "
           "\n Please have (image labeled) txt files\n")
    raw_input('\n press enter \n')
    print "%s%s/"  % (PATHN, P)
    
    subprocess_cmd('mkdir Newimages')
    subprocess_cmd('  cp  %s%s/* %sNewimages ' % (PATHN, P, PATH2B))
    print " Please wait... \n"

    subprocess_cmd(' cd Newimages; mkdir Converted_img ')
    subprocess_cmd(' cd Newimages; for i in *.png; do convert "$i" "Converted_img/${i%.*}.jpg"; done')
    subprocess_cmd(' cd Newimages ; for x in *.JPG; do mv "$x" "${x%.JPG}.jpg"; done  ')
    subprocess_cmd(' cd Newimages ; for x in *.JPEG; do mv "$x" "${x%.JPEG}.jpg"; done  ')
    subprocess_cmd('mkdir ALLrecentJpgTxt; cp -r %sNewimages/Converted_img/* %sALLrecentJpgTxt; cp -r %sNewimages/*.jpg %sALLrecentJpgTxt ' % (PATH2B, PATH2B, PATH2B, PATH2B))
    subprocess_cmd(' rm -r Newimages;')
    subprocess_cmd('cd Labels ; mkdir converted;  ')

    #class, predefined
    CLAS = "wave"
    cls = CLAS

    ##converting
    conversion()
    subprocess_cmd(' cp -r %sLabels/converted/* %sALLrecentJpgTxt ; rm -r converted ' % (PATH2B, PATH2B))

    NEW = raw_input('\n Is darknet installed?  y/n >>> ')
    if NEW.lower() == 'n' or NEW.lower() == 'no':
        quit()

    BATCH = raw_input("\n batch number? (64 recommended) >>> ")
    SUBDIV = raw_input("\n subdivisions number? (8,6,or 4 recommended) >>> ")
    print "... "

    #test and train
    test_train()

    ##----create files used for training----

    # train files are
    F = open("obj.data", "w+")
    F.write("classes= 1 \ntrain  = train.txt "
            "\nvalid  = test.txt \nnames = obj.names \nbackup = backup/ ")
    F.close()

    # classes
    F = open("obj.names", "w+")
    F.write("%s " % cls)
    F.close()

    # find voc file
    TRAIN_PATH = seeking("yolo-voc.cfg")

    # move files
    subprocess_cmd(' cp -r %s/yolo-voc.cfg .' % TRAIN_PATH)
    subprocess_cmd(' mv  yolo-voc.cfg yolo-obj.cfg')

    # parameters for training
    print "Setting parameters for training\n"

    # replace numbers in file
    replace_line('yolo-obj.cfg', 2, 'batch=%i\n' % int(BATCH))
    replace_line('yolo-obj.cfg', 3, 'subdivisions=%i\n' % int(SUBDIV))
    replace_line('yolo-obj.cfg', 243, 'classes=1\n')
    replace_line('yolo-obj.cfg', 236, 'filters=30\n')

    ##----- move files and start training ------
    searching("darknet19_448.conv.23")
    PDARK = raw_input(" Which path holds darknet executable file? paste here >>> ")

    print "\nmoving files\n"

    subprocess_cmd(' cp -r %sdarknet .' % PDARK)
    subprocess_cmd(' cp -r %sdarknet19_448.conv.23 .' % PDARK)

    print ' number of files: '
    DIR = "".join([os.path.dirname(os.path.abspath("ALLrecentJpgTxt")), "/ALLrecentJpgTxt"])
    F_NUMB = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
    print F_NUMB

    if (F_NUMB%2) != 0:
        print('WARNING!\n odd number of files in folder '
              'ALLrecentJpgTxt\n Please make sure each image file has a txt file\n')

    print '\n done...'
    print '\ncheck for weights file  when done training (usually a .backup)\n'
    print "Run this command to start training: \n"
    print '>>>  ./darknet detector train obj.data yolo-obj.cfg darknet19_448.conv.23  '
    print '\nQuit'
    quit()

##end


## instruction set taken from https://timebutt.github.io/static/author/nils/
