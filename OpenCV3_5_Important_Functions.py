# -*- coding: utf-8 -*-
import cv2 as cv
img = cv.imread('C:/Users/User 2/Desktop/Tyson.jpg')


#Convert to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)
cv.waitKey(0)

#Blur
blur = cv.GaussianBlur(img, (5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)
cv.waitKey(0)

#Edge Cascade
canny = cv.Canny(img, 125, 175,)
cv.imshow('Canny Edges', canny)
cv.waitKey(0)

#Reduce edges by blurring
canny_blur = cv.Canny(blur, 125, 175,)
cv.imshow('Canny Reduced Edges', canny_blur)
cv.waitKey(0)


#Dilating
dilated = cv.dilate(canny_blur, (7,7), iterations=3)
cv.imshow('Dilated', dilated)
cv.waitKey(0)

#Eroding
eroded = cv.erode(dilated, (7,7), iterations=3)
cv.imshow('Eroded', eroded)
cv.waitKey(0)

#Cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)
cv.waitKey(0)
#Resize
resized = cv.resize(img, (250, 250))
cv.imshow('Resized', resized)
cv.waitKey(0)