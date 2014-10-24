# -*- coding: utf-8 -*-
"""
Created on Sun Oct 19 20:49:44 2014

@author: jmorris
"""


import cv2
import sys


#python webcam.py haarcascade_frontalface_default.xml
#runfile('C:/Users/jmorris/Documents/GitHub/Webcam-Face-Detect/webcam.py', 'haarcascade_frontalface_default.xml')

cascPath = sys.argv[1]
faceCascade = cv2.CascadeClassifier(cascPath)

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
        
        

    # Display the resulting frame
    cv2.imshow('Video', frame)
    

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture

video_capture.release()
cv2.destroyAllWindows()







