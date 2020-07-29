import cv2
import numpy as np
#a = np.ones(10)
#print(a)
#print(type(a))
#they follow BGR
img1=np.zeros((250,250,3))
img1[:,:]=255,0,0
cv2.imshow('Blue Background',img1)

img = np.zeros((500,500,3))
img[0:250,0:250]=0,0,0
img[0:250,250:500]=1,1,1
img[250:500,250:500]=0,0,0
img[250:500,0:250]=1,1,1
cv2.imshow('Checkerboard',img)


cv2.waitKey(0)
cv2.destroyAllWindows()

