import random
import math

class Agent:
    def __init__(self, speed, battery, cargo_capacity):
        self.speed = speed
        self.battery = battery
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
        self.battery -= 1
    
    def move_a_star(self, target):
        # implémentation de l'algorithme A* pour trouver le chemin le plus court vers la cible
        pass
        
    def move_memorized(self, path):
        # déplacement en suivant un trajet mémorisé
        if len(path) > 0:
            self.position = path.pop(0)
            self.battery -= 1