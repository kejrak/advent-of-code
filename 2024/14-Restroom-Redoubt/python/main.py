from PIL import Image, ImageDraw

def parse_line(line):
    p, v = line.split()
    px, py = map(int, p[2:].split(","))
    vx, vy = map(int, v[2:].split(","))
    return px, py, vx, vy

def calculate_new_position(px, py, vx, vy, t, W, H):
    nx = (px + t * vx) % W
    ny = (py + t * vy) % H
    return nx, ny

def classify_position(nx, ny, W, H):
    if nx == W // 2 or ny == H // 2:
        return None
    if nx < W // 2 and ny < H // 2:
        return 0
    if nx > W // 2 and ny < H // 2:
        return 1
    if nx < W // 2 and ny > H // 2:
        return 2
    return 3

def process_data(data, t, W, H):
    ans = [0, 0, 0, 0]
    for line in data:
        if not line.strip():
            continue
        px, py, vx, vy = parse_line(line)
        nx, ny = calculate_new_position(px, py, vx, vy, t, W, H)
        quadrant = classify_position(nx, ny, W, H)
        if quadrant is not None:
            ans[quadrant] += 1
    return ans

def initialize_grid(W, H):
    return [[0 for _ in range(W)] for _ in range(H)]

def update_grid(grid, positions):
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            grid[y][x] = 0  # Reset grid
    for x, y in positions:
        grid[y][x] = 1 

def grid_to_image(grid, cell_size=50):
    H, W = len(grid), len(grid[0])
    img = Image.new("RGB", (W * cell_size, H * cell_size), "white")
    draw = ImageDraw.Draw(img)
    
    for y in range(H):
        for x in range(W):
            if grid[y][x] == 1:  # Point exists
                x0, y0 = x * cell_size, y * cell_size
                x1, y1 = x0 + cell_size, y0 + cell_size
                draw.rectangle([x0, y0, x1, y1], fill="black")
    
    return img


def part_one(filename, t, W, H):
    with open(filename) as f:
        data = f.read().splitlines()
    ans = process_data(data, t, W, H)
    print(ans[0] * ans[1] * ans[2] * ans[3])

def part_two(filename, t, W, H):
    with open(filename) as f:
        data = f.read().splitlines()

    points = [parse_line(line) for line in data if line.strip()]

    grid = initialize_grid(W, H)
    positions = [calculate_new_position(px, py, vx, vy, 7371, W, H) for px, py, vx, vy in points]  
    update_grid(grid, positions)

    img = grid_to_image(grid, cell_size=50)
    img.save(f"simulation/christmas_tree.png")

if __name__ == "__main__":
    W, H = 101, 103
    filename = "input.txt"
    print("Part One:")
    part_one(filename, 100, W, H)

    print("Part Two:")
    part_two(filename, 10, W, H)
    print("Printed")
