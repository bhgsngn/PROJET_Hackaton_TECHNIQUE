from battery import Battery
import random


#classe point violet
class PurplePoint:
    def __init__(self, grid, blue_square_x, blue_square_y):
        self.grid = grid
        self.battery = Battery(50)
        self.color = "purple"
        self.x = blue_square_x
        self.y = blue_square_y
        self.draw()
        self.charge_battery()

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        self.grid.canvas.move(self.shape, dx*self.grid.square_size, dy*self.grid.square_size)
        self.battery.use_battery(1)

    def draw(self):
        self.grid.canvas.create_oval(self.x * self.grid.square_size + 2, self.y * self.grid.square_size + 2, 
            (self.x+1) * self.grid.square_size - 2, (self.y+1) * self.grid.square_size - 2, fill=self.color)

    def erase(self):
        self.grid.canvas.create_rectangle(self.x * self.grid.square_size, self.y * self.grid.square_size, 
            (self.x+1) * self.grid.square_size, (self.y+1) * self.grid.square_size, fill="blue")
        
    def charge_battery(self):
        if self.grid.grid[self.x][self.y] == 2:
            # Si la case sur laquelle se trouve le point violet est une case jaune,
            # la batterie est rechargée de 20 unités
            self.battery.energy = min(self.battery.energy + 20, 50)
            print("Batterie rechargée. Niveau d'énergie actuel :", self.battery.get_energy_level())


#classe point rose 
class PinkPoint:
    def __init__(self, grid, red_square_x, red_square_y):
        self.grid = grid
        self.battery = Battery(50)
        self.color = "pink"
        self.x = red_square_x
        self.y = red_square_y
        self.draw()
        
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        self.grid.canvas.move(self.shape, dx*self.grid.square_size, dy*self.grid.square_size)
        self.battery.use_battery(1)
        self.draw()
        self.charge_battery()

    def draw(self):
        self.grid.canvas.create_oval(self.x * self.grid.square_size + 2, self.y * self.grid.square_size + 2, 
            (self.x+1) * self.grid.square_size - 2, (self.y+1) * self.grid.square_size - 2, fill=self.color)

    def erase(self):
        self.grid.canvas.create_rectangle(self.x * self.grid.square_size, self.y * self.grid.square_size, 
            (self.x+1) * self.grid.square_size, (self.y+1) * self.grid.square_size, fill="red")
        
    def charge_battery(self):
        if self.grid.grid[self.x][self.y] == 2:
            # Si la case sur laquelle se trouve le point violet est une case jaune,
            # la batterie est rechargée de 20 unités
            self.battery.energy = min(self.battery.energy + 20, 50)
            print("Batterie rechargée. Niveau d'énergie actuel :", self.battery.get_energy_level())