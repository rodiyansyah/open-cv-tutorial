import cv2

def main():
    imgpath = "img2.jpg"
    img = cv2.imread(imgpath)

    # display the image
    cv2.imshow('gambar', img)

    outpath = "img2_save.jpg"
    # save the image

    cv2.imwrite(outpath, img, [int(cv2.IMWRITE_JPEG_QUALITY), 100])

    cv2.waitKey(0)
    # destroy a certain window
    cv2.destroyWindow('Hanif_Life2Coding')


if __name__ == "__main__":
    main()