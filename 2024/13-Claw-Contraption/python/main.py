from sympy import Eq, solve, Symbol

with open("input.txt") as f:
    data = f.read()

count = 0

# Split the data into blocks
blocks = data.strip().split("\n\n")
for block in blocks:
    lines = block.split("\n")
    
    button_a_line = lines[0].split(", ")
    button_b_line = lines[1].split(", ")
    prize_line = lines[2].split(", ")
    
    button_a_x = int(button_a_line[0].split("+")[1])
    button_a_y = int(button_a_line[1].split("+")[1])
    button_b_x = int(button_b_line[0].split("+")[1])
    button_b_y = int(button_b_line[1].split("+")[1])
    prize_x = int(prize_line[0].split("=")[1]) + 10_000_000_000_000
    prize_y = int(prize_line[1].split("=")[1]) + 10_000_000_000_000

    a = Symbol("a", integer=True)
    b = Symbol("b", integer=True)

    equation1 = Eq(a * button_a_x + b * button_b_x, prize_x)
    equation2 = Eq(a * button_a_y + b * button_b_y, prize_y)

    solution = solve((equation1, equation2), (a, b))

    if solution:
        for var, value in solution.items():
            if var == a:
                count += value * 3
            elif var == b:
                count += value

print(count)
