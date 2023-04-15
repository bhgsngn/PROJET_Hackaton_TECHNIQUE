class PurplePoint:
    def __init__(self, grid, blue_square_x, blue_square_y):
        self.grid = grid
        self.x = blue_square_x
        self.y = blue_square_y
        self.color = "purple"
        self.draw()

    def move(self, dx, dy):
        new_x = self.x + dx
        new_y = self.y + dy
        if self.grid.is_valid(new_x, new_y):
            self.erase()
            self.x = new_x
            self.y = new_y
            self.draw()

    def draw(self):
        self.grid.draw_square(self.x, self.y, self.color)

    def erase(self):
        self.grid.draw_square(self.x, self.y, "blue")


class PinkPoint:
    def __init__(self, grid, red_square_x, red_square_y):
        self.grid = grid
        self.x = red_square_x
        self.y = red_square_y
        self.color = "pink"
        self.draw()

    def move(self, dx, dy):
        new_x = self.x + dx
        new_y = self.y + dy
        if self.grid.is_valid(new_x, new_y):
            self.erase()
            self.x = new_x
            self.y = new_y
            self.draw()

    def draw(self):
        self.grid.draw_square(self.x, self.y, self.color)

    def erase(self):
        self.grid.draw_square(self.x, self.y, "red")
