import random
import math
import battery.py

class Agent:
    #créeation d'une classe agent
    def __init__(self, speed, Battery, cargo_capacity):
        self.speed = speed
        self.Battery = Battery
        self.cargo_capacity = cargo_capacity
        self.position = (0, 0)
    
    def move_random(self):
        # déplacement aléatoire dans une direction aléatoire
        direction = random.choice(["N", "E", "S", "W"])
        if direction == "N":
            self.position = (self.position[0], self.position[1] + self.speed)
        elif direction == "E":
            self.position = (self.position[0] + self.speed, self.position[1])
        elif direction == "S":
            self.position = (self.position[0], self.position[1] - self.speed)
        elif direction == "W":
            self.position = (self.position[0] - self.speed, self.position[1])
        
    
    def move_a_star(self, target):
        # implémentation de l'algorithme A* pour trouver le chemin le plus court vers la cible
        pass
        
    def move_memorized(self, path):
        # déplacement en suivant un trajet mémorisé
        if len(path) > 0:
            self.position = path.pop(0)
            