class OutputDisplayer:
    def __init__(self, display_mode='overlay'):
        """
        Initializes the output displayer.
        :param display_mode: 'overlay', 'separate_window', 'caption_box'
        """
        self.display_mode = display_mode
        print(f"OutputDisplayer initialized with mode: {display_mode}")

    def display_text(self, frame, translated_text, original_text_bbox=None):
        """
        Displays the translated text.
        :param frame: The original frame (for overlay mode).
        :param translated_text: The text to display.
        :param original_text_bbox: Bounding box of original text for overlay placement.
        """
        if not translated_text:
            return
        print(f"Displaying text: '{translated_text}' in mode '{self.display_mode}'")
        # Placeholder: Actual implementation will use OpenCV for overlay or a GUI library.
        if self.display_mode == 'overlay' and frame is not None:
            # Example: Draw on frame (needs OpenCV)
            # cv2.putText(frame, translated_text, (x,y), font, scale, color, thickness)
            print("Overlaying text on frame.")
            return frame # Return modified frame
        return None

    def update_caption_window(self, translated_text):
        """
        Updates a dedicated caption window.
        """
        print(f"Updating caption window with: {translated_text}")
        # Placeholder
