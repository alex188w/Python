# 13.	Напишите программу, в которой пользователь будет задавать две строки, 
# а программа - определять количество вхождений одной строки в другой

# string_1 = input('Введите первую строку: ')
# string_2 = input('Введите втрую строку: ')
# print (string_1.count (string_2))

string_1 = input('Введите первую строку: ')
string_2 = input('Введите втрую строку: ')
count = 0
for i in string_1:
    for j in string_2:
        if i == j:
            count +=1
print(count)