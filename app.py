import cv2
from detection import detect_people
from logic import detect_threat
from alert import send_alert

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    persons = detect_people(frame)
    threat = detect_threat(persons)

    for (x1, y1, x2, y2) in persons:
        color = (0,255,0)

        if threat:
            color = (0,0,255)

        cv2.rectangle(frame, (x1,y1), (x2,y2), color, 2)

    if threat:
        send_alert()

    cv2.imshow("RakshaVision", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()