import cv2 as cv
import numpy as np
import sys
import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import os

 
# to open image to check if OpenCV package is working, can be deleted if the code is working
def openimage(image):
    img = cv.imread(image,-1);
    cv.namedWindow('image', cv.WINDOW_NORMAL);
    cv.imshow('image',img);
    cv.waitKey(0)
    cv.destroyAllWindows()

# calculates the center of a square/rectangle and returns the center coordinate
def center(x1,y1,x2,y2):
    x = x1+(x2/2)
    y = y1+(y2/2)
    c = [x,y]
    return c

# Set the tracker type.
# First frame of the video will be displayed pick an ROI
def openvideo():
    #tracker_types = ['BOOSTING', 'MIL','KCF', 'TLD', 'MEDIANFLOW', 'GOTURN', 'MOSSE', 'CSRT']
    capture = cv.VideoCapture(0)
    tracker= cv.TrackerKCF_create()
    ret,frame = capture.read()
    frame = cv.flip(frame,1)
    cv.imshow('video',frame)
    #select roi
    cv.putText(frame,"Drag and select object - press enter",(20,30),cv.FONT_ITALIC,1,(255,255,255),lineType=cv.LINE_AA)
    r = cv.selectROI('video',frame, fromCenter = False)
    #takes the ceter of defined ROI
    initial = center(int(r[0]),int(r[1]),int(r[2]),int(r[3]))
      
    
    
    #start tracking
    track = tracker.init(frame, r)
    while(True):
         #start video
         track,frame = capture.read()
         frame = cv.flip(frame,1)
         key = cv.waitKey(1) &0xFF
         (track, r) = tracker.update(frame)
         if track:
            #Define new ROI once the oject is tracked and updates in each frame
            p1 = (int(r[0]),int(r[1]))
            p2 = (int((r[0])+(r[2])), int(r[1]+r[3]))
            cv.rectangle(frame,p1,p2,(255,0,0),2,1)
            #takes the center of the new tracked ROI
            final = center(int(r[0]),int(r[1]),int(r[2]),int(r[3]))
            #Calculates how much it drifted from center of initial ROI
            final = np.subtract(final, initial)
            #print (final)
            x=final[0];
            y=final[1];
            #Display video            
            cv.imshow('video',frame)
            # write the coordinate in a text file for live plotting
            filename=open("Final.txt","w");
            filename.write("%i %i"%(final[0],final[1]))
            filename.close()
            
            # To define a new ROI press 's'
            if key == ord('s'):
               openvideo()
            #To quit the tracking press 'ESC'
            if key == 27:
               break
           
    capture.release()
    cv.destroyAllWindows()

openvideo()
 


