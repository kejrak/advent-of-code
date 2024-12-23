from collections import defaultdict

def process_stones(stones):
    new_stones = defaultdict(int)
    for stone, count in stones.items():
        if stone == 0:
            new_stones[1] += count
        elif len(str(stone)) % 2 == 0:
            stone_str = str(stone)
            mid = len(stone_str) // 2
            left, right = stone_str[:mid].lstrip("0"), stone_str[mid:].lstrip("0")
            new_stones[int(left) if left else 0] += count
            new_stones[int(right) if right else 0] += count
        else:
            new_stones[stone * 2024] += count
    return new_stones

def main():
    with open("input.txt") as f:
        data = f.read().split()

    stones = {int(n): 1 for n in data}
    for i in range(75):
        stones = process_stones(stones)
        print(f"Blink {i + 1}: {sum(stones.values())} stones")


if __name__ == "__main__":
    main()
