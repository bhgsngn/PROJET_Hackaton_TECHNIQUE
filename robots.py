from battery import Battery
import random

class PurplePoint:
    def __init__(self, grid, blue_square_x, blue_square_y):
        self.grid = grid
        self.battery = Battery(50)
        self.color = "purple"
        self.x = blue_square_x
        self.y = blue_square_y
        self.draw()

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

    def draw(self):
        self.grid.canvas.create_oval(self.x * self.grid.square_size + 2, self.y * self.grid.square_size + 2, 
            (self.x+1) * self.grid.square_size - 2, (self.y+1) * self.grid.square_size - 2, fill=self.color)

    def erase(self):
        self.grid.canvas.create_rectangle(self.x * self.grid.square_size, self.y * self.grid.square_size, 
            (self.x+1) * self.grid.square_size, (self.y+1) * self.grid.square_size, fill="red")