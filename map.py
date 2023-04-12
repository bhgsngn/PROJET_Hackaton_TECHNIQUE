import tkinter as tk

class Grid:
    def __init__(self, width, height, square_size, window):
        self.width = width
        self.height = height
        self.square_size = square_size
        self.grid = [[0 for _ in range(width)] for _ in range(height)]
        self.canvas = tk.Canvas(window, width=width*square_size, height=height*square_size)
        self.canvas.pack()
        self.draw_grid()

    def draw_grid(self):
        for y in range(self.height):
            for x in range(self.width):
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

