# Вывести список тех элементов, которые больше, чем предыдущие

# Найти числа, кратные 20 и 21 из промежутка 20-240
lst = [el for el in range(20, 240) if el % 20 == 0 or el % 21 == 0]
print(lst)

# Вывести элементы, которые не повторяются
lst = [300, 300, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
lst = [el for el in lst if lst.count(el) == 1] # - встроенная функция
print(lst)

# Пример с Генератором
# Факториал числа!


from itertools import count # пишется на строке 1
def fact(n):
    factorial = 1

    for x in count(1): # range - до этого значения, count - начиная с этого значения
        if x > n:
            break
        factorial *= x
        yield factorial

n = int(input('введите целое число: '))
i = 0
for el in fact(n):
    i += 1
    print(f'!{i} = {el}')



from functools import reduce # применяется к массиву и сводится к одному значению
# Перемножить все элементв с шагом 2
lst = [x for x in range(100, 1001, 2)]
res = reduce(lambda item, item2: item * item2, lst)
print(res)

