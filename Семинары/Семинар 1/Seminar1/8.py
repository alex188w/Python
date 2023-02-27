# Задача 7.	Напишите программу для проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат

print('X \t Y \t Z \t F1 \t F2 \t истинно/ложно')
for X in range(2):
    for Y in range(2):
        for Z in range(2):
            f1 = not (X or Y or Z)
            f2 = not X and not Y and not Z
            print(X, '\t', Y, '\t', Z, '\t', f1, '\t', f2, '\t', f1 == f2)