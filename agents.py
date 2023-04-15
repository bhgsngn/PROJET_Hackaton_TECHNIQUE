class Agent:
    def __init__(self, speed, battery=100, cargo_capacity=10):
        self.speed = speed
        self.battery = battery
        self.cargo_capacity = cargo_capacity
        self.position = (0, 0)
        self.shape = None

    def move_random(self):
        direction = random.choice(["N", "E", "S", "W"])
        if direction == "N":
            self.position = (self.position[0], self.position[1] + self.speed)
        elif direction == "E":
            self.position = (self.position[0] + self.speed, self.position[1])
        elif direction == "S":
            self.position = (self.position[0], self.position[1] - self.speed)
        elif direction == "W":
            self.position = (self.position[0] - self.speed, self.position[1])
        self.battery -= 1

        # Update agent shape on the grid
        self.canvas.coords(self.shape, self.position[0]*self.square_size, self.position[1]*self.square_size)

    def move_a_star(self, target):
        open_list = [self.position]
        costs = {self.position: {'g': 0, 'h': self.manhattan_distance(self.position, target)}}
        while open_list:
            current = min(open_list, key=lambda x: costs[x]['g'] + costs[x]['h'])
            if current == target:
                return self.reconstruct_path(current, costs)
            open_list.remove(current)
            closed_list = [current]
            for neighbor in self.get_neighbors(current):
                if neighbor in closed_list:
                    continue
                g = costs[current]['g'] + 1
                h = self.manhattan_distance(neighbor, target)
                if neighbor in open_list:
                    if costs[neighbor]['g'] <= g:
                        continue
                open_list.append(neighbor)
                costs[neighbor] = {'g': g, 'h': h}
        return None

    def manhattan_distance(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def reconstruct_path(self, current, costs):
        path = [current]
        while current != self.position:
            neighbors = self.get_neighbors(current)
            current = min(neighbors, key=lambda x: costs[x]['g'])
            path.append(current)
        path.reverse()
        return path

    def move_memorized(self, path):
        if self.battery > 0 and len(path) > 0:
            self.position = path.pop(0)
            self.battery -= 1

            # Update agent shape on the grid
            self.canvas.coords(self.shape, self.position[0]*self.square_size, self.position[1]*self.square_size)

    def draw(self, canvas, square_size):
        # Create a circle shape for the agent
        x_pixel = self.position[0] * square_size
        y_pixel = self.position[1] * square_size
        self.shape = canvas.create_oval(x_pixel, y_pixel, x_pixel + square_size, y_pixel + square_size, fill="green")
        self.canvas = canvas
        self.square_size = square_size
