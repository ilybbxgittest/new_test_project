print()
print('Задача 1. Таблица умножения: возвращение')
for multiplied in range(2, 7, 4):
	print()
	for multiplier in range(2, 11):
		print(multiplied, 'x', multiplier, '=', multiplied * multiplier, ' ', \
              '\t', multiplied + 1, 'x', multiplier, '=', (multiplied + 1) * multiplier,  ' ', \
		'\t', multiplied + 2, 'x', multiplier, '=', (multiplied + 2) * multiplier,  ' ', \
		'\t', multiplied + 3, 'x', multiplier, '=', (multiplied + 3) * multiplier)