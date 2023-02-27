# 21.	Напишите программу, которая определит позицию второго вхождения
#  строки в списке либо сообщит, что её нет

str = (input('Введите строку: '))
my_list = ['wewy3', 'qwe', 'dfgh867', '4436d', 'qwe', '555rty567']
count = 0
for i in range(len(my_list)):
    if my_list[i] == str:
        count += 1
        if count == 2:
            print(f'Да, присутствует, позиция равна {i}')
if count < 2:
    print('Нет второго вхождения')
        
