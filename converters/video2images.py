import cv2
import sys
from math import floor


if len(sys.argv) != 2:
    print(
        "Call this program like this:\n"
        "    python video2images.py ../samples/Ballmer_DavidRubensteinshow_KopLe5NZBJc.mkv")
    exit()

video_path = sys.argv[1]

video_capture = cv2.VideoCapture(video_path)

fps = video_capture.get(cv2.CAP_PROP_FPS)
print('FPS: {}'.format(fps))

i = 0
capture_second = 0
while True:
    ret, frame = video_capture.read()
    if not ret:
        break

    second = floor(i / fps)
    if second == capture_second:
        print('Capturing {} second'.format(second))
        cv2.imwrite('frames/frame_{}s.png'.format(second), frame)
        capture_second += 1
    i += 1


