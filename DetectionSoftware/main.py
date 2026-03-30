import sys
import cv2
import json
import time
from detection import detect_people
from logic import detect_threat

def main():
    # Read command line arguments
    if len(sys.argv) < 3:
        print("Usage: python3 main.py <source> <camera_name>", file=sys.stderr)
        sys.exit(1)

    source_arg = sys.argv[1]
    camera_name = sys.argv[2]

    # Handle numeric vs string sources
    if source_arg.isdigit():
        source = int(source_arg)
    else:
        source = source_arg

    cap = cv2.VideoCapture(source)

    if not cap.isOpened():
        print(f"Error: Could not open video source {source}", file=sys.stderr)
        sys.exit(1)

    last_event_time = 0
    cooldown_seconds = 2.0

    while True:
        ret, frame = cap.read()
        if not ret:
            # End of video stream or error
            break

        # Run detections
        persons = detect_people(frame)
        threat = detect_threat(persons)

        current_time = time.time()

        # Build an event based on detection
        event_msg = None
        confidence = 0.0

        if threat:
            event_msg = "Threat Detected (Harassment/Assault)"
            confidence = 0.95

        # Print JSON event to stdout if an event occurred and cooldown has passed
        if event_msg and (current_time - last_event_time > cooldown_seconds):
            event = {
                "Camera": camera_name,
                "Time": current_time,
                "Event": event_msg,
                "Confidence": confidence
            }
            # Flush stdout to ensure the Go backend receives immediately
            print(json.dumps(event), flush=True)
            last_event_time = current_time

        # Headless operation, no cv2.imshow() to prevent blocking and GUI errors

    cap.release()

if __name__ == "__main__":
    main()
