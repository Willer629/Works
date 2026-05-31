with open('words.txt', 'r') as f:
    words = []
    for line in f:
        word = line.strip()
        if word:
            words.append(word)

words.sort()
with open('sorted_alphabetically.txt', 'w') as f:
    for word in words:
        f.write(word + '\n')

words.sort(key=len)
with open('sorted_by_length.txt', 'w') as f:
    for word in words:
        f.write(word + '\n')

words.sort(reverse=True)
with open('sorted_reverse.txt', 'w') as f:
    for word in words:
        f.write(word + '\n')

print("Готово!")
