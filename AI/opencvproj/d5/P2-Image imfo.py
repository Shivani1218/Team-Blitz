import cv2
img = cv2.imread('small flower.png')
print(img.shape)
print('to duplicate image')
cv2.imwrite('copy.png',img)