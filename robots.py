from battery import Battery
import random

class PurplePoint:
    def __init__(self, canvas, battery):
        self.canvas = canvas
        self.battery = Battery(50)
        self.shape = self.canvas.create_oval(10, 10, 30, 30, fill="purple")
        self.x = random.randint(0, 400)
        self.y = random.randint(0, 400)

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        self.canvas.move(self.shape, dx, dy)
        self.battery.use_battery(1)

    def draw(self):
        self.grid.canvas.create_oval(self.x * self.grid.square_size + 2, self.y * self.grid.square_size + 2, 
            (self.x+1) * self.grid.square_size - 2, (self.y+1) * self.grid.square_size - 2, fill=self.color)

    def erase(self):
        self.grid.canvas.create_rectangle(self.x * self.grid.square_size, self.y * self.grid.square_size, 
            (self.x+1) * self.grid.square_size, (self.y+1) * self.grid.square_size, fill="blue")


class PinkPoint:
    def __init__(self, canvas, battery):
        self.canvas = canvas
        self.battery = Battery(50)
        self.shape = self.canvas.create_oval(10, 10, 30, 30, fill="pink")
        self.x = random.randint(0, 400)
        self.y = random.randint(0, 400)

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        self.canvas.move(self.shape, dx, dy)
        self.battery.use_battery(1)


    def draw(self):
        self.grid.canvas.create_oval(self.x * self.grid.square_size + 2, self.y * self.grid.square_size + 2, 
            (self.x+1) * self.grid.square_size - 2, (self.y+1) * self.grid.square_size - 2, fill=self.color)

    def erase(self):
        self.grid.canvas.create_rectangle(self.x * self.grid.square_size, self.y * self.grid.square_size, 
            (self.x+1) * self.grid.square_size, (self.y+1) * self.grid.square_size, fill="red")


