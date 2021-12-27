import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 6)
    for faces in faces:
        x, y, w, h = faces
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        if faces != ():
            if y >= 100 and x >= 100:
                roi = frame[y - 50:y + h + 100, x - 100:x + w + 100]
            elif y <= 100 or x <= 100:
                roi = frame
        elif faces == ():
            print('No faces found')
    cv2.imshow('roi', roi)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
