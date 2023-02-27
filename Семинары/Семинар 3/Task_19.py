# 19.	Реализуйте алгоритм задания случайных чисел без использования 
# встроенного генератора псевдослучайных чисел.

import time

print(int(str(time.time())[-1])) # на основе миллисекунд времени 1

def Random_Set(start = 0, end = 1): # на основе миллисекунд времени 2
    second = time.time() # выдает количество секунд от создания интернета, точностью до 15 знака
    Next = True
    while Next:
        Rand = end * (second % 1)
        if Rand >= start or Rand > end: Next = False

    return int(Rand)

print(Random_Set(1, 100))



exit()
c = 50
A = 2
B = 3
x = 7
m = 100

lst = []

for i in range(c):
    x = (A * x + B) % m
    lst.append(x)
print(lst)