import cv2 as cv

img = cv.imread('images/elon.jfif')

cv.imshow("Output", img)

print("Olá")

cv.waitKey(0)