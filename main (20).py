#Задание 35 
import numpy as np 
def sss():
    A = np.random.randint(-10, 10, size=(7,4))
    print("Матрица:")
    print(A)
    sums = np.zeros(7)
    for i in range(7):
        for j in range(4):
            if A[i,j]>0:
                sums[i] += A[i,j]
    print(sums)
    return A,sums 
x,c = sss()
#Задание 36 
import numpy as np 
def fff():
    m = int(input("введите 1 число: "))
    n = int(input("введите 2 число: "))
    A = np.random.randint(-10,10,size=(m,n))
    print("Матрица:")
    print(A)
    row = () 
    print(sum(row for row in A / len(A) ))
    return A, m, n 
c,x,a = fff()
#Задание 37 
import numpy as np 
def zzz(): 
    m = int(input("введите 1 число: "))
    n = int(input("введите 2 число: "))
    A = np.random.randint(-10,10,size=(m,n))
    print("Матрица:")
    print(A)
    print(np.count_nonzero(A, axis=1))
    return A, m, n 
x,a,r = zzz()
#Задание 38 
import random

def generate_matrix(M, N):
    return [[random.randint(-10, 10) for _ in range(N)] for _ in range(M)]

def negative_products_array(matrix):
    products = [1] * len(matrix[0])
    for row in matrix:
        for i, val in enumerate(row):
            if val < 0:
                products[i] *= val
    return products

M = 3  
N = 4 

B = generate_matrix(M, N)
print(B)

negative_products = negative_products_array(B)
print(negative_products)
#Задание 39 
import random

def generate_matrix(M, N):
    return [[random.randint(-10, 10) for _ in range(N)] for _ in range(M)]

def min_elements_array(matrix):
    return [min(row) for row in matrix]

M = 3  
N = 4

A = generate_matrix(M, N)
print(A)

min_elements = min_elements_array(A)
print(min_elements)
#Задание 40 
import random

def generate_matrix(M, N):
    return [[random.randint(0, 1) for _ in range(N)] for _ in range(M)]

def count_nonzero_elements(matrix):
    return [len([item for item in row if item != 0]) for row in matrix]

M = 3  
N = 4  

A = generate_matrix(M, N)
print(A)

nonzero_counts = count_nonzero_elements(A)
print(nonzero_counts)

    
    
    
