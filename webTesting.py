# -*- coding: utf-8 -*-
"""
Created on Thu Nov 06 23:12:17 2014

@author: jmorris
"""

import cv2

HAAR_CASCADE_PATH = "haarcascade_smile.xml"

CAMERA_INDEX = 0

def detect_faces(image):
         faces = []
         detected = cv2.HaarDetectObjects(image, cascade, storage, 1.1,99,0,(40,40))
         if detected:
             for (x,y,w,h),n in detected:
                faces.append((x,y,w,h))
         return faces

if __name__ == "__main__":
        cv2.NamedWindow("Video", cv2.CV_WINDOW_AUTOSIZE)

        capture = cv2.cv.CaptureFromCAM(CAMERA_INDEX)
        storage = cv2.cv.CreateMemStorage()
        cascade = cv2.cv.Load(HAAR_CASCADE_PATH)

        faces = []

        i = 0
        c = -1
        while (c == -1):
             image = cv2.QueryFrame(capture)

             #Only run the Detection algorithm every 5 frames to improve performance
             if i%5==0:
                   faces = detect_faces(image)

             for (x,y,w,h) in faces:
                   cv2.Rectangle(image, (x,y), (x+w,y+h), 255)

             cv2.ShowImage("Video", image)   
             i += 1
             c = cv2.WaitKey(10)