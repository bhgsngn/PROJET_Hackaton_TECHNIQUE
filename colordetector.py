#colordetector.py

import cv2

class Robot:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def move(self, x, y):
        self.position = (self.position[0] + x, self.position[1] + y)

    def detect_color(self, image):
        # Récupération de la couleur de la case où se trouve le robot
        color = image[self.position[1], self.position[0]]
        # Conversion de la couleur de BGR à RGB
        color = (color[2], color[1], color[0])
        return color