import cv2
import numpy as np
import sys
import concurrent.futures
import os

# Obtenez le chemin absolu du répertoire courant
current_dir = os.path.abspath(os.path.dirname(__file__))

# Nom du fichier image
image_file = "Hackathontech.png"

# Chemin complet de l'image
image_path = os.path.join(current_dir, image_file)

# Chargez l'image
img = cv2.imread(image_path)

# Afficher la forme de l'image
print(img.shape)



rows, cols, _ = img.shape

def draw_vertical_lines(img, start, end, step):
    for i in range(start, end):
        if i % step == 0:
            cv2.line(img, (i, 0), (i, rows), (0, 0, 0), 1)

def draw_horizontal_lines(img, start, end, step):
    for i in range(start, end):
        if i % step == 0:
            cv2.line(img, (0, i), (cols, i), (0, 0, 0), 1)

# Use concurrent.futures to run the two loops in parallel
with concurrent.futures.ThreadPoolExecutor() as executor:
    future1 = executor.submit(draw_vertical_lines, img, 0, cols, 10)
    future2 = executor.submit(draw_horizontal_lines, img, 0, rows, 10)

# Show the image
cv2.imshow("Image", img)

# Wait for a key press and then close the window
cv2.waitKey(0)
cv2.destroyAllWindows()

