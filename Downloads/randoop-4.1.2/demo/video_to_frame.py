# -*- coding: utf-8 -*-
from moviepy.editor import VideoFileClip
import cv2

clip = VideoFileClip("a.mp4")
starting_point = 94  # start at second minute
end_point = 99  # record for 300 seconds (120+300)
subclip = clip.subclip(starting_point, end_point)
subclip.write_videofile("a.mp4")

vidcap = cv2.VideoCapture('a.mp4')

success,image = vidcap.read()
count = 0
while success:
  cv2.imwrite("frame%d.jpg" % count, image)     # save frame as JPEG file      
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1