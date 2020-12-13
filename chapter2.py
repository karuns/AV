import cv2
import numpy as np
print('Important image functions')

def important_image_functions(image_path):
    img = cv2.imread(image_path)
    cv2.imshow('Outout', img)


    # Gray Image
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Gray Image", imgGray)

    # BLurImage
    imgBlur = cv2.GaussianBlur(imgGray,(7,7), 1)
    cv2.imshow("Blur Image",imgBlur)

    # Canny image or lined image
    imgCanny = cv2.Canny(img, 150, 200)
    cv2.imshow("Canny Image", imgCanny)

    # Make image diluted (increase thickness of lines)
    kernel = np.ones((5,5), np.uint8)
    imgDilated = cv2.dilate(imgCanny,kernel,iterations=1)
    cv2.imshow("Dialeted Image", imgDilated)

    # Make image eroded (get back to sharpness, instead of dialetion)
    imgEroded = cv2.erode(imgDilated,kernel, iterations=1)
    cv2.imshow("Eroded(Undiluted) image",imgEroded)
    cv2.waitKey(0)
important_image_functions('Resources/lena.png')