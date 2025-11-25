import os
import cv2
from datetime import datetime

class FileManagerAgent:
    def __init__(self, output_folder="plates"):
        self.output_folder = output_folder
        os.makedirs(self.output_folder, exist_ok=True)

    def save_plate(self, img):
        filename = f"plate_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
        save_path = os.path.join(self.output_folder, filename)
        cv2.imwrite(save_path, img)
        return save_path

    def log(self, text):
        with open("process_log.txt", "a") as f:
            f.write(text + "\n")
