import os
import sys
from cv2 import cv2
import socket
import threading
import numpy as np

def checkQuit() -> bool:

    # This function wil return a bool depending on
    # if the quitkey (ESC) is clicked.
    if cv2.waitKey(20) & 0xFF == 27:
        return True
    else:
        return False


def setData(frame, speed, depth, gpsCoordinates):

    # This function will display some data to the display
    gps_text = "Latitude: {}, Longtitude {}".format(gpsCoordinates[0], gpsCoordinates[1])

    cv2.putText(frame, "Speed: {}".format(str(speed)), (20, 40), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 255), 2, cv2.LINE_AA)
    cv2.putText(frame, "Depth: {}".format(str(depth)), (20, 80), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 255), 2, cv2.LINE_AA)
    cv2.putText(frame, gps_text, (190, 460), cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.7, (0, 200, 255), 1, cv2.LINE_AA)