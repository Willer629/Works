word = input("Введите слово: ").lower()

with open('text.txt', 'r', encoding='utf-8') as f:
    text = f.readlines()

count = 0
lines = []

for i, line in enumerate(text, 1):
    if word in line.lower():
        count += 1
        lines.append(i)

print(f"Найдено: {'Да' if count > 0 else 'Нет'}")
print(f"Количество: {count}")
print(f"Строки: {lines if lines else '-'}")

with open('search_results.txt', 'w', encoding='utf-8') as f:
    f.write(f"Найдено: {count}\n")
    f.write(f"Строки: {lines}")