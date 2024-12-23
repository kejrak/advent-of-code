import heapq

def find_symbol(symbol, grid):
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == symbol:
                return (x, y)
    return None

with open("input.txt") as f:
    data = [list(line.strip()) for line in f.readlines()]

start_pos = find_symbol("S", data)
goal_pos = find_symbol("E", data)

cost, path = dijkstra(data, start_pos, goal_pos)
print("Cost:", cost)
print("Path:", path)
