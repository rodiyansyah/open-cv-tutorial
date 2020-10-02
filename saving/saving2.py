import cv2
import numpy as np


def save(path, image, jpg_quality=None, png_compression=None):
    '''
    persist :image: object to disk. if path is given, load() first.
    jpg_quality: for jpeg only. 0 - 100 (higher means better). Default is 95.
    png_compression: For png only. 0 - 9 (higher means a smaller size and longer compression time).
                    Default is 3.
    '''

    if jpg_quality:
        cv2.imwrite(path, image, [int(cv2.IMWRITE_JPEG_QUALITY), jpg_quality])
    elif png_compression:
        cv2.imwrite(path, image, [int(cv2.IMWRITE_PNG_COMPRESSION), png_compression])
    else:
        cv2.imwrite(path, image)


def main():
    imgpath = "img2.jpg"
    img = cv2.imread(imgpath)

    # display the image
    cv2.imshow('saving', img)

    # save the image in JPEG format with 85% quality
    outpath_jpeg = "IMG_Save_JPEG.jpg"

    save(outpath_jpeg, img, jpg_quality=100)

    outpath_png = "IMG_Save_PNG.png"

    # save the image in PNG format with 4 Compression
    save(outpath_png, img, png_compression=9)

    cv2.waitKey(0)
    # destroy a certain window
    cv2.destroyWindow('saving')


if __name__ == "__main__":
    main()