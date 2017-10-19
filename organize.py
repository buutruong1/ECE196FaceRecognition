import os 
import shutil

# list all name of files in this path 
#listIm = os.listdir('/home/pi/ece196FaceRecognition/yaleB_faces/00')

#print listIm[4]

#imgSize= len(listIm)

#seventyPer = imgSize*.7

#seventyPer = int(round(seventyPer))

#tenPer = int(round(imgSize*0.1))

#remainSize = imgSize - seventyPer - tenPer

#print('total images is {0}'.format(imgSize))
#print('Seventy percent of image file is {0}'.format(seventyPer))
#print('Ten percent of images is {0}'.format(tenPer)) 
#print('Twenty percent of images is {0}'.format(remainSize))

#shutil.copy('/home/pi/ece196FaceRecognition/hello.txt','/home/pi/ece196FaceRecognition/yaleB_faces')

# list out all the image folders
allFolder = sorted(os.listdir('/home/pi/ece196FaceRecognition/yaleB_faces'))

mainLo = '/home/pi/ece196FaceRecognition'

# starting at the yaleB folder
for x in range (0,18):

    # make the 18 folders
    if x < 10:
        folderName = '0' + str(x)
    else:
        folderName = str(x)

    os.mkdir('./data/Train/%s'%folderName)    
    os.mkdir('./data/Test/%s'%folderName)
    os.mkdir('./data/Val/%s'%folderName)

    # list out all the images in the given file
    imgList = os.listdir('/home/pi/ece196FaceRecognition/yaleB_faces/{0}'.format(folderName))
    imgLength = len(imgList)

    seventyPer = int(round(imgLength*0.7))

    tenPer = int(round(imgLength*0.1))

    twentyPer = imgLength - seventyPer - tenPer
    
    # copy images to the train folder
    for y in range (0, seventyPer):
        shutil.copy(mainLo + '/yaleB_faces/{0}/{1}'.format(folderName,imgList[y]), mainLo + '/data/Train/{0}'.format(folderName))

    # copy images to val folder
    for z in range (seventyPer, seventyPer+tenPer):
        shutil.copy(mainLo + '/yaleB_faces/{0}/{1}'.format(folderName,imgList[z]), mainLo + '/data/Val/{0}'.format(folderName))

    # copy images to test folder (20%)
    for i in range (seventyPer+tenPer, imgLength):
        shutil.copy('./yaleB_faces/{0}/{1}'.format(folderName,imgList[i]), './data/Test/{0}'.format(folderName))

