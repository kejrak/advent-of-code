import time
def get_guard_position(guard: str, grid: list[list[str]]):
    for row_index, row in enumerate(grid):
        if guard in row:
            col_index = row.index(guard)
            return row_index, col_index
    return None


def rotate(current_direction_index: int) -> int:
    return (current_direction_index + 1) % 4


def traverse(guard: str, grid: list[list[str]]):
    directions = [
        (-1, 0),  # up
        (0, 1),   # right
        (1, 0),   # down
        (0, -1)   # left
    ]
    current_direction_index = 0
    moves = 1

    guard_pos = get_guard_position(guard, grid)
    if guard_pos is None:
        return moves, []

    row, col = guard_pos

    visited = [(row, col)]
    moved = [(row, col)]

    while True:
        dr, dc = directions[current_direction_index]
        new_row, new_col = row + dr, col + dc

        if not (0 <= new_row < len(grid) and 0 <= new_col < len(grid[0])):
            break

        if grid[new_row][new_col] == '#':
            current_direction_index = rotate(current_direction_index)
        else:
            row, col = new_row, new_col
            moved.append((row, col))
            if (row, col) not in visited:
                moves += 1
                visited.append((row, col))

    return moves, visited


def traverse_with_block(guard: str, grid: list[list[str]], block_pos: tuple[int, int]):
    directions = [
        (-1, 0),  # up
        (0, 1),   # right
        (1, 0),   # down
        (0, -1)   # left
    ]
    current_direction_index = 0
    moves = 1

    guard_pos = get_guard_position(guard, grid)
    if guard_pos is None:
        return moves, [], False

    row, col = guard_pos

    visited = set()
    moved = [(row, col)] 

    visited.add((row, col, current_direction_index))

    while True:
        dr, dc = directions[current_direction_index]
        new_row, new_col = row + dr, col + dc

        if (new_row, new_col) == block_pos:
            current_direction_index = rotate(current_direction_index)
            continue

        if not (0 <= new_row < len(grid) and 0 <= new_col < len(grid[0])):
            break

        if grid[new_row][new_col] == '#':
            current_direction_index = rotate(current_direction_index)
        else:
            # Move to the next position
            row, col = new_row, new_col
            moved.append((row, col))
            if (row, col, current_direction_index) in visited:
                return moves, moved, True
            else:
                visited.add((row, col, current_direction_index))
                moves += 1

    return moves, moved, False


def find_loops_with_blocks(guard: str, grid: list[list[str]]):
    loops_detected = 0

    _, visited = traverse(guard, grid)
    guard_pos = get_guard_position(guard, grid)

    for block_pos in visited:
        if block_pos == guard_pos:
            continue
        _, _, is_loop = traverse_with_block(guard, grid, block_pos)
        if is_loop:
            loops_detected += 1

    return loops_detected


def main():
    with open("./input.txt") as f:
        data = f.read()
    grid: list[list[str]] = [list(line) for line in data.split("\n") if line.strip()]

    guard = '^'

    start_time_one = time.time()
    # Part One: Original traversal
    print("Part One:")
    moves, _ = traverse(guard, grid)
    print("Moves:", moves)
    print("%s seconds" % (time.time() - start_time_one))

    start_time_two = time.time()
    # Part Two: Loop detection with artificial blocks
    print("\nPart Two:")
    loops_detected = find_loops_with_blocks(guard, grid)
    print("Number of artificial blocks creating loops:", loops_detected)
    print("%s seconds " % (time.time() - start_time_two))


if __name__ == "__main__":
    main()
