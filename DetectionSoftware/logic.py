import numpy as np

def calculate_distance(p1, p2):
    return np.linalg.norm(np.array(p1) - np.array(p2))


def detect_threat(persons):
    threat = False

    for i in range(len(persons)):
        for j in range(i+1, len(persons)):
            x1, y1, x2, y2 = persons[i]
            x3, y3, x4, y4 = persons[j]

            center1 = ((x1+x2)//2, (y1+y2)//2)
            center2 = ((x3+x4)//2, (y3+y4)//2)

            dist = calculate_distance(center1, center2)

            if dist < 100:  # threshold
                threat = True

    return threat