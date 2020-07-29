import cv2
import numpy as np
#cv2.EVENT_MOUSEMOVE
windowName = 'Mouse Events'
img = np.zeros((1000,1000,3))
cv2.namedWindow(windowName)
def draw(event,x,y,flags,param):#creating a method
    if event== cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img,(x,y),30,(0,255,0),-1)
    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.rectangle(img,(x,y),(x+100,y+100),(0,255,0),5)
    if event == cv2.EVENT_LBUTTONDOWN:
         cv2.line(img,(x,y),(x+100,y+100),(255,0,0),9)

cv2.setMouseCallback(windowName,draw)
while True:
    cv2.imshow(windowName,img)
    if cv2.waitKey(1)==ord('q'):
        break

cv2.destroyAllWindows()
