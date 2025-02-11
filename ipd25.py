import cv2
import pytesseract
from deep_translator import GoogleTranslator

# Set Tesseract executable path (adjust if needed)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Load and preprocess your image
image_path = r"D:\Backup\ipd\IPD-2D-to-3D-\dimg1.png"
image = cv2.imread(image_path)
if image is None:
    print("Error: Image not found. Check the file path:", image_path)
else:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # (Optional: display or further process the image)

    # Extract French text using Tesseract OCR
    french_text = pytesseract.image_to_string(gray, lang='fra')
    print("Extracted French Text:")
    print(french_text)
    
    # Translate French text to English using deep-translator
    translated_text = GoogleTranslator(source='fr', target='en').translate(french_text)
    print("Translated English Text:")
    print(translated_text)


#

##1. **OCR Output Quality:**  
 #  - The extracted French text contains a mix of numbers, symbols, and words. Some parts (like "vide sur combles", "salon", "CHAMBRE 4", "PALIER 1.36") are recognizable, while other parts are garbled.  
  # - This is common when the image quality isn’t optimal or if the blueprint has complex layouts, small fonts, or noise. It suggests that Tesseract is picking up both the intended text and some extraneous artifacts.

#2. **Translation Results:**  
#   - The translated output reflects the OCR output. For example, "vide sur combles" has been translated as "empty on attic" and "salon" as "living room", while "CHAMBRE" becomes "BEDROOM".  
#   - However, since the OCR output is noisy, the translation also contains a lot of the garbled parts. Translation libraries work on the text they receive, so any OCR errors will be carried through.

#3. **Next Steps for Improvement:**  
#   - **Enhance Preprocessing:**  
#     Consider additional image processing steps (such as thresholding, resizing, or contrast adjustment) to improve OCR accuracy.  
#   - **Parameter Tuning:**  
#     Experiment with Tesseract’s configuration options (for instance, using a custom config file or adjusting the DPI setting) to reduce errors.  
#  - **Post-OCR Cleaning:**  
#     Apply regex or other text-cleaning techniques to filter out unwanted symbols and isolate meaningful words before translation.
#  - **Image Quality:**  
#     If possible, use higher-quality images or scans of your blueprints.
