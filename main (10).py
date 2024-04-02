#Задача 1 
def schet(): 
    a = input ("Введите 1 число: ")
    a = float (a)
    b = input ("Введите 2 число: ")
    b = float (b)
    c = input ("Введите 3 число: ")
    c = float (c)
    if a > b > c: 
        print (a - b - c)
    elif b > a > c: 
        print (b - a - c)
    else: 
        print (c - a - b)
    return a, b, c
    
c, d, r = schet()
e, f, b = schet()
z, x, m= schet()