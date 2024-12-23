def main():
    with open("./input.txt") as f:
        data = f.read().splitlines()

    rules_input = data[:data.index('')]
    order_input = data[data.index('')+1:]


    rules = [tuple(map(int, item.split('|'))) for item in rules_input]
    order = [list(map(int, item.split(','))) for item in order_input]

    sumPartOne = 0
    sumPartTwo = 0

    for _, q in enumerate(order):
        print(q)
        if is_order_correct(q, rules):
            middleIndex = (len(q) - 1) // 2
            sumPartOne += q[int(middleIndex)]

    print(sumPartOne)
    for _, q in enumerate(order):
        if not is_order_correct(q, rules):
            q_sorted = sorted(q, key=lambda x: sort_order(x, q, rules))
            middleIndex = (len(q_sorted) - 1) // 2
            sumPartTwo += q_sorted[int(middleIndex)]
    print(sumPartTwo)

def is_order_correct(order, rules):
    for before, after in rules:
        if before in order and after in order:
            if order.index(before) > order.index(after):
                return False
    return True

def sort_order(element, order, rules):
    key = 0
    for before, after in rules:
        if before == element:
            if before in order and after in order:
                key -= 1  
        if after == element:
            if before in order and after in order:
                key += 1 
    return key

if __name__ == "__main__":
    main()
