#!/usr/local/bin/python3 


import cv2

# import as greyscale (1 is color, -1 is color with transparency)
img = cv2.imread("galaxy.jpg", 0)
 
# print(img)
# print(type(img))
# print(img.shape)
# print(img.ndim)
# resizedimg = cv2.resize(img,(800,600))
resizedimg = cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))
cv2.imshow("Galaxy!!!", resizedimg)
cv2.imwrite("Galaxy_resized.jpg",resizedimg)
# click to close
cv2.waitKey(0)
# cv2.waitKey(4000)
cv2.destroyAllWindows()

# img1 = cv2.imread("galaxy.jpg", 1)
# print(img1)
# print(type(img1))
# print(img1.shape)
# print(img1.ndim)
