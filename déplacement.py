import pygame
import random

# Initialisation de pygame
pygame.init()

# Création de la fenêtre de la carte
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Ma carte")

# Chargement de l'image de la carte
map_image = pygame.image.load("chemin/vers/image/carte.png")

# Chargement de l'image de l'objet à déplacer
object_image = pygame.image.load("chemin/vers/image/objet.png")
object_width = object_image.get_width()
object_height = object_image.get_height()

# Position initiale de l'objet aléatoire
object_x = random.randint(0, window_width - object_width)
object_y = random.randint(0, window_height - object_height)

# Boucle principale du jeu
running = True
while running:

    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Déplacement de l'objet aléatoire
    object_x += random.randint(-5, 5)
    object_y += random.randint(-5, 5)

    # Gestion des collisions avec les bords de la carte
    if object_x < 0:
        object_x = 0
    elif object_x > window_width - object_width:
        object_x = window_width - object_width
    if object_y < 0:
        object_y = 0
    elif object_y > window_height - object_height:
        object_y = window_height - object_height

    # Affichage de la carte et de l'objet
    window.blit(map_image, (0, 0))
    window.blit(object_image, (object_x, object_y))

    # Rafraîchissement de l'écran
    pygame.display.flip()

# Fermeture de la fenêtre pygame
pygame.quit()
