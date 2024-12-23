from collections import Counter

array1 = []
array2 = []

def main():
  with open("./input.txt") as f:
    for line in f:
        # Split the line into two numbers and append to respective arrays
        num1, num2 = map(int, line.split())
        array1.append(num1)
        array2.append(num2)

  array1.sort()
  array2.sort() 

  array2_counts = Counter(array2)

  sumPartOne = 0
  sumPartTwo = 0

  for numberL, numberR in zip(array1, array2):
      occurencies = array2_counts[numberL]
      sumPartOne += abs(numberL - numberR)
      sumPartTwo += numberL * occurencies
     
  print(sumPartOne)
  print(sumPartTwo)

if __name__ == "__main__":
    main()
  
    