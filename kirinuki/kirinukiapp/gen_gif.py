from itertools import count
import math
import os
import cv2
from PIL import Image

def convert_movie_to_jpgs(path):
    video_capture = cv2.VideoCapture(path)
    still_reading, image = video_capture.read()
    frame_count = 0
    while still_reading:
        cv2.imwrite(f"output/frame_{frame_count:03d}.jpg", image)
        
        still_reading, image = video_capture.read()
        frame_count += 1