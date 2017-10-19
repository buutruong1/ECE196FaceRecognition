"""
ECE196 Face Recognition Project
Author: W Chen

Adapted from:
http://www.pyimagesearch.com/2015/03/30/accessing-the-raspberry-pi-camera-with-opencv-and-python/

Use this code as a template to process images in real time, using the same techniques as the last challenge.
You need to display a gray scale video with 320x240 dimensions, with box at the center
"""


# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import numpy as np

# define d for naming new Image
d = 300

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))

# allow the camera to warmup
time.sleep(0.1)

# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    # grab the raw NumPy array representing the image, then initialize the timestamp
    # and occupied/unoccupied text
    image = frame.array

    # convert RGB color to grayscale video
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    #print image.shape
    
    # resize the image
    image = cv2.resize(image,(750,750), interpolation = cv2.INTER_AREA)

    # size of the image
    sizeIm = image.shape

    # obtain edge to draw the white rectangle 
    # row1 = (sizeIm[0]/2)-50
    #col1 = (sizeIm[1]/2)-50
    
    #row2 = (sizeIm[0]/2)+50
    # col2 = (sizeIm[1]/2)+50

    # draw the white rectangle 
    #cv2.rectangle(image,(col1,row1),(col2,row2),(255,255,255),3)

    # start face cascade classifier
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
  
    # skill factor 
    faces = face_cascade.detectMultiScale(image, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(image,(x,y),(x+w,y+h),(255,255,255),2)
        
        newIm = image[y:y+h, x:x+w]
        
        # name new image iteratively
        filename = "/home/pi/ece196FaceRecognition/buuFace/buuFace_%d.jpg"%d

        cv2.imwrite(filename, newIm)
        
        d+=1

    # show the frame
    cv2.imshow("Frame", image)
    key = cv2.waitKey(1) & 0xFF

    # clear the stream in preparation for the next frame
    rawCapture.truncate(0)

    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break

    if d == 330:
        break
