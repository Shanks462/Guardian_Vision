# 🚨 GUARDIAN VISION

**Intelligent Real-Time Threat Detection & Smart Surveillance System with Women Safety Focus**

---

## 📌 Overview

Guardian Vision AI is an advanced AI-powered surveillance system designed to transform traditional CCTV cameras into proactive threat detection units.

The system detects:
- Violent behavior
- Physical aggression
- Suspicious interactions
- Abnormal crowd dynamics
- Potential harassment scenarios

**🔴 Primary Focus:** Enhancing women’s safety in public spaces by identifying early signs of harassment, forced interaction, stalking patterns, or assault-related behavior.

Instead of passively recording footage, Guardian Vision analyzes live video streams in real time and instantly alerts authorities or response teams with contextual evidence.

---

## 🎯 Problem Statement

Women’s safety remains a critical concern in public environments such as streets, transportation hubs, campuses, and marketplaces.

**Traditional CCTV systems:**
- Only record incidents
- Require manual monitoring
- React after the event occurs

There is a need for a scalable, intelligent surveillance system that can:
- Detect potential harassment or assault scenarios in real time
- Identify aggressive or unsafe interactions
- Reduce response time significantly
- Maintain ethical and privacy compliance

---

## 💡 Our Solution

GuardianVision AI combines:
- Real-time human detection
- Pose estimation
- Interaction modeling
- Violence classification
- Anomaly detection algorithms

The system evaluates behavioral patterns rather than relying solely on object detection, allowing it to detect:
- One person forcefully pulling another
- Sudden aggressive motion
- Group surrounding a single individual
- Falling or distress-like posture
- Abnormal pursuit behavior

This makes it particularly effective for early identification of potential threats against women in public spaces.

---

## 🧠 How It Works

1. **Service Orchestration (Go Backend)**
   - The Go-based main application acts as the central control structure.
   - It parses system configurations (`config.yaml`) and efficiently oversees concurrent camera streams.
   
2. **Live CCTV Feed Processing (Python Engine)**
   - The Go backend automatically spawns headless Python detection subprocesses for each camera source.
   - Video frames are extracted continuously in real-time by the Python inference engine.

3. **Detection & Behavioral Analysis**
   - **YOLOv8** identifies individuals within the video feed.
   - **MediaPipe** (optional) maps body keypoints to assess behavioral context.
   - The system calculates distances and analyzes movement to classify potential threats, checking for close, aggressive proximity.

4. **Event Streaming & Logging**
   - When a designated threat (e.g., Harassment/Assault) is detected, the Python engine emits a structured JSON alert to `stdout`.
   - The Go event handler intercepts these JSON outputs in real-time and orchestrates date-stamped log storage and future alert dispatching.

---

## 🏗️ System Architecture

Our system operates dynamically using a robust Go-Python hybrid architecture:

**[ Camera Subsystem / CCTV Feeds ]**
       ↓
**[ Go Service Manager (`cmd/main.go`) ]** *(Spawns & Tracks Processes)*
       ↓
**[ Python AI Subprocesses (`DetectionSoftware/main.py`) ]**
   ├─ Frame Extraction (OpenCV)
   ├─ Object Detection (YOLOv8)
   └─ Threat Logic Engine
       ↓
*(JSON Event Stream via stdout)*
       ↓
**[ Go Event Handler (`handler/Camera/`) ]** *(Asynchronous Reader)*
   ├─ Date-based Continuous Logging (`logs/YYYY-MM-DD/`)
   └─ Event Routing
       ↓
**[ Dashboard / Alerting Systems ]** *(Upcoming)*

---

## ⚙️ Tech Stack

**Backend & Orchestration**
- **Go (Golang)**: Scalability, Concurrency, Process Management, Data Streams

**AI / Machine Learning Engine**
- **Python**
- **OpenCV**: Feed handling
- **Ultralytics YOLOv8**: Real-time object tracking
- **NumPy**: Distance and geometric calculations
- **MediaPipe**: Pose Estimation heuristics

**Data Persistence**
- Secure Local Storage via partitioned log indexing.

---

## 🔐 Privacy & Ethical AI

GuardianVision is built with a privacy-first architecture:
- Focuses entirely on behavior mapping rather than structural facial recognition.
- No identity caching or PII (Personally Identifiable Information) storage.
- Operates statelessly, only storing log events when an aggressive threshold is explicitly broken.

---

## 📊 Key Features

- 🎥 **Scalable Camera Orchestration:** Handled concurrently via Go routines.
- ⚠️ **Intelligent Threat Detection:** Heuristic-based alerts for violent scenarios.
- 👩 **Women Safety-Focused Analytics:** specifically prioritizing risk scenarios common to harassment.
- 🗂️ **Zero-overhead Communication:** Real-time data piping between native binaries and python instances without complex HTTP overheads.

---

## 🌍 Use Cases

- Smart Cities
- Public Transport Systems
- University Campuses
- Shopping Malls
- Corporate Offices
- Public Events

**Primary Impact:** Strengthening women’s safety and proactive threat prevention in public spaces.

---

## 👥 Team

- **SHANKS**
- **ADITYA RAWAT**
- **ADITYA SHUKLA**
- **VINAYAK**

---

*Building smarter security. Protecting lives proactively.*
