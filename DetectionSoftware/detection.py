import cv2
from ultralytics import YOLO
# Load YOLO model
model = YOLO("yolov8n.pt")

def get_pose(frame):
    import mediapipe as mp
    mp_pose = mp.solutions.pose
    pose = mp_pose.Pose()
    
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = pose.process(rgb)
    return results.pose_landmarks

def detect_people(frame):
    results = model(frame, verbose=False)
    persons = []

    for r in results:
        for box in r.boxes:
            cls = int(box.cls[0])
            if cls == 0:  # person class
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                persons.append((x1, y1, x2, y2))

    return persons

