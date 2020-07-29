import cv2
import numpy as np
#a = np.ones(10)
#print(a)
#print(type(a))
img1 = np.ones((500,500,3))
cv2.imshow('White Background',img1)
img = np.zeros((250,500,3))
cv2.imshow('Black Background', img)
cv2.waitKey(0)
cv2.destroyAllWindows()