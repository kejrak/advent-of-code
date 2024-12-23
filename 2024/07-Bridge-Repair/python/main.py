from itertools import product

def solve_part_one(target, numbers):
    n = len(numbers) - 1 
    operators = ["+", "*"]

    for ops in product(operators, repeat=n):
        acc = numbers[0]
        valid = True

        for i, op in enumerate(ops):
            if op == "+":
                acc += numbers[i + 1]
            elif op == "*":
                acc *= numbers[i + 1]

            if acc > target:
                valid = False
                break

        if valid and acc == target:
            return True

    return False

def solve_part_two(target, numbers):
    n = len(numbers) - 1  
    operators = ["+", "*", "||"]

    for ops in product(operators, repeat=n):
        acc = numbers[0]
        valid = True

        for i, op in enumerate(ops):
            if op == "||":
                acc = int(f"{acc}{numbers[i + 1]}")
            elif op == "+":
                acc += numbers[i + 1]
            elif op == "*":
                acc *= numbers[i + 1]

            if acc > target:
                valid = False
                break

        if valid and acc == target:
            return True

    return False

def main():
    with open("input.txt") as f:
        data = f.read().splitlines()

    sum_part_one = 0
    sum_part_two = 0

    for line in data:
        target, rest = line.split(":")
        target = int(target.strip())
        numbers = list(map(int, rest.strip().split()))

        if solve_part_one(target, numbers):
            sum_part_one += target

        if solve_part_two(target, numbers):
            sum_part_two += target

    print(f"Part One Sum: {sum_part_one}")
    print(f"Part Two Sum: {sum_part_two}")

if __name__ == "__main__":
    main()
