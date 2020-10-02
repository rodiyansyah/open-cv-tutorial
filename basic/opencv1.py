import cv2

img = cv2.imread('kucing.png')
cv2.imshow('kucing', img)
cv2.imwrite('kucing_2.png', img)
cv2.waitKey(0)