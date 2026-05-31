with open('input.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

    line_count = len(lines)

    word_count = 0
    for line in lines:
        words = line.split()
        word_count += len(words)

with open('statistics.txt', 'w', encoding='utf-8') as output_file:
    output_file.write(f"Количество строк: {line_count}\n")
    output_file.write(f"Количество слов: {word_count}\n")

print("Статистика успешно записана в файл statistics.txt")