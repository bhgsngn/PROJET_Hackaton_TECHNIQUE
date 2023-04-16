from battery import Battery
import random

class PurplePoint:
    def __init__(self, grid, x=0, y=0):
        self.grid = grid
        self.battery = Battery(50)
        self.shape = self.grid.canvas.create_oval(10, 10, 30, 30, fill="purple")
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        self.grid.canvas.move(self.shape, dx*self.grid.square_size, dy*self.grid.square_size)
        self.battery.use_battery(1)

    def draw(self):
        self.grid.canvas.create_oval(self.x * self.grid.square_size + 2, self.y * self.grid.square_size + 2, 
            (self.x+1) * self.grid.square_size - 2, (self.y+1) * self.grid.square_size - 2, fill="purple")

    def erase(self):
        self.grid.canvas.create_rectangle(self.x * self.grid.square_size, self.y * self.grid.square_size, 
            (self.x+1) * self.grid.square_size, (self.y+1) * self.grid.square_size, fill="blue")


class PinkPoint:
    def __init__(self, grid, x=15, y=15):
        self.grid = grid
        self.battery = Battery(50)
        self.shape = self.grid.canvas.create_oval(10, 10, 30, 30, fill="pink")
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        self.grid.canvas.move(self.shape, dx*self.grid.square_size, dy*self.grid.square_size)
        self.battery.use_battery(1)


    def draw(self):
        self.grid.canvas.create_oval(self.x * self.grid.square_size + 2, self.y * self.grid.square_size + 2, 
            (self.x+1) * self.grid.square_size - 2, (self.y+1) * self.grid.square_size - 2, fill="pink")

    def erase(self):
        self.grid.canvas.create_rectangle(self.x * self.grid.square_size, self.y * self.grid.square_size, 
            (self.x+1) * self.grid.square_size, (self.y+1) * self.grid.square_size, fill="red")
