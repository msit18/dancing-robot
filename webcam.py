# -*- coding: utf-8 -*-
"""
Created on Sun Oct 19 20:49:44 2014

@author: jmorris
"""

import cv2
import sys
import numpy as np
#from indicoio import *


#python webcam.py haarcascade_frontalface_default.xml
#runfile('C:/Users/jmorris/Documents/GitHub/dancing-robot/webcam.py', 'haarcascade_frontalface_default.xml')
#runfile('C:/Users/jmorris/Documents/GitHub/dancing-robot/webcam.py', 'haarcascade_smile.xml')

cascPath = sys.argv[1]
smilePath = 'haarcascade_smile.xml'
eyePath = 'haarcascade_eye.xml'
mouthPath = 'Mouth.xml'

faceCascade = cv2.CascadeClassifier(cascPath)
smileCascade = cv2.CascadeClassifier(smilePath)
eyeCascade = cv2.CascadeClassifier(eyePath)
mouthCascade = cv2.CascadeClassifier(mouthPath)

video_capture = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()
    

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.cv.CV_HAAR_SCALE_IMAGE
    )    

    # Draw a rectangle around the faces
    # stores distances from the center
    for (x, y, w, h) in faces:
        midPoint = (int(x+0.5*w),int(y+0.5*h))
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        distanceX = abs(midPoint[0]-240)
        distanceY = abs(midPoint[1]-320)
        distance = ((distanceX)**2+(distanceY)**2)**0.5
        
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        
        """
        eyes = eyeCascade.detectMultiScale(roi_gray)    
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
        """
        """
        mouth = mouthCascade.detectMultiScale(roi_gray)
        if len(mouth) > 3:
            (mx, my, mw, mh) = mouth[3]
            cv2.rectangle(roi_color, (mx,my), (mx+mw, my+mh), (0,255,0),2)
        """
        
        mouth = mouthCascade.detectMultiScale(roi_gray)
        yValues = []
        
        for (ex,ey,ew,eh) in mouth:
            yValues.append(ey)
            
        for (ex,ey,ew,eh) in mouth:
            if ey == max(yValues):
                #mvals = (ex, ey, ew, eh)
                cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
                
                roi_mouth_gray = roi_gray[ey:ey+eh,ex:ex+ew]
                roi_mouth_color = roi_color[ey:ey+eh,ex:ex+ew]
                
                smiles = smileCascade.detectMultiScale(roi_mouth_gray)
                for (sx,sy,sw,sh) in smiles:                    
                    cv2.rectangle(roi_mouth_color,(sx,sy),(sx+sw,sy+sh),(255,0,0),2)
        
        
        
    # Display the resulting frame
    cv2.imshow('Video', frame)
    

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture

video_capture.release()
cv2.destroyAllWindows()
