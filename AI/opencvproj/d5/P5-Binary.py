import cv2
img = cv2.imread('king.jfif',0)
cv2.imshow('Grayscale image',img)
(thresh,binary) = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
cv2.imshow('Binary Image',binary)
cv2.waitKey(0)
cv2.destroyAllWindows()