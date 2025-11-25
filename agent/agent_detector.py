import cv2
import numpy as np
from number_plate import NumberPlateDetector

class DetectionAgent:
    def __init__(self):
        self.model = NumberPlateDetector()

    def detect_plate(self, image):
        # Get bounding box from your model
        x, y, w, h = self.model.detect(image)

        # Crop plate region
        plate_img = image[y:y+h, x:x+w]

        return plate_img, (x, y, w, h)
