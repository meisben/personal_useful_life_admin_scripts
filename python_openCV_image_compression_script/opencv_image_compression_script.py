import cv2
import numpy as np
from os import listdir
from os.path import isfile, join


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
        cv2.imwrite(
            path, image, [int(cv2.IMWRITE_PNG_COMPRESSION), png_compression])
    else:
        cv2.imwrite(path, image)


def findFilesNames(imgpath):
    onlyfiles = [f for f in listdir(
        imgpath) if isfile(join(imgpath, f))]
    return onlyfiles


def main():

    # Edit this line each time !!
    imgPath = r'M:\Images pack MK2 refill station'

    imagesNameList = findFilesNames(imgPath)

    print(imagesNameList)

    for imgName in imagesNameList:

        currentFilePath = join(imgPath, imgName)

        img = cv2.imread(currentFilePath)

        # # display the image
        # cv2.imshow(imgName, img)

        # save the image in JPEG format with 85% quality
        outPath_jpeg = currentFilePath[:-4] + "_compressed.jpg"
        save(outPath_jpeg, img, jpg_quality=85)

        # # save the image in PNG format with 4 Compression
        # outPath_png = currentFilePath[:-4] + "_compressed.png"
        # save(outPath_png, img, png_compression=4)

        # # destroy a certain window
        # cv2.waitKey(0)
        # cv2.destroyWindow(imgName)


if __name__ == "__main__":
    main()
