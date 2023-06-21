import cv2
import os

video = cv2.VideoCapture("Bruh1.webm")
fps = video.get(cv2.CAP_PROP_FPS)

start = int(input('Enter the start time: '))
dur = int(input('Enter the duration (Enter -1 for full): '))

path = 'D:/Face Recognition/New'
fps_skip = 25

init_fr = int(start*fps) + 1
nr_frames = video.get(cv2.CAP_PROP_FRAME_COUNT) - init_fr

scl = 1

if dur == -1:
    end_frame = int(nr_frames/fps_skip)
else:
    end_frame = int((dur*fps)/fps_skip)


for i in range(1, end_frame+2):
    video.set(1, init_fr)
    success, frame = video.read()
    resized = cv2.resize(frame, (int(frame.shape[1]/scl), int(frame.shape[0]/scl)))
    cv2.imwrite(os.path.join(path , 'Frame ' + str(i) + '.jpg'), resized)
    init_fr+=fps_skip

print(str(end_frame+1) + " Frames have been Extracted.")