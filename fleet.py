#fleet.py

import random
import math

class Fleet:
    def __init__(self, agents, missions, warehouses):
        self.agents = agents
        self.missions = missions
        self.warehouses = warehouses

    def assign_missions(self):
        # Fonction pour assigner des missions aux agents
        for mission in self.missions:
            if mission.status == "En attente":
                for agent in self.agents:
                    if agent.battery > 0:
                        path = agent.move_a_star(mission.source.position)
                        if path:
                            agent.move_memorized(path)
                            if mission.update_status(agent):
                                break
