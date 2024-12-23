
def find_trails_part_one(matrix):
    rows, cols = len(matrix), len(matrix[0])

    def dfs(x, y, target, visited, reached_nines):
      
      if target == 9:
          if (x, y) not in reached_nines:
              reached_nines.add((x, y))  
              return 1
          return 0

     
      if not (0 <= x < rows and 0 <= y < cols) or matrix[x][y] != target:
          return 0


      visited.add((x, y))

      total_trails = 0

      for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
          nx, ny = x + dx, y + dy 
          if (
              0 <= nx < rows and 0 <= ny < cols  
              and (nx, ny) not in visited      
              and matrix[nx][ny] == target + 1 
          ):
              total_trails += dfs(nx, ny, target + 1, visited, reached_nines)

      visited.remove((x, y))

      return total_trails
   
    
    total_trails_per_zero = {}
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0: 
                reached_nines = set()  
                visited = set() 
                trails = dfs(i, j, 0, visited, reached_nines)
                total_trails_per_zero[(i, j)] = trails

    return total_trails_per_zero

def find_trails_part_two(matrix):
    rows, cols = len(matrix), len(matrix[0])

    def dfs(x, y, target):
      if target == 9:
          return 1
      if not (0 <= x < rows and 0 <= y < cols) or matrix[x][y] != target:
          return 0

      total_trails = 0

      for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
          nx, ny = x + dx, y + dy  
          if ( 0 <= nx < rows and 0 <= ny < cols and matrix[nx][ny] == target + 1):
              total_trails += dfs(nx, ny, target + 1)


      return total_trails

   
    total_trails_per_zero = {}
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:  
                trails = dfs(i, j, 0)
                total_trails_per_zero[(i, j)] = trails

    return total_trails_per_zero


def main():
    with open("input.txt") as f:
        data = f.read().splitlines()

    matrix = [[int(char) for char in row] for row in data]

    part_one = find_trails_part_one(matrix)
    part_two = find_trails_part_two(matrix)

    sum_part_one = 0
    sum_part_two = 0

    for _, count in part_one.items():
        sum_part_one += count

    for _, count in part_two.items():
        sum_part_two += count

    print(sum_part_one)
    print(sum_part_two)


if __name__ == "__main__":
    main()
