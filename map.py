import tkinter as tk
import random
from robots import PinkPoint, PurplePoint  # import the classes from the points module

class Grid:
    def __init__(self, width, height, square_size, window):
        self.width = width
        self.height = height
        self.square_size = square_size
        self.grid = [[0 for _ in range(width)] for _ in range(height)]#map.py

import tkinter as tk
import random
from robots import PinkPoint, PurplePoint  # import the classes from the points module

class Grid:
    def __init__(self, width, height, square_size, window):
        self.width = width
        self.height = height
        self.square_size = square_size
        self.grid = [[0 for _ in range(width)] for _ in range(height)]
        self.canvas = tk.Canvas(window, width=width*square_size, height=height*square_size)
        self.canvas.pack()
        self.draw_grid()
        self.draw_square(0, 0, "blue") #position et couleur du carré
        self.draw_square(15, 15, "red") #position et couleur du carré
        self.purple_point = PurplePoint(self, 0, 0)  # create an instance of PurplePoint
        self.pink_point = PinkPoint(self, 15, 15)  # create an instance of PinkPoint
        
    def draw_square(self, x, y, color):
        x_pixel = x * self.square_size
        y_pixel = y * self.square_size
        self.canvas.create_rectangle(x_pixel, y_pixel, x_pixel + self.square_size, y_pixel + self.square_size, fill=color)
    
    def draw_grid(self):
        for y in range(self.height):
            for x in range(self.width):
                
                # Ajout de carrés noirs aléatoirement
                if random.random() < 0.1 and self.grid[y][x] == 0:
                    self.grid[y][x] = 1
                    self.canvas.create_rectangle(x*self.square_size, y*self.square_size, (x+1)*self.square_size, (y+1)*self.square_size, fill="black")
                # Ajout de carrés jaunes aléatoirement
                elif random.random() < 0.025 and self.grid[y][x] == 0 and not any(self.grid[i][j] == 2 for i in range(max(0, y-1), min(self.height, y+2)) for j in range(max(0, x-1), min(self.width, x+2))):
                    self.grid[y][x] = 2
                    self.canvas.create_rectangle(x*self.square_size, y*self.square_size, (x+1)*self.square_size, (y+1)*self.square_size, fill="yellow")
                
                elif random.random() < 0.05 and self.grid[y][x] == 0 and not any(self.grid[i][j] == 3 for i in range(max(0, y-1), min(self.height, y+2)) for j in range(max(0, x-1), min(self.width, x+2))):
                    self.grid[y][x] = 3
                    self.canvas.create_rectangle(x*self.square_size, y*self.square_size, (x+1)*self.square_size, (y+1)*self.square_size, fill="chocolate4")
                    
                # Ajout de carrés gris pour le reste de la grille
                else:
                    self.canvas.create_rectangle(x*self.square_size, y*self.square_size, (x+1)*self.square_size, (y+1)*self.square_size, fill="gray")

def generate_grid(width, height, square_size, window):
    grid = Grid(width, height, square_size, window)
    return grid



# Example usage with Tkinter
grid_width = 16
grid_height = 16
square_size = 32

root = tk.Tk()
root.title("Agents Game")
grid = generate_grid(grid_width, grid_height, square_size, root)

# Set window size to 800x600 pixels
window_width = 800
window_height = 600
root.geometry(f"{window_width}x{window_height}")

root.mainloop()

        self.canvas = tk.Canvas(window, width=width*square_size, height=height*square_size)
        self.canvas.pack()
        self.draw_grid()
        self.draw_square(0, 0, "blue") #position et couleur du carré
        self.draw_square(15, 15, "red") #position et couleur du carré
        self.purple_point = PurplePoint(self, 0, 0)  # (self, position)
        self.pink_point = PinkPoint(self, 15, 15)  # 
        
    def draw_square(self, x, y, color):
        x_pixel = x * self.square_size
        y_pixel = y * self.square_size
        self.canvas.create_rectangle(x_pixel, y_pixel, x_pixel + self.square_size, y_pixel + self.square_size, fill=color)
    
    def draw_grid(self):
        for y in range(self.height):
            for x in range(self.width):
                # Ajout de carrés noirs aléatoirement
                if random.random() < 0.1 and self.grid[y][x] == 0:
                    self.grid[y][x] = 1
                    self.canvas.create_rectangle(x*self.square_size, y*self.square_size, (x+1)*self.square_size, (y+1)*self.square_size, fill="black")
                # Ajout de carrés jaunes aléatoirement
                elif random.random() < 0.025 and self.grid[y][x] == 0 and not any(self.grid[i][j] == 2 for i in range(max(0, y-1), min(self.height, y+2)) for j in range(max(0, x-1), min(self.width, x+2))):
                    self.grid[y][x] = 2
                    self.canvas.create_rectangle(x*self.square_size, y*self.square_size, (x+1)*self.square_size, (y+1)*self.square_size, fill="yellow", tags="balise")
                # Ajout de carrés gris pour le reste de la grille
                else:
                    self.canvas.create_rectangle(x*self.square_size, y*self.square_size, (x+1)*self.square_size, (y+1)*self.square_size, fill="gray")

def generate_grid(width, height, square_size, window):
    grid = Grid(width, height, square_size, window)
    return grid

# Example usage with Tkinter
grid_width = 16
grid_height = 16
square_size = 32

root = tk.Tk()
root.title("Grid Example")
grid = generate_grid(grid_width, grid_height, square_size, root)

# Set window size to 800x600 pixels
window_width = 800
window_height = 700
root.geometry(f"{window_width}x{window_height}")

root.mainloop()


