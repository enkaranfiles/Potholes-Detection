from darkflow.net.build import TFNet
import numpy as np
import time
import cv2
import matplotlib.pyplot as plt


options = {
    'model': 'cfg/tiny-yolo-voc-custom.cfg',
    'load': 2000,                             
    'threshold': 0.1,                       # this number can be higher if the performance is better
    'gpu': 1.0                               
}

tfnet = TFNet(options)
capture = cv2.VideoCapture('pothole.mkv')
colors = [tuple(255 * np.random.rand(3)) for i in range(10)]

while (capture.isOpened()):
    ret, frame = capture.read()# ret is a boolean. True when the video is playing.
    print "ret",ret
    if ret:
        print "frame",frame
        results = tfnet.return_predict(frame)
        print "result",results
        for color, result in zip(colors, results):
            tl = (result['topleft']['x'], result['topleft']['y'])
            br = (result['bottomright']['x'], result['bottomright']['y'])
            label = result['label']
            frame = cv2.rectangle(frame, tl, br, color, 7)
            frame = cv2.putText(frame, label, tl, cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)
            print "frame",frame
        cv2.imshow('frame', frame)
      