class PurplePoint:
    def __init__(self, grid, x, y):
        self.grid = grid
        self.x = x
        self.y = y
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
        self.grid.draw_square(self.x, self.y, "gray")


class PinkPoint:
    def __init__(self, grid, x, y):
        self.grid = grid
        self.x = x
        self.y = y
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
        self.grid.draw_square(self.x, self.y, "gray")
