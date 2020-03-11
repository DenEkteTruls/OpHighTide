import os
import sys
import cv2
import socket
import threading
import numpy as np

import general

camera = cv2.VideoCapture(int(sys.argv[1]))

while True:
  
  frame = camera.read()[1]
  
  cv2.imshow("mainframe", frame)
  
  if general.checkQuit():
    break
    
camera.release()
cv2.destroyAllWindows()
