import time

# Création de la batterie
class Battery:
    def __init__(self, energy):
        # Initialisation de l'énergie en prenant en compte les bornes (0, 50)
        self.energy = min(max(0, energy), 50)

    # Méthode qui permet d'obtenir le niveau d'énergie actuel
    def get_energy_level(self):
        return self.energy

    # Méthode qui permet d'utiliser la batterie en spécifiant la quantité d'énergie utilisée
    def use_battery(self, amount):
        if amount > self.energy:
            # Si la quantité d'énergie à utiliser est supérieure au niveau d'énergie actuel,
            # la batterie est complètement déchargée
            self.energy = 0
            print("La batterie est épuisée.")
        else:
            # Sinon, la quantité d'énergie est déduite du niveau d'énergie actuel
            self.energy -= amount

    # Méthode qui fait diminuer le niveau d'énergie de la batterie en fonction du temps et du taux de décharge
    def decrease_energy_over_time(self, rate, time_elapsed):
        self.energy -= rate * time_elapsed
        # Le niveau d'énergie est borné entre 0 et 50
        self.energy = max(0, self.energy)
        if self.energy <= 0:
            # Si le niveau d'énergie atteint 0, la batterie est épuisée
            print("La batterie est épuisée.")
            self.energy = 0

# Exemple d'utilisation de la classe Battery
battery = Battery(100)
print("Niveau d'énergie initial :", battery.get_energy_level())

battery.use_battery(5)
print("Niveau d'énergie après décrémentation :", battery.get_energy_level())

