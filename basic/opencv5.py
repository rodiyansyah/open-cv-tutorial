import cv2
font=cv2.FONT_HERSHEY_COMPLEX_SMALL
cap = cv2.VideoCapture('Traffic.mp4')
while(cap.isOpened()):
    ret, frame = cap.read()
    cv2.imshow('frame', frame)

    if cv2.waitKey(1)== ord('q'):
        break

cap.release()
cv2.destroyAllWindows()