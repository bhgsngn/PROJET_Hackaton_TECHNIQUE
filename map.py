import cv2

def is_color_at_position(self, color, x, y):
    # Retourne True si la couleur à la position (x, y) correspond à la couleur donnée
    b, g, r = self.image[y, x]
    return color == (b, g, r)

def get_new_direction(self, current_direction, x, y):
    # Retourne une nouvelle direction en fonction de la couleur à la position (x, y)
    if self.is_color_at_position((0, 0, 255), x, y): # Rouge
        if current_direction == "droite":
            return "haut"
        elif current_direction == "bas":
            return "droite"
        elif current_direction == "gauche":
            return "bas"
        elif current_direction == "haut":
            return "gauche"
    elif self.is_color_at_position((0, 255, 0), x, y): # Vert
        if current_direction == "droite":
            return "bas"
        elif current_direction == "bas":
            return "gauche"
        elif current_direction == "gauche":
            return "haut"
        elif current_direction == "haut":
            return "droite"
    # Ajoutez ici d'autres couleurs et directions possibles
    else:
        return current_direction

def draw_grid(self):
    # Dessine des lignes de grille sur l'image
    for i in range(self.cols):
        if i % 10 == 0: # dessine une ligne tous les 10 pixels
            cv2.line(self.image, (i, 0), (i, self.rows), (0, 0, 0), 1)

    for i in range(self.rows):
        if i % 10 == 0: # dessine une ligne tous les 10 pixels
            cv2.line(self.image, (0, i), (self.cols, i), (0, 0, 0), 1)

def show(self):
    # Affiche l'image
    cv2.imshow("Image", self.image)

def wait_for_key(self):
    # Attend une pression de touche et ferme la fenêtre
    cv2.waitKey(0)
    cv2.destroyAllWindows()