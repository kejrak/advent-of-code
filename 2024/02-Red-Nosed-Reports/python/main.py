
def is_increasing(arr):
    return all(i < j for i, j in zip(arr, arr[1:]))

def is_decreasing(arr):
    return all(i > j for i, j in zip(arr, arr[1:]))

def increases(arr):
    return [j - i for i, j in zip(arr, arr[1:])]

def decreases(arr):
    return [i - j for i, j in zip(arr, arr[1:])]

def find_removable(arr):
    
    # Check if the array is already valid with max increase/decrease <= 3
    if is_increasing(arr) and max(increases(arr)) <= 3:
        return None
    if is_decreasing(arr) and max(decreases(arr)) <= 3:
        return None
    
    for i in range(len(arr)):
        modified_sequence = arr[:i] + arr[i+1:]
        
        if is_increasing(modified_sequence) and (1<= max(increases(modified_sequence)) <= 3):
            print("modified", modified_sequence)
            return True
        
        elif is_decreasing(modified_sequence) and (1<= max(decreases(modified_sequence)) <= 3):
            print("modified", modified_sequence)
            return True
    
    return None 


def main():
  with open("./input.txt") as f:
    data = f.read()

  safePartOne = 0
  safePartTwo = 0

  matrix = [list(map(int, row.split())) for row in data.splitlines() if row]
  for i in matrix:
    increasing = is_increasing(i)
    decreasing = is_decreasing(i)

    if increasing:
       if 1 <=max(increases(i)) <= 3:
          print("increasing:", i)
          safePartOne += 1
          safePartTwo += 1

    if decreasing:
       if 1 <= max(decreases(i)) <= 3:
          print("deacreasing", i)
          safePartOne += 1
          safePartTwo += 1

    is_safe = find_removable(i)
    
    if is_safe:
       safePartTwo += 1

  print(safePartOne)  
  print(safePartTwo)
    

if __name__ == "__main__":
    main()
  
    