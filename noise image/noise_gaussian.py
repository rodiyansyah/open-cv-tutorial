import cv2
from matplotlib import pyplot as plt

img = cv2.imread('data.png')

blur = cv2.GaussianBlur(img,(11,11),0)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
plt.xticks([]), plt.yticks([])
plt.show()