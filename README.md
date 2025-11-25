# 🚗 AI-Based Car Number Plate Detection & Intelligent Monitoring System

An end-to-end AI-powered system that detects vehicle number plates from images/video using deep learning, extracts text using OCR, and uses intelligent agents for violation monitoring and automated alerts.  
Built for **traffic surveillance**, **parking automation**, **toll systems**, and **law enforcement applications**.

---

## ✨ Features

### 🔍 1. Number Plate Detection
- Detects number plates in images or real-time video.
- Uses deep learning (YOLO / Haar Cascade / SSD / Faster-RCNN).
- Supports Indian and international plates.

### 🔠 2. OCR – Number Plate Recognition
- Extracts alphanumeric characters from detected plates.
- Works in multiple lighting & environmental conditions.

### 🎥 3. Real-Time Video Processing
- Compatible with webcams, CCTV feeds, and IP cameras.
- Optimized for low latency and high FPS.

### 🤖 4. Intelligent Violation Monitoring Agent
Automatically detects:
- Overspeeding  
- Red-light jump  
- Wrong parking  
- Lane violations  

For each violation:
- Captures plate image  
- Logs time, location, violation type  
- Sends real-time alerts to owner + authorities  
- Generates structured logs/reports  

### 📩 5. Automated Follow-Up System
If fines remain unpaid:
- Sends automated email/SMS reminders  
- Escalates alerts to control room  
- Maintains violation + reminder logs  

---

## 🧠 How the System Works

1. Camera captures video  
2. AI detects number plates  
3. OCR extracts characters (e.g., **MH12AB1234**)  
4. Violation agent analyses frame for rules  
5. Real-time alerts sent  
6. Automated reminders follow  
7. All logs stored & tracked  

---

## 🏗️ Project Architecture

Camera Feed
      ↓
Number Plate Detector (YOLO/Haar)
      ↓
OCR Recognition (EasyOCR/Tesseract)
      ↓
Violation Monitoring Agent
      ↓
Notification Service (Email/SMS/Slack)
      ↓
Follow-up Automation
      ↓
Logs / Reports / Database



---

# 🧩 Agent Architecture (New Integration)

| Agent | Responsibility |
|-------|---------------|
| **PreprocessingAgent** | Cleans and prepares images |
| **DetectionAgent** | Detects number plates |
| **OCRAgent** | Extracts text from plate |
| **FileManagerAgent** | Saves plates, logs data |
| **NotificationAgent** | Console, Email, Slack alerts |
| **ErrorHandlingAgent** | Logs errors + sends alerts |
| **OrchestratorAgent** | Controls full workflow |

---

---

## 🔧 Tech Stack

### **Computer Vision & AI**
- OpenCV  
- YOLO / SSD / Haar Cascade  
- EasyOCR / Tesseract  

### **Backend & Agents**
- Python  
- Autogen / LangGraph  
- FastAPI / Flask (optional)

### **Notifications**
- SMTP Email  
- Slack Webhooks  
- Twilio / Firebase SMS  

### **Storage**
- MongoDB  
- PostgreSQL  
- Local storage for plate images  

---