#warehouse.py

import random
import math

class Warehouse:
    def init(self, position, items):
    self.position = position
    self.items = items
    
    def take_item(self, item_type, quantity):
    # Fonction pour prendre un certain nombre d'articles d'un type donné
        if item_type in self.items and self.items[item_type] >= quantity:
            self.items[item_type] -= quantity
            return True
        else:
            return False

    def put_item(self, item_type, quantity):
        # Fonction pour déposer un certain nombre d'articles d'un type donné
        if item_type in self.items:
            self.items[item_type] += quantity
        else:
            self.items[item_type] = quantity
        return True