class Node:
    def __init__(self, pos: tuple, g_cost: float, h_cost: float, direction=None):
        self.pos = pos
        self.g_cost = g_cost
        self.h_cost = h_cost
        self.f_cost = g_cost + h_cost
        self.is_corner = False
        self.parent = None
        self.direction = direction

    def __lt__(self, other):
        return self.f_cost < other.f_cost

class AStar:

    def __init__(self, map_grid):
        self.open = []
        self.closed = []
        self.map_grid = map_grid
        self.count_path = 0

    def search(self, start_node, goal_node):
        self.open.append(start_node)

        while self.open:
            self.open.sort() 
            current_node = self.open.pop(0)
            self.closed.append(current_node)

            if current_node.pos == goal_node.pos:
                return self.reconstruct_path(current_node, start_node, goal_node)
            
            neighbors = self.get_neighbors(current_node)
            for neighbor_pos, direction in neighbors:
                neighbor = Node(pos=neighbor_pos, g_cost=0, h_cost=0, direction=direction)

                if any(closed_node.pos == neighbor.pos for closed_node in self.closed):
                    continue

                g_cost = current_node.g_cost + 1
                h_cost = self.heuristic(neighbor, goal_node)

            
                if any(open_node.pos == neighbor.pos and open_node.f_cost <= g_cost + h_cost for open_node in self.open):
                    continue

                self.update_node(neighbor, g_cost, h_cost, current_node)
                self.open.append(neighbor)

        return None 

    def get_neighbors(self, node):
        directions = [(1, 0, 'E'), (0, 1, 'S'), (-1, 0, 'W'), (0, -1, 'N')]
        neighbors = []

        for dx, dy, direction in directions:
            neighbor_pos = (node.pos[0] + dx, node.pos[1] + dy)

            if (0 <= neighbor_pos[0] < len(self.map_grid[0]) and
                0 <= neighbor_pos[1] < len(self.map_grid) and
                self.map_grid[neighbor_pos[1]][neighbor_pos[0]] != '#'):
                neighbors.append((neighbor_pos, direction))

        return neighbors

    def heuristic(self, node, goal):
        return abs(node.pos[0] - goal.pos[0]) + abs(node.pos[1] - goal.pos[1])

    def reconstruct_path(self, node, start_node, goal_node):
        path = []
        current = node
        previous_direction = None

        while current:
            if current.pos == goal_node.pos:  
                path.append((current.pos, False))
            else:
                if current.direction == previous_direction:
                    path.append((current.pos, False))  
                    self.count_path += 1 
                else:
                    path.append((current.pos, True))  
                    self.count_path += 1000 + 1 

            previous_direction = current.direction
            current = current.parent

        return path[::-1]  
    
    def update_node(self, node, g_cost, h_cost, parent_node):
       
        turn_penalty = 100 if parent_node.direction != node.direction else 0  
        node.g_cost = g_cost + turn_penalty  
        node.h_cost = h_cost 
        node.f_cost = node.g_cost + node.h_cost
        node.parent = parent_node


def find_symbol(symbol, grid):
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == symbol:
                return (x, y)
    return None


def print_grid(grid, path):
    grid_copy = [row[:] for row in grid]

    for pos, is_turn in path:
        x, y = pos
        if grid_copy[y][x] not in ('S', 'E'):
            grid_copy[y][x] = '.' if not is_turn else 'o' 

    for row in grid_copy:
        print("".join(row))


with open("input.txt") as f:
    data = [list(line.strip()) for line in f.readlines()]

start_pos = find_symbol("S", data)
goal_pos = find_symbol("E", data)

if not start_pos or not goal_pos:
    print("Start or goal position not found in the input.")
else:
    start_direction = 'E' 
    astar = AStar(data)
    start_node = Node(start_pos, g_cost=0, h_cost=0, direction=start_direction)
    goal_node = Node(goal_pos, g_cost=0, h_cost=0)

    path = astar.search(start_node, goal_node)

    if path:
        print(f"Path found! Total steps: {len(path)}")
        for step in path:
            print(f"Position: {step[0]}, Turn: {step[1]}")

        print("\nGrid with path:")
        print_grid(data, path)
    else:
        print("No path found.")

    print(astar.count_path)