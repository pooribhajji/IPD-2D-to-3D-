import cv2
import pytesseract

# Set the Tesseract executable path manually
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Load an image and convert it to grayscale
image = cv2.imread(r"D:\Backup\ipd\IPD-2D-to-3D-\dimg1.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Extract text from the grayscale image using Tesseract OCR
extracted_text = pytesseract.image_to_string(gray)
print("Extracted Text:")
print(extracted_text)

#Text is being extracted from the image.Problem:Text is in French ;()