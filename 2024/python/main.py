def count_ways_to_form_word(word, available_words, memo):
    if word in memo:
        return memo[word]

    if word == "":
        return 1

    total_ways = 0

    for w in sorted(available_words, key=len, reverse=True):
        if word.startswith(w): 
            remaining_word = word[len(w):]
            total_ways += count_ways_to_form_word(remaining_word, available_words, memo)

    memo[word] = total_ways
    return total_ways


with open("input.txt") as f:
    data = f.read().splitlines()

vowels = data[0].replace(",", "").split()  
words_to_check = data[2:] 

results = {}
for word in words_to_check:
    memo = {}
    results[word] = count_ways_to_form_word(word, vowels, memo)

sum = 0
for word, ways in results.items():
    sum += ways

print(sum)
