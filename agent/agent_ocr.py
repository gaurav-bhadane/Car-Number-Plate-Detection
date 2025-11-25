import easyocr

class OCRAgent:
    def __init__(self):
        self.reader = easyocr.Reader(['en'])

    def extract_text(self, plate_img):
        result = self.reader.readtext(plate_img, detail=0)

        if not result:
            return "UNREADABLE"

        # Join lines & clean
        text = "".join(result).replace(" ", "")
        return text
