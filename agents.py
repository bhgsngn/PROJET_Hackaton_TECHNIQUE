import random
import math
import battery
import color_detector

class Agent:
#créeation d'une classe agent
    def __init__(self, speed, Battery, cargo_capacity):
        self.speed = speed
        self.Battery = Battery
        self.cargo_capacity = cargo_capacity
        self.position = (0, 0)
        self.closed_list = []

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
        self.Battery -= 1

    def move_a_star(self, target):
        # Initialiser la liste des cases ouvertes avec la case de départ
        open_list = [self.position]
        # Initialiser le dictionnaire des coûts avec la case de départ
        costs = {self.position: {
            'g': 0, 'h': self.manhattan_distance(self.position, target)}}
        # Boucle jusqu'à ce que toutes les cases aient été vues ou que la cible ait été atteinte
        while open_list:
            # Trouver la case avec le coût f le plus bas (f = g + h)
            current = min(
                open_list, key=lambda x: costs[x]['g'] + costs[x]['h'])
            # Si c'est la cible, retourner le chemin
            if current == target:
                return self.reconstruct_path(target, costs)
            # Sinon, marquer la case comme fermée
            open_list.remove(current)
            self.closed_list.append(current)
            # Pour chaque case voisine
            for neighbor in self.get_neighbors(current):
                # Si elle est fermée, passer
                if neighbor in self.closed_list:
                    continue
                # Calculer les nouveaux coûts g et h
                # On suppose ici que tous les déplacements coûtent 1
                g = costs[current]['g'] + 1
                h = self.manhattan_distance(neighbor, target)
                # Si la case voisine est déjà dans la liste ouverte
                if neighbor in open_list:
                    # Si les nouveaux coûts sont plus élevés, passer
                    if costs[neighbor]['g'] <= g:
                        continue
                # Sinon, ajouter la case voisine à la liste ouverte
                open_list.append(neighbor)
                costs[neighbor] = {'g': g, 'h': h}
        # Si aucun chemin n'a été trouvé, retourner None
        return None

    def manhattan_distance(a, b):
        # Fonction pour calculer la distance de Manhattan entre deux cases
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def reconstruct_path(self, target, costs):
        # Fonction pour reconstruire le chemin à partir du dictionnaire des coûts
        path = [target]
        current = target
        while current != self.position:
            # Trouver la case voisine avec le coût g le plus faible
            neighbors = self.get_neighbors(current)
            neighbor = min(neighbors, key=lambda x: costs[x]['g'])
            # Ajouter la case voisine au chemin
            path.append(neighbor)
            current = neighbor
            # Renverser le chemin pour qu'il soit dans l'ordre
            path.reverse()
        return path

    def move_memorized(self, path):
        # déplacement en suivant un trajet mémorisé
        if len(path) > 0:
            self.position = path.pop(0)
            self.Battery -= 1