#!/usr/bin/env python

import cv2 
  
# change with your source
# digits for cameras on your computer
# path for video in filesystem
# url for RTSP stream
# more details at https://docs.opencv.org/3.4/d8/dfe/classcv_1_1VideoCapture.html#a85b55cf6a4a50451367ba96b65218ba1
vid = cv2.VideoCapture("/home/markus/Videos/2023-04-07-MononElm01.mp4")
  
while(True): 
      
    # Capture video frame from source
    ret, frame = vid.read() 
    # better - check if reading was succesful  
    # Display resulting frames
    cv2.imshow('frame', frame) 
      
    # stop loop if q is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break
  
# be nice to your os and release all resources
vid.release() 
cv2.destroyAllWindows()