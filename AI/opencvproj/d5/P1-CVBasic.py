import cv2

img = cv2.imread('small flower.png')
cv2.imshow('Output Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()