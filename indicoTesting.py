# -*- coding: utf-8 -*-
"""
Created on Tue Nov 04 11:41:21 2014

@author: jmorris
"""

import numpy as np
from indicoio import *
import cv2
import sys


test_face = np.linspace(0,50,48*48).reshape(48,48).tolist()
#print fer(test_face)

video_capture = cv2.VideoCapture(0)
i=0
while True:
    # Capture frame-by-frame

    
    i+=1
    ret, frame = video_capture.read()

    if i%10 == 0:
        print fer(frame.tolist())

    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    


    cv2.imshow('Video', frame)
    

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture

video_capture.release()
cv2.destroyAllWindows()









