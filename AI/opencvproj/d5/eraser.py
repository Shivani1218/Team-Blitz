import cv2
import numpy as np
windowName = 'Mouse Events'
img = cv2.imread('king.jfif',)
cv2.namedWindow(windowName)

eraser= False
x_start, y_start, x_end, y_end = 0, 0, 0, 0
x,y=0,0
def draw_circle(event, x, y, flags, param, eraser=None):
    if (event == cv2.EVENT_LBUTTONDOWN):
        x_start, y_start, x_end, y_end = x, y, x, y
        eraser = True
    elif (event == cv2.EVENT_MOUSEMOVE):
        if eraser == True:
            x_end, y_end = x, y

    elif event == cv2.EVENT_LBUTTONUP:
        x_end, y_end = x, y
        eraser = False



cv2.setMouseCallback(windowName, draw_circle)
while True:

    i = img.copy()
    if not eraser:
        cv2.imshow("image", img)

    elif eraser:
        cv2.circle(img, (x, y), 20, (255, 255, 255), -1)
        cv2.imshow(windowName, img)

    if cv2.waitKey(1) == ord('q'):
        break
