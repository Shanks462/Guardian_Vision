import json
import time
import random

time.sleep(random.randint(1, 5))  # random delay (1 to 5 sec)

data = {
        "camera": "cam1",
        "time": time.time(),
        "event": "person_detected",
        "confidence": 0.92
    }

print(json.dumps(data), flush=True)