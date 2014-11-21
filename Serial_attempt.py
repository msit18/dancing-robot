# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
C:\Users\jmorris\.spyder2\.temp.py

Needs to be run in conjunction with the arduino code (arduino.py)
"""


import serial
import time
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=0)
i = 0
while i<10:
 try:
  ser.write('90')
  print ser.readall()
  
  time.sleep(1)
  i+=1
 except ser.SerialTimeoutException:
  print('Data could not be read')
  time.sleep(1)
  ser.close()

ser.close()


    
    
    
    
