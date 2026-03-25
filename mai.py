import json
import time

for i in range(5):
    data = {
        "camera": "cam1",
        "time": time.time(),
        "event": "person_detected",
        "confidence": 0.92
    }

    print(json.dumps(data), flush=True)
    time.sleep(1)