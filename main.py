import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

def detect(gray,frame):
  faces = face_cascade.detectMultiScale(gray,1.5,5)
  for (x, y, w, h) in faces:
    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
  return frame

video_capture = cv2.VideoCapture(0)
while True:
  _, frame = video_capture.read()
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  canvas = detect(gray, frame)
  cv2.imshow('Video', canvas)
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break
video_capture.release()