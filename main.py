# Задание 1
m = ['круг', 0.25, 'квадрат', 'треугольник', 15, 'круг', 'овал', '10']
m.remove(0.25)
m.remove(15)
m.remove("10")
print(m)
# Задание 2
abc = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
del abc[1]
del abc[1]
del abc[1]
del abc[1]
print(abc)
# Задание 3
numbers = [1, 4]
numbers.insert(1, 3)
numbers.insert(1, 2)
print(numbers)
# Задание 4
mass = [14, -6, 3, 11, 6, 8.5, 99, -20, -6, 10, 40, 0.25, -4, 5]
mass.remove(-6)
mass.remove(-20)
mass.remove(-6)
mass.remove(-4)
mass.sort()
print(mass)
mass.sort(reverse = True)
print(mass)
# Задание 5
pol = []
otr = []
null = []
i = 0
count = int(input("Введите количество чисел: "))
while i < count:
    a = int(input("Введите числа: "))
    i += 1
    if a > 0:
        pol.append(a)
    elif a < 0:
        otr.append(a)
    else:
        null.append(a)
otr_summ = 0
pol_summ = 0 
for o in otr:
    otr_summ += o
for p in pol:
    pol_summ += p
print(otr_summ)
if len(pol) == 0:
    print("Нет")
else:
    print(pol_summ / len(pol))
for col in range(len(null)):
    null[col] = '*'
print(f'Количество звезд: {len(null)} {null}')