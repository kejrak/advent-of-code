def robot(symbol, grid):
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == symbol:
                return x, y
    return -1, -1


def boxes(symbol, grid):
    count = 0
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == symbol:
                count += 100 * y + x

    return count
    
def move_robot(robot_pos, moves, grid):
    directions = {
        ">": (1, 0),
        "<": (-1, 0),
        "^": (0, -1),
        "v": (0, 1)
    }

    print(grid)

    x, y = robot_pos
    grid = [list(row) for row in grid]

    for move in moves:
        if move in directions:
            dx, dy = directions[move]
            nx, ny = x + dx, y + dy

        if 0 <= ny < len(grid) and 0 <= nx < len(grid[ny]):
            if grid[ny][nx] == "#":
                continue
            elif grid[ny][nx] == "O":
                positions = []
                temp_x, temp_y = nx, ny

                while 0 <= temp_y < len(grid) and 0 <= temp_x < len(grid[temp_y]) and grid[temp_y][temp_x] == "O":
                    positions.append((temp_x, temp_y))
                    temp_x, temp_y = temp_x + dx, temp_y + dy

            
                if 0 <= temp_y < len(grid) and 0 <= temp_x < len(grid[temp_y]) and grid[temp_y][temp_x] == ".":
                    for px, py in reversed(positions):
                        grid[py + dy][px + dx] = "O"  
                        grid[py][px] = "."
                    grid[temp_y][temp_x] = "O"  
                    grid[y][x] = "." 
                    grid[ny][nx] = "@" 
                    x, y = nx, ny
            else:
                grid[y][x], grid[ny][nx] = ".", "@"
                x, y = nx, ny

    return grid

def print_grid(grid):
    for row in grid:
        print("".join(row))
    print()

with open("input.txt") as f:
    data = f.read().strip()

grid = data.split("\n\n")[0].splitlines()
moves = data.split("\n\n")[1]

robot_pos = robot("@", grid)
factory = move_robot(robot_pos, moves, grid)

print(boxes("O", factory))
