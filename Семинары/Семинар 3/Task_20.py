# 20.	Задайте список. Напишите программу, которая определит, 
# присутствует ли в заданном списке строк некое число

n = int(input('Введите число: '))
my_list = ['wewy3', 'dfgh867', '4436d, 555rty567']
length = len(my_list)
Flag = False 
n = str(n)
for i in range(length):
    if my_list[i].find(n) != -1 :
        Flag = True
        break
print(Flag)