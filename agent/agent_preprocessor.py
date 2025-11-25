import cv2
import os

class PreprocessingAgent:
    def __init__(self):
        pass

    def preprocess(self, img_path):
        if not os.path.exists(img_path):
            raise FileNotFoundError("Image not found!")

        img = cv2.imread(img_path)

        # Resize for consistency
        img = cv2.resize(img, (640, 480))

        # Convert to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Noise removal
        denoised = cv2.GaussianBlur(gray, (5, 5), 0)

        return denoised
