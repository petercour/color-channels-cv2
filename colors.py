import cv2
import numpy as np
 
img = cv2.imread("lena.png", cv2.IMREAD_UNCHANGED)
 
b, g, r = cv2.split(img)
 
cv2.imshow("B", b)
cv2.imshow("G", g)
cv2.imshow("R", r)
 
cv2.waitKey(0)
cv2.destroyAllWindows()
