from itertools import count
import math
import os
import cv2
from PIL import Image

def convert_movie_to_jpgs(path):
    video_capture = cv2.VideoCapture(path)
    still_reading, image = video_capture.read()
    print(video_capture.isOpened())
    frame_count = 0
    print(video_capture.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = math.ceil(video_capture.get(cv2.CAP_PROP_FPS))

    
    while frame_count < fps * 6:
        cv2.imwrite(f"{os.getcwd()}/kirinukiapp/output/frame_{frame_count:03d}.jpg", image)
        a = Image.fromarray(image)
        a.save(f"{os.getcwd()}/kirinukiapp/output/frame_{frame_count:03d}.jpg")
        print(image.shape)
        still_reading, image = video_capture.read()
        frame_count += 1