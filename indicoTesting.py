# -*- coding: utf-8 -*-
"""
Created on Tue Nov 04 11:41:21 2014

@author: jmorris
"""

import numpy as np
from indicoio import *
import cv2
import sys
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image



test_face = np.linspace(0,50,48*48).reshape(48,48).tolist()
#print fer(test_face)
video_capture = cv2.VideoCapture(0)
i=0

img0 = mpimg.imread('C:\Users\jmorris\Documents\GitHub\dancing-robot\julianSmile.jpg')
img1 = mpimg.imread('C:\Users\jmorris\Documents\GitHub\dancing-robot\julianNeutral.jpg')
img2 = mpimg.imread('C:\Users\jmorris\Documents\GitHub\dancing-robot\julianAngry2.jpg')


def rgb2gray(rgb):

    r, g, b = rgb[:,:,0], rgb[:,:,1], rgb[:,:,2]
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b

    return gray


a1 = rgb2gray(img0)
a2 = rgb2gray(img1)
a3 = rgb2gray(img2)
rgb2gray(img0).resize((100,100))
rgb2gray(img1).resize((100,100))
rgb2gray(img2).resize((100,100))


#img = mpimg.imread("C:\Users\jmorris\Documents\GitHub\dancing-robot\webcam\julianSmile.png")
#print fer(a1.tolist())
#print fer(a2.tolist())
#print fer(a3.tolist())
#print fer(test_face)




"""
while True:
    # Capture frame-by-frame
    
    i+=1
    ret, frame = video_capture.read()

    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if i%10 == 0:
        print fer(frame.tolist())
        #print fer(gray.tolist())

    cv2.imshow('Video', frame)
    

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
"""
# When everything is done, release the capture
"""
video_capture.release()
cv2.destroyAllWindows()
"""










