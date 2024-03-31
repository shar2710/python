import cv2 as cv

img=cv.imread('Downloads/R.jpeg')

cv.imshow('R (1)', img)

cv.waitKey(0)
cv.destroyAllWindows()