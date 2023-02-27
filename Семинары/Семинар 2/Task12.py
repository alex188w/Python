# 12.	Для натурального n создать список, состоящий из элементов
# последовательности 3n + 1.
# Пример: Для n = 6: [4, 7, 10, 13, 16, 19]

# num = int(input('Введите число n: '))
# list = []
# for i in range(1, num + 1):
#     elem = 3 * i + 1
#     list.append(elem)     # присвоение массиву значений
# print(list)

# Другой способ
# num = int(input('Введите число n: '))
# for i in range(1, num + 1):
#     num = 3 * i + 1
#     print(num, end= ' ')

# Другой способ
num = int(input('Введите число n: '))
a = [3 * i + 1 for i in range(1, num + 1)]
print(a)
 
