import cv2
img = cv2.imread('sudoku_puzzle.jpg')

canny=cv2.Canny(img,100,250)


cv2.imshow('Canny Final Image',canny)
cv2.findContours()
cv2.waitKey(0)
cv2.destroyAllWindows()
