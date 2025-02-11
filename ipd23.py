# Perform Canny Edge Detection on the blurred image
edges = cv2.Canny(blurred, 50, 150)

# Display the edge-detected image
cv2.imshow("Edges Detected", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()


## CANNY EDGE DETECTION Performed !!