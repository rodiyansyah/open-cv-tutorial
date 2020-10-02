import cv2
import numpy as np

img = np.zeros((512,512,3), np.uint8)
img = cv2.rectangle(img, (50,10),(100,50), (0,0,255),)
cv2.imshow('kotak', img)
cv2.waitKey(0)
cv2.destroyAllWindows()