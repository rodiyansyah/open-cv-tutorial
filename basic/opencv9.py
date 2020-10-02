import cv2
import numpy as np

img = np.zeros((512,512,3), np.uint8)
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img, 'sandi', (10,300),font, 2,(255,0,0), 1, cv2.LINE_AA)
cv2.imshow('text',img)
cv2.waitKey(0)
cv2.destroyAllWindows()