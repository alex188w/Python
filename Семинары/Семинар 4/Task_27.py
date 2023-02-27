# 27.	Задайте строку из набора чисел. Напишите программу, которая покажет 
# большее и меньшее число. В качестве символа-разделителя используйте пробел

a = "5 46 33 78 26"

lst = a.split()
new_lst = []
for i in lst:
    new_lst.append(int(i))

print(new_lst)

print(max(new_lst), min(new_lst))

new_lst.sort()
print(new_lst[-1], new_lst[0])
