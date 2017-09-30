# coding=utf-8
import cv2
import sys


str_src_video_path = "E:\\tmp2_video\\1097090570.f4v"
videoCapture = cv2.VideoCapture(str_src_video_path)
if not videoCapture.isOpened():
    print "video open fail!"
    sys.exit(-1)
fps = videoCapture.get(cv2.cv.CV_CAP_PROP_FPS)
print "video fps is {}".format(fps)
totalFrameNumber = videoCapture.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT)
print "total video has {} frames.".format(totalFrameNumber)








