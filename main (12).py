#Задание 27
ma1 = [2, 34, 65, 45, 43, 22, 11, 66, 9, 3, 7, 110, 256, 265, 239, 950, 235]
ma2 = [1, 5, 6, 7, 8, 9, 10, 2, 3, 4, 11, 12, 14, 13, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
ma3 = []
for i in ma1 + ma2: 
    ma3.append(i)
ma3 = set(ma3)
print(ma3)
#Задача 28
mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(mat)
count_nonzero = sum(map(lambda x: x.count(0), mat))
print(f"Количество ненулевых элементов: {count_nonzero}")
#Задача 29 
D = [[1, 2, 3], [4, -5, 6], [7, 8, 9]]
print(D)
negative_elements_product = 1
for row in D:
    for element in row:
        if element < 0:
            negative_elements_product *= element
print(f"Произведение отрицательных элементов: {negative_elements_product}")
#Задача 30 
B = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(B)
positive_elements_product = 1
for row in B:
    for element in row:
        if element > 0:
            positive_elements_product *= element
print(f"Произведение положительных элементов: {positive_elements_product}")
#Задача 31
B = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(B)
min_element = min(B)
min_coords = B.index(min_element)
print(f"Минимальный элемент: {min_element}")
print(f"Координаты минимального элемента: {min_coords}")
