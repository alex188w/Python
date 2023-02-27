# value = None
# print (type(value))
a = 123
b = 1.23
# print (a)
# print (b)
# print (type(a))
# print (type(b))
# value = 23456
# print (value)
# s = 'hello \'World' # для вывода апострофа
# d = "hello 'World"
# v = 'hello \nWorld' # перевод на новую строку
# print (a, '-',b, '-', s)   
# print ('{2} - {1} - {0}'.format(a, b, s)) # через формат
# print (f'{a} - {b} - {s}') #  вывод строки через интерполяцию
# f = True
# print (f)

# МАССИВЫ СПИКИ
# list = ['1', '2', '3']
# col = ['hello', 1, 2, 4.5, True]
# print (list)
# print (col)

# Ввод и вывод
# print ('Введите а'); # если вещественные числа то float
# a = int(input())
# print ('Введите b');
# b = int(input())
# print (a, ' + ', b, ' = ', a+b)

# Арифметические действия
# // деление в целых числах
# % - остаок от деления
# a ** b - возведение в степень
# a = 1.22345
# b = 5
# c = round(a * b, 5) # round - округление, если нет цифры по законам математики, если есть цифра - до того знака
# print (c)

#  Присваивание
# a = 3
# a += 5  # = a + 5
# print (a)

# Логические операции
# >, >=, <, <=, ==, !=
# not, and, or – не путать с &, |, ^

# Кое-что ещё: is, is not, in, not in
# a = 1 < 4 and 5 > 2
# print (a)

# a = 'qwe'
# b = 'qwe'
# a = [1, 2]
# b = [1, 2]
# print (a == b)

# f = 5
# T = 15
# x = 123
# print (f<T>(x))

# f = 1 > 2 or 4 < 6
# print (f)

# f = [1, 2, 3, 4]
# print (f)
# print (not 2 in f)

# is_odd = f[0] % 2 == 0 # проверка четности числа
# print (is_odd)

# нахождение максимального двух чисел
# a = int(input('a = '))
# b = int(input('b = '))
# if a > b:
    # print(a)
# else:
    # print(b)

# username = input('Введите имя: ')
# if username == 'Маша':
    # print('Ура, это же МАША!')
# elif username == 'Марина':
    # print('Я так ждала Вас, Марина!')
# elif username == 'Ильнар':
    # print('Ильнар - топ)')
# else:
    # print('Привет, ', username)

# original = 123 # инвертирование числа
# inverted = 0
# while original != 0:
    # inverted = inverted * 10 + (original % 10)
    # original //= 10
# print(inverted)

# original = 123
# inverted = 0
# while original != 0:
    # inverted = inverted * 10 + (original % 10)
    # original //= 10
# else:
    # print('Пожалуй')
    # print('хватит )')
# print(inverted)
# Пожалуй
# хватит )
# 32

# list = [1, 2, 3, 4, 5]
# for i in list:
    # print (i**2)

# for i in 1, -2, 3, 14, 5:
    # print (i)

# r = range(10)
# for i in r:
    # print (i)

# for i in range(1, 10, 2): # приращение 2
    # print (i)

# for i in 'qwe - rty':
    # print (i)

# text = 'съешь ещё этих мягких французских булок'
# print(len(text)) # 39
# print('ещё' in text) # True
# print(text.isdigit()) # False
# print(text.islower()) # True
# print(text.replace('ещё','ЕЩЁ')) #

# for c in text:
    # print(c)

# text = 'съешь ещё этих мягких французских булок'
# print(text[0])   # c
# print(text[1])   # ъ
# print(text[len(text)-1])  # к
# print(text[-5])  # б
# print(text[:])   # print(text)
# print(text[:2])  # съ
# print(text[len(text)-2:])  # ок
# print(text[2:9])  # ешь ещё
# print(text[6:-18])  # ещё этих мягких
# print(text[0:len(text):6])  # сеикакл
# print(text[::6])  # сеикакл
# text = text[2:9] + text[-5] + text[:2] # ...

# Списки: введение

# numbers = [1, 2, 3, 4, 5]
# print(numbers)  # [1, 2, 3, 4, 5]

# numbers = list(range(1, 6))
# print(numbers)  # [1, 2, 3, 4, 5]

# numbers[0] = 10
# print(numbers)  # [10, 2, 3, 4, 5]

# for i in numbers:
    # i *= 2
    # print(i)    # [20, 4, 6, 8, 10]
# print(numbers)  # [10, 2, 3, 4, 5]

# colors = ['red', 'green', 'blue']

# for e in colors:
 # print(e) # red green blue

# for e in colors:
 # print(e*2) # redred greengreen blueblue

# colors.append('gray') # добавить в конец
# print(colors == ['red', 'green', 'blue', 'gray']) # True
# colors.remove('red') #del colors[0] # удалить элемент


# Функции
def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return

print(f(1))         # Целое
print(f(2.3))       # 23
print(f(28))        # None
print(type(f(1)))   # str
print(type(f(2.3))) # int
print(type(f(28)))  # NoneType