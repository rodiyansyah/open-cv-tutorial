import cv2
img = cv2.imread('img1.jpg')
res = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
cv2.imwrite('img1_resize.jpg', res)

cv2.imshow('res', res)
cv2.waitKey(0)
cv2.destroyAllWindows()