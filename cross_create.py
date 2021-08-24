import cv2
import numpy as np
import matplotlib.pyplot as plt

colors={'red':(0,0,255)}
image = cv2.imread('/test.jpg')

cv2.line(image,(540,329),(540,279),colors['red'],2);
cv2.line(image,(515,304),(565,304),colors['red'],2); 
cv2.namedWindow("Cross",1); 
cv2.imshow("Cross",image);
cv2.waitKey(0);
cv2.destroyAllWindows()
cv2.imwrite('/test.jpg',image)
