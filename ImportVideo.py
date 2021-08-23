import cv2
import matplotlib.pyplot as plt
import numpy as np
%matplotlib inline
vc=cv2.VideoCapture("\demo.mp4")

while open:
    ret,frame=vc.read()
    if frame is None:
        break
    if ret == True:
        #gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow('result',frame)
        if cv2.waitKey(1) & 0xFF==27:
            break
vc.release()
cv2.destroyAllWindows()
