import cv2
import numpy as np

'''cv2.Cann(image, threshold1, theshold2[, edges[,apertureSize[,L2gradient]]])
必要参数：
第一个参数是需要处理的原图像，该图像必须唯单通道的灰度图；
第二个参数是滞后阈值1；
第三个参数是之后阈值2
'''

img = cv2.imread("lenna.png", 1)
gray =cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("canny", cv2.Canny(gray, 250, 300))
cv2.waitKey()
cv2.destroyAllWindows()
