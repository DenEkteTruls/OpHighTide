import os
import sys
from cv2 import cv2
import socket
import threading
import numpy as np

import general
import network
import system
import display

camera = cv2.VideoCapture(int(sys.argv[1]))

width = camera.get(3)
height = camera.get(4)

while True:

  
  frame = camera.read()[1]


  # Frame is resized to (1280, 720)
  cv2.resize(frame, (1280, 720))

  speed = system.getSpeed()
  depth = system.getDepth()
  gpsCoordinates = system.getGpsCoordinates()
  display.setData(frame, speed, depth, gpsCoordinates)

  cv2.imshow("mainframe", frame)
  if display.checkQuit():
    break
    
camera.release()
cv2.destroyAllWindows()
