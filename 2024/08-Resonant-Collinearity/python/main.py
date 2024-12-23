def solution_one(grid):
    N = len(grid)
    M = len(grid[0])

    nodes = {}
    for i in range(N):
        for j in range(M):
            if grid[i][j] != ".":
                if grid[i][j] in nodes:
                    nodes[grid[i][j]].append((i, j))
                else:
                    nodes[grid[i][j]] = [(i, j)]

    antinodes = set()

    def antinode(pr1, pr2):
        x1, y1 = pr1
        x2, y2 = pr2
        newx = x2 + (x2 - x1)
        newy = y2 + (y2 - y1)
        if 0 <= newx < N and 0 <= newy < M:
            antinodes.add((newx, newy))

    for k in nodes:
        node_list = nodes[k]
        L = len(node_list)
        for i in range(L):
            for j in range(i):
                node1 = node_list[i]
                node2 = node_list[j]
                antinode(node1, node2)
                antinode(node2, node1)

    return len(antinodes)


def solution_two(grid):
    N = len(grid)
    M = len(grid[0])

    nodes = {}
    for i in range(N):
        for j in range(M):
            if grid[i][j] != ".":
                if grid[i][j] in nodes:
                    nodes[grid[i][j]].append((i, j))
                else:
                    nodes[grid[i][j]] = [(i, j)]

    antinodes = set()

    def antinode(pr1, pr2):
        x1, y1 = pr1
        x2, y2 = pr2
        dx, dy = x2 - x1, y2 - y1
        newx, newy = x2 + dx, y2 + dy
        antinodes.add((x2, y2))
        while 0 <= newx < N and 0 <= newy < M:
            antinodes.add((newx, newy))
            newx += dx
            newy += dy

    for k in nodes:
        node_list = nodes[k]
        L = len(node_list)
        for i in range(L):
            for j in range(i):
                node1 = node_list[i]
                node2 = node_list[j]
                antinode(node1, node2)
                antinode(node2, node1)

    return len(antinodes)


def main():
    with open("input.txt") as f:
        data = f.read().splitlines()

    grid = [line.strip() for line in data if line.strip()]

    print("Solution One:", solution_one(grid))
    print("Solution Two:", solution_two(grid))


if __name__ == "__main__":
    main()
