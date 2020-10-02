# import packages
from face.face1 import anonymize_face_simple
import numpy as np
import cv2
import os



# memuat model pendeteksi wajah
prototxtPath = ("model/deploy.prototxt")
weightsPath = ("model/res10_300x300_ssd_iter_140000.caffemodel")
net = cv2.dnn.readNet(prototxtPath, weightsPath)

# memuat gambar input, mengkloningnya, dan ambil gambar spasial
# ukuran
image = cv2.imread("face.png")
orig = image.copy()
(h, w) = image.shape[:2]

# membangun blob dari gambar
blob = cv2.dnn.blobFromImage(image, 1.0, (300, 300),
	(104.0, 177.0, 123.0))

# mendapatkan deteksi wajah
net.setInput(blob)
detections = net.forward()

# loop deteksi wajahnya
for i in range(0, detections.shape[2]):
	# deteksi
	confidence = detections[0, 0, i, 2]
	if confidence > 0.5:
		# menghitung (x, y) - koordinat kotak pembatas untuk objek yang terdeteksi
		box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
		(startX, startY, endX, endY) = box.astype("int")

		# ekstrak ROI wajahnya
		face = image[startY:endY, startX:endX]

		# memeriksa untuk melihat apakah kita menerapkan pengaburan pada wajah
		face = anonymize_face_simple(face, factor=3.0)
		# kemudian simpan wajah buram di gambar output
		image[startY:endY, startX:endX] = face

# menampilkan gambar asli dan gambar buram
output = np.hstack([orig, image])
cv2.imshow("Output", output)
cv2.waitKey(0)