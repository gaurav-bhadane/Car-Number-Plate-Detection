import cv2
import datetime

# Agent imports
from agent.violation_agent import ViolationMonitoringAgent
from agent.rules_engine import RulesEngine
from agent.notification_service import NotificationService
from agent.database_service import DatabaseService

# Path to the Haar Cascade classifier XML file for license plate detection
harcascade = "/model/haarcascade_russian_plate_number.xml"

# Accessing the webcam (index 0)
cap = cv2.VideoCapture(0)

cap.set(3, 640) # width
cap.set(4, 480) # height

min_area = 500
count = 0

# Initialize agent
rules = RulesEngine()
notify = NotificationService()
db = DatabaseService()

agent = ViolationMonitoringAgent(
    notification_service=notify,
    db_service=db,
    rules_engine=rules
)

while True:
    success, img = cap.read()

    plate_cascade = cv2.CascadeClassifier(harcascade)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    plates = plate_cascade.detectMultiScale(img_gray, 1.1, 4)

    for (x, y, w, h) in plates:
        area = w * h

        if area > min_area:
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(img, "Number Plate", (x, y-5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 0, 255), 2)

            img_roi = img[y: y+h, x:x+w]
            cv2.imshow("ROI", img_roi)

            # ---- Agent Integration ----
            frame_data = img_roi.copy()

            # Temporary metadata (can be replaced with real inputs)
            metadata = {
                "speed": 75,
                "location": "Camera-01 Junction",
                "signal_status": "GREEN",
                "timestamp": datetime.datetime.now().isoformat()
            }

            agent.process_detection(
                plate_number="UNKNOWN_PLATE",
                frame_data=frame_data,
                metadata=metadata
            )
            # ---------------------------

    cv2.imshow("Result", img)

    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite("plates/scaned_img_" + str(count) + ".jpg", img_roi)
        cv2.rectangle(img, (0, 200), (640, 300), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, "Plate Saved", (150, 265), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2, (0, 0, 255), 2)
        cv2.imshow("Results", img)
        cv2.waitKey(500)
        count += 1
