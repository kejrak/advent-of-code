
import re

array = []

def main():
  with open("./input.txt") as f:
    data = f.read()

  paternPartOne = r'mul\(\d+,\d+\)'
  patternPartTwo = r'mul\(\d+,\d+\)|(?:do_not|don\'t|do)\(\)'

  matchesPartOne = re.findall(paternPartOne, data)
  matchesPartTwo = re.findall(patternPartTwo, data)

  enabled = True
  for match in matchesPartTwo:
    if match.startswith("mul") and enabled:
      array.append(match)
    if match == "don't()":
      enabled = False
    if match == "do()":
      enabled = True
    
  
  productsPartOne = [
      int(pair[0]) * int(pair[1]) 
      for pair in (item[3:].strip('()').split(',') for item in matchesPartOne)
  ]
    
  productsPartTwo = [
      int(pair[0]) * int(pair[1]) 
      for pair in (item[3:].strip('()').split(',') for item in array)
  ]

  print(sum(productsPartOne))
  print(sum(productsPartTwo))

     

if __name__ == "__main__":
    main()
  