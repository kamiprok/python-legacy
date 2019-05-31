import cv2

img = cv2.imread('pyimg.jpg')

print(type(img))

cv2.imshow('Original Image', img)
cv2.waitKey()

