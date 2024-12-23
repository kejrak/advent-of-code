def move_files_part_two(arr):
    n = len(arr)
    files = {}

    for i, val in enumerate(arr):
        if isinstance(val, int):
            files.setdefault(val, []).append(i)
    print(files)

    for file_id in sorted(files.keys(), reverse=True):
        positions = files[file_id]
        file_size = len(positions)
        free_count = 0
        leftmost_space = -1

        for i in range(n):
            if arr[i] == '.':
                free_count += 1
                if free_count == file_size:
                    leftmost_space = i - file_size + 1
                    break
            else:
                free_count = 0

        if leftmost_space != -1 and leftmost_space + file_size - 1 < positions[0]:
            for pos in positions:
                arr[pos] = '.'
            for i in range(file_size):
                arr[leftmost_space + i] = file_id

    return arr


def move_towards_dots_part_one(arr):
    n = len(arr)
    reverse_index = n - 1
    new_arr = arr[:]

    for i in range(n):
        if new_arr[i] == '.':
            while reverse_index > i and new_arr[reverse_index] == '.':
                reverse_index -= 1
            if reverse_index > i:
                new_arr[i], new_arr[reverse_index] = new_arr[reverse_index], '.'
                reverse_index -= 1

    return new_arr


def compute_sum(arr):
    return sum(index * int(value) for index, value in enumerate(arr) if value != '.')

def main():
    with open("input.txt") as f:
        data = f.read()

    result_dict = {
        i // 2: (int(data[i]), int(data[i + 1]) if i + 1 < len(data) else 0)
        for i in range(0, len(data), 2)
    }

    data_arr = []
    for key, (x, y) in result_dict.items():
        data_arr += int(x) * [key]
        data_arr += int(y) * ["."]


    new_array_one = move_towards_dots_part_one(data_arr)
    new_array_two = move_files_part_two(data_arr)
    sum_part_one = 0
    sum_part_two = 0

    for index, number in enumerate(new_array_one):
        if new_array_one[index] == ".":
            continue
        sum_part_one += index * int(number)

    for index, number in enumerate(new_array_two):
        if new_array_two[index] == ".":
            continue
        sum_part_two += index * int(number)

    print(sum_part_one)
    print(sum_part_two)

if __name__ == "__main__":
    main()
