#import#
import tkinter as tk
import random
from robots import PinkPoint, PurplePoint  # import the classes from the points module
from tkinter import ttk

class Grid:
    #
    #
    def __init__(self, width, height, square_size, window):
        self.width = width
        self.height = height
        self.square_size = square_size
        self.grid = [[0 for _ in range(width)] for _ in range(height)]
        self.canvas = tk.Canvas(window, width=width*square_size, height=height*square_size)
        self.canvas.pack(side=tk.LEFT)
        self.canvas.pack()
        self.draw_grid()
        self.draw_square(0, 0, "blue") #position et couleur du carré
        self.draw_square(15, 15, "red") #position et couleur du carré
        self.purple_point = PurplePoint(self, 0, 0)  # create an instance of PurplePoint
        self.pink_point = PinkPoint(self, 15, 15)  # create an instance of PinkPoint
        
                # Create a table to show battery percentage
        self.battery_table = ttk.Treeview(window, columns=('Robot', 'Battery (%)'), show='headings')
        self.battery_table.heading('Robot', text='Robot')
        self.battery_table.heading('Battery (%)', text='Battery (%)')
        self.battery_table.insert('', 'end', values=('PurplePoint', PurplePoint(self, 0, 0).battery.get_energy_level()))
        self.battery_table.insert('', 'end', values=('PinkPoint', PinkPoint(self, 15, 15).battery.get_energy_level()))
        
        self.battery_table.pack(side=tk.RIGHT, padx=10, pady=10)
    #
    #     
    def draw_square(self, x, y, color):
        x_pixel = x * self.square_size
        y_pixel = y * self.square_size
        self.canvas.create_rectangle(x_pixel, y_pixel, x_pixel + self.square_size, y_pixel + self.square_size, fill=color)
    #
    # 
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
        purple_point.move(1,0)

#
#
def generate_grid(width, height, square_size, window):
        # Create a canvas with a frame to center the grid
    frame = ttk.Frame(window)
    frame.pack(fill=tk.BOTH, expand=tk.YES)
    canvas = tk.Canvas(frame, width=width*square_size, height=height*square_size)
    canvas.pack(expand=tk.YES)
    
    # Create the grid inside the canvas
    grid = Grid(width, height, square_size, canvas)
    window_width = window.winfo_width()
    window_height = window.winfo_height()
    canvas_width = width * square_size
    canvas_height = height * square_size
    
    # Calculate the x and y offsets to center the grid
    if window_width > canvas_width:
        x_offset = (window_width - canvas_width) // 2
        canvas.place(x=x_offset)
    if window_height > canvas_height:
        # Calculate the y offset to center the grid
        y_offset = (window_height - canvas_height) // 2
        canvas.place(y=y_offset)
        
    return grid


# Example usage with Tkinter
grid_width = 16
grid_height = 16
square_size = 32



root = tk.Tk()
root.title("Agents Game")
grid = generate_grid(grid_width, grid_height, square_size, root)

root.mainloop()