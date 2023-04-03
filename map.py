import cv2
import numpy as np
import sys

img = cv2.imread("Hackathontech.png")
print(img.shape)

rows, cols,  = img.shape

# Draw vertical lines
for i in range(cols):
    if i % 10 == 0: # draw a line every 10 pixels
        cv2.line(img, (i, 0), (i, rows), (0, 0, 0), 1)

# Draw horizontal lines
for i in range(rows):
    if i % 10 == 0: # draw a line every 10 pixels
        cv2.line(img, (0, i), (cols, i), (0, 0, 0), 1)

# Show the image
cv2.imshow("Image", img)

# Wait for a key press and then close the window
cv2.waitKey(0)
cv2.destroyAllWindows()