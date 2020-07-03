import os
import cv2


def main(img_path):
    img = cv2.imread(img_path)
    xmin, ymin, xmax, ymax = 429, 318, 665, 604
    crop = img[ymin:ymax, xmin:xmax]

    #img = cv2.resize(crop, (600, 800), interpolation=cv2.INTER_CUBIC)
    img2 = cv2.resize(crop, (600, 800), interpolation=cv2.INTER_LINEAR)

    #cv2.imwrite('1_.jpg', img)
    cv2.imwrite('2_.jpg', img2)

if __name__ == '__main__':
    main('1.jpg')