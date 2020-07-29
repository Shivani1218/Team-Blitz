import cv2
face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#face = cv2.CascadeClassifier('haarcascade_smile.xml')


img = cv2.imread('abc.jpg')
gray = cv2.imread('abc.jpg',0)
faces = face.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=200)
for x,y,w,h in faces:
  img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),5)
  cv2.imshow('Face Recognised',img)
#cv2.imshow('Face Recognised',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
