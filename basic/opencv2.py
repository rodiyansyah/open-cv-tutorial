import cv2

img = cv2.imread('kucing.png')
cv2.imshow('kucing', img)
k = cv2.waitKey(0)
if k ==27:
    cv2.destroyAllWindows()
elif k==ord('s'):
    cv2.imwrite('save_kucing.png', img)
    cv2.destroyAllWindows()