#battery.py

import time
#création de la batterie
class Battery:
    def __init__(self, energy):
        self.energy = min(max(0, energy), 50)

    #variable qui defini l'énergie
    def get_energy_level(self):
        return self.energy
   
    #variable qui utilise la batterie
    def use_battery(self, amount):
        self.energy -= amount
        if self.energy <= 0:
            print("La batterie est épuisée.")
            self.energy = 0

    #variable qui fais diminuer la batterie en fonction du temps
    def decrease_energy_over_time(self, rate, time_elapsed):
        self.energy -= rate * time_elapsed
        if self.energy <= 0:
            print("La batterie est épuisée.")
            self.energy = 0

battery = Battery(100)
print("Niveau d'énergie initial :", battery.get_energy_level())

battery.decrease_energy_over_time(1, 10)
print("Niveau d'énergie après décrémentation :", battery.get_energy_level())