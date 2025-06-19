from .input_handler import InputHandler
from .text_extractor import TextExtractor
from .translation_engine import TranslationEngine
from .speech_synthesizer import SpeechSynthesizer
from .output_displayer import OutputDisplayer

class MainApp:
    def __init__(self, config=None):
        """
        Initializes the main application and its components.
        """
        self.config = config if config else self._default_config()

        self.input_handler = InputHandler(
            source_type=self.config['input']['type'],
            source_path=self.config['input'].get('path')
        )
        self.text_extractor = TextExtractor(
            ocr_engine=self.config['ocr']['engine']
        )
        self.translation_engine = TranslationEngine(
            api_service=self.config['translation']['service'],
            target_language=self.config['translation']['target_lang']
        )
        self.speech_synthesizer = SpeechSynthesizer(
            tts_service=self.config['tts']['service'],
            voice_emotion=self.config['tts']['emotion']
        )
        self.output_displayer = OutputDisplayer(
            display_mode=self.config['output']['mode']
        )
        print("MainApp initialized with all components.")

    def _default_config(self):
        return {
            'input': {'type': 'webcam'},
            'ocr': {'engine': 'tesseract'},
            'translation': {'service': 'google_translate_api', 'target_lang': 'es'},
            'tts': {'service': 'google_tts', 'emotion': 'neutral'},
            'output': {'mode': 'overlay'}
        }

    def run_pipeline(self):
        """
        Runs the main translation pipeline for a single frame/image.
        """
        print("\n--- Running translation pipeline ---")
        frame = self.input_handler.capture_frame()
        if frame is None:
            print("Failed to capture frame.")
            # return # Commented out to allow pipeline to proceed for stub testing

        extracted_text = self.text_extractor.extract_text(frame)
        if not extracted_text:
            print("No text extracted.")
            # return # Commented out to allow pipeline to proceed for stub testing

        translated_text = self.translation_engine.translate(extracted_text)
        if not translated_text:
            print("Translation failed.")
            # return # Commented out to allow pipeline to proceed for stub testing

        # Speech synthesis (can be run in parallel or optionally)
        # audio_output = self.speech_synthesizer.synthesize_speech(translated_text)
        # if audio_output:
        #     print(f"Generated audio (size: {len(audio_output)} bytes).")
            # Add code to play audio_output

        # Display output
        modified_frame = self.output_displayer.display_text(frame, translated_text)
        if modified_frame is not None:
            print("Frame modified for display.")
            # Add code to show modified_frame (e.g., cv2.imshow)

        print("--- Pipeline finished ---\n")

if __name__ == '__main__':
    app = MainApp()
    # This is a conceptual run for one frame.
    # Real application would have a loop for video.
    app.run_pipeline()

    # Example with image file
    # config_img = app._default_config()
    # config_img['input']['type'] = 'image_file'
    # config_img['input']['path'] = 'data/sample_image.png' # Assuming a sample image exists
    # app_img = MainApp(config=config_img)
    # app_img.run_pipeline()
