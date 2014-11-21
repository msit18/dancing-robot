# -*- coding: utf-8 -*-
"""
Code from CompRobo
Adela Wee and Michelle Sit"""

import scipy
import numpy
import cv2
from train_smile import train_smiles
import sys
import pdb
from datetime import datetime
from sklearn.externals import joblib
import serial

"""
>>> joblib.dump(clf, 'my_model.pkl', compress=9)
And then later, on the prediction server:

>>> model_clone = 
"""

ser = serial.Serial('/dev/ttyACM0', 9600)

#Create xml classifiers
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
mouthCascade = cv2.CascadeClassifier('Mouth.xml')
# smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')

def detectFaces():

    #reads in the images from the camera
    video_capture = cv2.VideoCapture(0)

    while True:
        # Capture frame-by-frame
        ret, frame = video_capture.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=10,
            minSize=(30, 30)
        )
        
        if len(faces) == 0:
            print "There are no faces."
            ser.write('11')
            
        else:
            facedetectTime = datetime.now()
            #print "face detected time: %s" %facedetectTime
            # Draw a rectangle around the faces
            for (x,y,w,h) in faces:
                print "I see %s people" %len(faces)
                #center of shape, rectangle dimensions, color, line thickness
                #cv2.rectangle (img, vertex1, vertex across from 1, color, something)
                faceRect = cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),0)
                roi_gray = gray[6*(y/5):y+h,x+20:x+w-20]
                # roi_gray = gray[y+40:y+h-10,x+20:x+w-20]
                
                #resize roi_gray to (24, 24)
                if len(roi_gray) == 0:
                    pass
                else:
                    resized_roi = cv2.resize(roi_gray, (24, 24)).T/255.0
                    # scipy.misc.imsave('outfile.jpg', resized_roi)
                    roi_vec = resized_roi.reshape((resized_roi.shape[0]*resized_roi.shape[1],1))
                    smile_prob = -model.predict_log_proba(roi_vec.T)[0][0]
                    print "Smile probability: %s" %smile_prob
    
                    #the following still needs to be adjusted
                    if (smile_prob < 0.75):
                        print "NO SMILE DETECTED"
                        ser.write('22')
    
                    elif (smile_prob >= 0.75):
                        print "SMILE DETECTED"
                        ser.write('33')
                        
                        for (x, y, w, h) in faces:
                            roi_gray = gray[y:y+h, x:x+w]
                            roi_color = frame[y:y+h, x:x+w]
                            
                            mouth = mouthCascade.detectMultiScale(
                                roi_gray,
                                scaleFactor=1.1,
                                minNeighbors=5,
                                minSize=(30, 30),
                                flags=cv2.cv.CV_HAAR_SCALE_IMAGE)
                            
                            yValues = []
                            
                            for (ex,ey,ew,eh) in mouth:
                                yValues.append(ey)
                                
                            for (ex,ey,ew,eh) in mouth:
                                if ey == max(yValues):
                                    mvals = (ex, ey, ew, eh)
                                    cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

                    # import pdb
                    # pdb.set_trace()
            cv2.imshow("ROI", roi_gray)
            cv2.imshow('ROI_resized', resized_roi)

                # Display the resulting frame
            
        cv2.imshow('Video', frame)

        # cv2.imshow('ROI', roi_gray)
    
        if cv2.waitKey(1) & 0xFF == ord('q'):
            ser.close()
            break
        
        # import pdb
        # pdb.set_trace()

    # When everything is done, release the capture
    ser.close()
    video_capture.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    model = joblib.load('my_model.pkl')
    detectFaces()
    ser.close()
