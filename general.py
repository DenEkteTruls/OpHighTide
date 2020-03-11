import os
import sys
import cv2
import socket
impor threading
import numpy as np

def checkQuit():
  
  if cv2.waitKey(20) & 0xFF == 27:
    return True
  else:
    return False
