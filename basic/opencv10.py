import cv2
import numpy as np

def draw_circle(event, x,y, flags, param):
    if event==cv2.EVENT_LBUTTONDBLCLK:
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, 'sandi', (x,y), font, 2, (255,0,0), 3)

img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)

while(1):
    cv2.imshow('image', img)
    if cv2.waitKey(20)==ord('q'):
        break
cv2.destroyAllWindows()