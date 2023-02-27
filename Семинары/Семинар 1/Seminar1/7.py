# 7.	Напишите программу для. проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат

# x V y          V - or      /\ - and       ¬ x отриыание не x - not(x)

print('x y z F')
for x in range(2):
    for y in range(2):
        for z in range(2):
            f = x or y or z
            print(x, y, z, bool(f))