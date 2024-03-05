#Задание 6 
n = int(input("введите число: "))
while n >= 0: 
    print(n)
    n -= 1 
#Задание 7 
a = float(input("введите a: "))
sum = 0 
n = 1 
while sum <= a:
    sum += 1/n 
    n += 1 
for i in range(1,n):
    print(i)
#Задание 8 
n = int(input("введите число: "))
a = 1 
while True: 
    if a**2 > n:
        print(a)
        break
    else: 
        a +=1
#Задание 9 
a = 200 
while True: 
    if a % 17 == 0: 
        print(a)
        break 
    else: 
        a += 1 
#Задание 10 
a = 600 
while True: 
    if a % 28 == 0: 
        print(a)
        break 
    else: 
        a -= 1 