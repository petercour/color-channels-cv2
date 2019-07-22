# -*- coding:utf-8 -*-
import cv2
import numpy as np

img = cv2.imread("lena.png", cv2.IMREAD_UNCHANGED)
face = np.ones((200, 150, 3))
cv2.imshow("Demo", img)
face = img[200:400, 200:350]
cv2.imshow("face", face)
cv2.waitKey(0)
cv2.destroyAllWindows()

