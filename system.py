import os
import sys
from cv2 import cv2
import socket
import threading
import numpy as np
import geopy

geo = geopy.geocoders.Nominatim(user_agent="OpHighTide")
location = geo.geocode("ocean, norway, vestfold")

def getDepth() -> int:

	# This function will return the depth underneath the keel.
	return 10


def getSpeed() -> int:

	# This function will return the GPS-calculated speed
	return 5


def getGpsCoordinates() -> int:

	# This function will return the GPS coordinates

	try:
		return (location.latitude, location.longitude)
	except:
		return (0,0)