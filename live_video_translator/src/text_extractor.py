class TextExtractor:
    def __init__(self, ocr_engine='tesseract'):
        """
        Initializes the text extractor.
        :param ocr_engine: 'tesseract', 'easyocr', or cloud API name
        """
        self.ocr_engine = ocr_engine
        print(f"TextExtractor initialized with {ocr_engine}")

    def extract_text(self, frame):
        """
        Extracts text from a given frame.
        :param frame: The input frame (e.g., a NumPy array).
        :return: A string of extracted text or None.
        """
        if frame is None:
            return None
        print("Extracting text from frame...")
        # Placeholder: Actual implementation will use pytesseract or other OCR tools
        return "Example extracted text"

    def extract_text_with_bounding_boxes(self, frame):
        """
        Extracts text and its bounding box coordinates.
        :param frame: The input frame.
        :return: A list of tuples, each (text, (x, y, w, h)), or None.
        """
        if frame is None:
            return None
        print("Extracting text with bounding boxes...")
        # Placeholder
        return [("Example text", (10, 20, 100, 30))]
