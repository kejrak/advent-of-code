from collections import deque

def bfs(grid):
    rows, cols = len(grid), len(grid[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)] 
    start, end = (0, 0), (rows - 1, cols - 1)

    if grid[start[0]][start[1]] == '#' or grid[end[0]][end[1]] == '#':
        return -1
    
    queue = deque([(0, 0, 0)]) 
    visited = set()
    visited.add((0, 0))

    while queue:
        row, col, steps = queue.popleft()

        if (row, col) == end:
            return steps

        for dr, dc in directions:
            nr, nc = row + dr, col + dc

            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and grid[nr][nc] == '.':
                queue.append((nr, nc, steps + 1))
                visited.add((nr, nc))

    return -1 


with open("input.txt") as f:
    data = f.read().splitlines()


grid_size = 71
grid = [['.' for _ in range(grid_size)] for _ in range(grid_size)]

def main():
    for i in range(1025, len(data)):
        for coord in data[:i]:
            x, y = map(int, coord.split(','))
            grid[y][x] = '#'
        
        if bfs(grid) == -1:
            print(coord)
            return

main()


