import cv2
img = cv2.imread('king.jfif',0)#put a zero here instead of the code below
cv2.imshow('Original Image',img)
#gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#cv2.imshow('Grayscale',gray)
(#thresh, blackAndWhiteImage) = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
#cv2.imshow('Black white image', blackAndWhiteImage)
cv2.waitKey(0)
cv2.destroyAllWindows()