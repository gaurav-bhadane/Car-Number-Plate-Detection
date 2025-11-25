from agents.agent_preprocessor import PreprocessingAgent
from agents.agent_detector import DetectionAgent
from agents.agent_ocr import OCRAgent
from agents.agent_file_manager import FileManagerAgent
from agents.agent_notification import NotificationAgent
from agents.agent_error_handler import ErrorHandlingAgent

class OrchestratorAgent:
    def __init__(self):
        self.pre = PreprocessingAgent()
        self.det = DetectionAgent()
        self.ocr = OCRAgent()
        self.fm = FileManagerAgent()

        self.notify = NotificationAgent(
            email_config=None,    # Add SMTP config if needed
            slack_webhook=None    # Add Slack Webhook if needed
        )

        self.error_handle = ErrorHandlingAgent(self.notify)

    def execute(self, img_path):
        try:
            # Step 1
            processed = self.pre.preprocess(img_path)

            # Step 2
            plate_img, box = self.det.detect_plate(processed)

            # Step 3
            text = self.ocr.extract_text(plate_img)

            # Step 4
            saved_path = self.fm.save_plate(plate_img)

            # Notification
            self.notify.notify_console(f"Plate Detected: {text}")
            self.notify.notify_slack(f"Plate Detected → {text}")
            
            # Log
            self.fm.log(f"{img_path} → {text} → {saved_path}")

            return {
                "status": "success",
                "plate_text": text,
                "saved_path": saved_path
            }

        except Exception as e:
            self.error_handle.handle(e)
            return {"status": "error", "message": str(e)}
