import cv2
import numpy as np

img = np.zeros((512,512,3), np.uint8)
img = cv2.circle(img,(200,200),50,(0,0,100),1)
img = cv2.circle(img,(100,200),50,(0,0,100),1)
img = cv2.circle(img,(200,100),50,(0,0,100),1)
img = cv2.circle(img,(100,100),50,(0,0,100),1)


cv2.imshow('lingkaran', img)
cv2.waitKey(0)
cv2.destroyAllWindows()