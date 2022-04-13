print('Задача 2. Калькулятор')
print()
act = input('Выберите операцию: ')
first_num = int(input('Введите первое число: '))
second_num = int(input('Введите второе число: '))
if act == '+':
	result = int(first_num + second_num)
elif act == '-':
	result = int(first_num - second_num)
elif act == '*':
	result = int(first_num * second_num)
elif act == '/':
	result = int(first_num / second_num)
else:
	result = 'НЕ ПОЛУЧАЕТСЯ'
	print('Неверно введено действие.')

print(first_num, act, second_num, '=', result)