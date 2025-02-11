import cv2

# Load the blueprint image; update the path to your image file.
image_path = r"D:\Backup\ipd\IPD-2D-to-3D-\dimg1.png"  # Use a raw string or "D:\\Backup\\ipd\\dimg1.png"
image = cv2.imread(image_path)

if image is None:
    print("Error: Image not found. Please check the file path:", image_path)
else:
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Display the grayscale image
    cv2.imshow("Grayscale Blueprint", gray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

## Grayscale image is being displayed.Moving on to step 2 in phase 2.