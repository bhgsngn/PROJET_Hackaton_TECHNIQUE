import random
import math


class Mission:
    def init(self, source, target, item_type, quantity):

        self.source = source
        self.target = target
        self.item_type = item_type
        self.quantity = quantity
        self.status = "En attente"

    def update_status(self, agent):
        # Fonction pour mettre à jour le statut de la mission
        if self.status == "En attente":
            if agent.cargo_capacity >= self.quantity:
                if self.source.take_item(self.item_type, self.quantity):
                    self.status = "En cours"
                    return True
        elif self.status == "En cours":
            if self.target.put_item(self.item_type, self.quantity):
                self.status = "Terminée"
                return True
        return False
