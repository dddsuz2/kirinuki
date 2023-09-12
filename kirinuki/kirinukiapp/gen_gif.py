from itertools import count
import math
import os
import cv2
import glob
from PIL import Image
from moviepy.editor import VideoFileClip
from apng import APNG

def convert_movie_to_jpgs(path):
    video_capture = cv2.VideoCapture(path)
    still_reading, image = video_capture.read()
    print(video_capture.isOpened())
    frame_count = 0
    print(video_capture.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = math.ceil(video_capture.get(cv2.CAP_PROP_FPS))

    
    while frame_count < fps * 6:
        cv2.imwrite(f"kirinuki/kirinukiapp/output/frame_{frame_count:03d}.jpg", image)
        print(image.shape)
        still_reading, image = video_capture.read()
        frame_count += 1


def duration(file_path):
    if file_path:
        video = VideoFileClip(file_path)
        video_duration = math.floor(video.duration)
    return video_duration

def gen_apng():
    im = APNG()
    path = 'kirinuki/kirinukiapp/output/*.jpg'
    files = glob.glob(path)
    for file in files:
        im.append_file(file, delay=200)
    im.save("kirinuki/kirinukiapp/result/result.png")
    

    
