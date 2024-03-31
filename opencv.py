import cv2 as cv

cap=cv.VideoCapture(0)

while True:
    isTrue, frame = cap.read()
    cv.imshow('frame', frame)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

cap.release()
cv.destroyAllWindows()
