#Задание 35-40 в прошлой р
# Задание 43
import random 
def skibidi():
    stolbi = 5
    stroki = 3
    B = []
    nulevoy_spisok = []
    Ne_nulevoy_spisok = []
    for stolb in range(stolbi):
        nulevoy_el = 0
        Ne_nulevoy_el = 0
        matrix_numb = []
        for stroka in range(stroki):
            matrix_numb.append(random.randint(-5, 5))
            B.append(matrix_numb)
        for i in matrix_numb:
            if i == 0:
                nulevoy_el += 1 
                continue
            elif i != 0:
                Ne_nulevoy_el += 1
        nulevoy_spisok.append(nulevoy_el)
        Ne_nulevoy_spisok.append(Ne_nulevoy_el)
    for vivod in B:
        print(vivod)
    print('\n', 'Количество нулевых элементов', nulevoy_spisok)
    print('\n', 'Количество ненулевых элементов', Ne_nulevoy_spisok)
    return stolbi, stroki, B 
s, x, c = skibidi()
