# import OpenCV
import cv2
# Import numpy
import numpy as np

# Membaca gambar
img = cv2.imread('line1.png')
# Ubah ke gray
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# deteksi tepi
edges = cv2.Canny(gray, 50, 150, apertureSize=3)
minLineLength = 100
maxLineGap = 10
# Fungsi deteksi arus
lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 100, minLineLength, maxLineGap)
# Mencari semua garis
for x1, y1, x2, y2 in lines[0]:
    cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

# Simpan gambar
cv2.imwrite('houghlines5.jpg', img)
# Tampilkan
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()