print('Задача 3. Калькулятор 2')
print()

def addin(num, num_next):
    num += num_next
    return num

def subtracting(num, num_next):
    num -= num_next
    return num

def multiplication(num, num_next):
    num *= num_next
    return num

def division(num, num_next):
    num /= num_next
    return num

def printing(act, quantity, num):
    text = str(num) + ' ' + act + ' '
    for add in range(2, quantity + 1):
        print('Введите операнд', add, ': ', end = '')
        num_next = int(input(''))
        if add != quantity:
            text = text + (str(num_next) + ' ' + act + ' ')
        else:
            text = text + str(num_next)
        if act == '+':
            num = addin(num, num_next)
        elif act == '-':
            num = subtracting(num, num_next)
        elif act == '*':
            num = multiplication(num, num_next)
        elif act == '/':
            num = division(num, num_next)
    print(text, '=', num) 
	
act = input('Выберите операцию: ')
quantity = int(input('Сколько операндов? '))
print('Введите операнд 1 : ', end = '')
num = int(input(''))

printing(act, quantity, num)
