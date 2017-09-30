# coding=utf-8
import cv2
import sys
import os

# str_src_video_path = "sun16.mkv"
str_src_video_path = "test.avi"
str_dst_video_folder = "./"
i_frameToStart = 0
i_framToStop = 100

videoCapture = cv2.VideoCapture('sun16.mkv')
if not videoCapture.isOpened():
    print "video open fail!"
    sys.exit(-1)
fps = videoCapture.get(cv2.cv.CV_CAP_PROP_FPS)
print "video fps is {}".format(fps)


# get total frame number
totalFrameNumber = videoCapture.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT)
print "total video has {} frames.".format(totalFrameNumber)


videoCapture.set(cv2.cv.CV_CAP_PROP_POS_FRAMES, i_frameToStart)
print "read video from frame {}".format(i_frameToStart)

size = (int(videoCapture.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)),
        int(videoCapture.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)))

str_src_video_name_ext = os.path.basename(str_src_video_path)
str_src_video_name_noext = os.path.splitext(str_src_video_name_ext)[0]
str_src_video_ext = os.path.splitext(str_src_video_name_ext)[1].strip().lower()
str_dst_video_path = str_dst_video_folder + str_src_video_name_noext + ".avi"

videoWriter = cv2.VideoWriter(str_dst_video_path, cv2.cv.CV_FOURCC('M','P','E','G'), fps, size)


if i_framToStop == -1:
    i_framToStop = totalFrameNumber

assert i_framToStop >= i_frameToStart, "stop frame < start frame. i_frameToStart = {}, i_framToStop = {}".format(i_frameToStart, i_framToStop)
print "i_framToStop = {}".format(i_framToStop)


bStop = False

currentFrame = i_frameToStart

while not bStop:
    if currentFrame >= i_framToStop:
        bStop = True

    videoCapture.set(cv2.cv.CV_CAP_PROP_POS_FRAMES, currentFrame)
    success, frame = videoCapture.read()
    assert success, "read frame error. currentFrame = {}".format(currentFrame)
    print "read frame {}".format(currentFrame)

    videoWriter.write(frame)
    currentFrame += 1

print "video finish!"





