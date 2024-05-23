import cv2

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('models/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('models/haarcascade_eye.xml')

while True:
    ret, frame = cap.read()
    
    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    faces_rect = face_cascade.detectMultiScale(gray_img, scaleFactor=2.0, minNeighbors=5)
    
    eyes_rect = eye_cascade.detectMultiScale(gray_img, scaleFactor=1.3, minNeighbors=9)
    
    if len(faces_rect) == 1 and len(eyes_rect) == 1:
        cv2.imwrite("public/output_image.jpg", frame)
        break
    cv2.imshow("webcam window", frame)

cap.release()
cv2.destroyAllWindows()


