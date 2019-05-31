import cv2

img = cv2.imread('pyimg.jpg')

print(type(img))

# cv2.imshow('Original Image', img)
# cv2.waitKey()

print(img.shape[0:2])

width = img.shape[0]
height = img.shape[1]

# (center point, angle, scale)
rotationMatrix = cv2.getRotationMatrix2D((250, 650), 30, .5)

rotatedImage = cv2.warpAffine(img, rotationMatrix, (width, height))

cv2.imshow('Rotated Image', rotatedImage)
cv2.waitKey()
