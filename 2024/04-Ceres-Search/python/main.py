def PartOne():
    with open("./input.txt") as f:
        data = f.read().splitlines()

    word = "XMAS"

    count = 0

    def search(index, x, y, dx, dy):
        if index == len(word):
            return 1

        if x < 0 or y < 0 or x >= len(data) or y >= len(data[0]) or word[index] != data[x][y]:
            return 0

        return search(index + 1, x + dx, y + dy, dx, dy)

    directions = [
        (1, 0),    # Down
        (-1, 0),   # Up
        (0, -1),   # Left
        (0, 1),    # Right
        (1, -1),   # Bottom-Left Diagonal
        (-1, -1),  # Top-Left Diagonal
        (1, 1),    # Bottom-Right Diagonal
        (-1, 1)    # Top-Right Diagonal
    ]

    for x in range(len(data)):
        for y in range(len(data[0])):
            for dx, dy in directions:
                count += search(0, x, y, dx, dy)

    print(count)

def getXMASed(character, x, y, data):
    if character != 'A':
        return 0

    left_top = data[x - 1][y - 1]
    right_top = data[x - 1][y + 1]
    left_bottom = data[x + 1][y - 1]
    right_bottom = data[x + 1][y + 1]

    wordLeft = f"{left_top}{right_bottom}"
    wordRight = f"{right_top}{left_bottom}"

    if (wordLeft == "SM" or wordLeft == "MS") and (wordRight == "SM" or wordRight == "MS"):
        return 1

    return 0

    

def PartTwo():
    with open("./input.txt") as f:
        data = f.read().splitlines()

    counter = 0

    for x in range(1, len(data) - 1): 
        for y in range(1, len(data[0]) - 1):
          counter += getXMASed(data[x][y], x, y, data)

    print(counter)
            
if __name__ == "__main__":
    PartOne()
    PartTwo()
