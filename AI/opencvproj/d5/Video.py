import cv2
cap = cv2.VideoCapture(0)

while True:
    ret,frame =cap.read()#ret isnt doing anything but is required for the program to run
    canny = cv2.Canny(frame,20,150)
    cv2.imshow('My Live Sketch',canny)
    if cv2.waitKey(1) == 13:#13 is the askey value of enter key
        break

cap.release()
cv2.destroyAllWindows()
