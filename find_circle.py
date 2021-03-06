import cv2 as cv
import numpy as np

def detect_circles_demo(image):
    dst = cv.pyrMeanShiftFiltering(image, 10, 89)   #边缘保留滤波EPF
    cimage = cv.cvtColor(dst, cv.COLOR_RGB2GRAY)
    circles = cv.HoughCircles(cimage, cv.HOUGH_GRADIENT, 1, 19, param1=106, param2=39, minRadius=0, maxRadius=250)
    circles = np.uint16(np.around(circles)) #把circles包含的圆心和半径的值变成整数
    for i in circles[0, : ]:
        cv.circle(image, (i[0], i[1]), i[2], (0, 0, 255), 2)  #画圆
        cv.circle(image, (i[0], i[1]), 2, (0, 0, 255), 2)  #画圆心
    cv.imshow("circles", image)

src = cv.imread("/test.jpg")
cv.namedWindow('input_image', cv.WINDOW_NORMAL) #设置为WINDOW_NORMAL可以任意缩放
cv.imshow('input_image', src)
detect_circles_demo(src)
cv.waitKey(0)
cv.destroyAllWindows()
