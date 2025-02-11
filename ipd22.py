# Apply Gaussian Blur to the grayscale image
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Optionally display the blurred image
cv2.imshow("Blurred Blueprint", blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()

# displays a slightly blurred image.