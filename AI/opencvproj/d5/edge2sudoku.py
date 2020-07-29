import cv2
img = cv2.imread('sudoku_puzzle.jpg')

sobel_x=cv2.Sobel(img,cv2.CV_8U,dx=1,dy=0,ksize=-1)
sobel_y=cv2.Sobel(img,cv2.CV_8U,dx=0,dy=1,ksize=-1)
sobel_f= cv2.bitwise_or(sobel_x,sobel_y)

cv2.imshow('Sobel X-Image',sobel_x)
cv2.imshow('Sobel Y-Image',sobel_y)
cv2.imshow('Sobel Final Image',sobel_f)

cv2.waitKey(0)
cv2.destroyAllWindows()
