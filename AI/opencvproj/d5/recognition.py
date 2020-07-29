import numpy as np
import cv2
img = np.zeros((1000,1000,3))
#for i in range(0,600,100):
    #cv2.line(img, (0,i ), (500,i), (0, 0, 255), 5)
    #cv2.imshow('red line', img)
#for j in range(0,600,100):
    #cv2.line(img, (j, 0), (j, 500), (0, 0, 255), 5)
    #cv2.imshow('red line', img)

#cv2.line(img, (0,100), (500,100), (0, 0, 255), 5)
#cv2.imshow('red line', img)
#cv2.rectangle(img,(0,0),(500,200),(255,0,0),-9)
#cv2.circle(img,(250,250),100,(0,255,0),9)
#cv2.imshow('green circle',img)
name = input("Enter Your Name: ")
cv2.putText(img,name,(250,250),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),1)
cv2.imshow('text',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
