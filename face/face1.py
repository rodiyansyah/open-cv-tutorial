# import packages
import numpy as np
import cv2


def anonymize_face_simple(image, factor=3.0):
    # secara otomatis menentukan ukuran berdasarkan kernel
    # dimensi spasial dari gambar input
    (h, w) = image.shape[:2]
    kW = int(w / factor)
    kH = int(h / factor)

    # pastikan lebar kernel
    if kW % 2 == 0:
        kW -= 1

    # pastikan ketinggian kernel
    if kH % 2 == 0:
        kH -= 1

    # terapkan Gaussian blur
    # ukuran kernel
    return cv2.GaussianBlur(image, (kW, kH), 0)

def anonymize_face_pixelate(image, blocks=3):
    # bagi gambar input menjadi blok NxN
    (h, w) = image.shape[:2]
    xSteps = np.linspace(0, w, blocks + 1, dtype="int")
    ySteps = np.linspace(0, h, blocks + 1, dtype="int")

    # lingkaran di atas blok di kedua arah x dan y
    for i in range(1, len(ySteps)):
        for j in range(1, len(xSteps)):
            # hitung koordinat awal dan akhir (x, y)
            # untuk blok saat ini
            startX = xSteps[j - 1]
            startY = ySteps[i - 1]
            endX = xSteps[j]
            endY = ySteps[i]

            # nilai RGB di atas ROI pada gambar
            roi = image[startY:endY, startX:endX]
            (B, G, R) = [int(x) for x in cv2.mean(roi)[:3]]
            cv2.rectangle(image, (startX, startY), (endX, endY),
                          (B, G, R), -1)

    # mengembalikan gambar blur
    return image