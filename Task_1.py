# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

line_text = [str(i) for i in input('Введите текст: ').split()]
find_text = input('Введите буквы, слова с содержанием которых будут удалены: ')
new_line = []
count = 0
for item in line_text:
    if item.find(find_text) == -1:
        new_line.append(item)

print(' '.join(new_line))

