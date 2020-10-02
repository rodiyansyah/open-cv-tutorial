import cv2
cap = cv2.VideoCapture(0)
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

print("W : ",width)
print("H : ",height)
print("X : ",width*height)

while(True):
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    fps = cap.get(cv2.CAP_PROP_FPS)
    print(("fps : ", fps))
    if cv2.waitKey(1)==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()