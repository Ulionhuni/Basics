import numpy as np
import sys
def gauss(a):
    a = np.concatenate((a[np.any(a != 0, axis=1)], a[np.all(a == 0, axis=1)]), axis=0)
    for i in range(0, a.shape[0]):
        j = 1
        pivot = a[i][i]
        while pivot == 0 and i + j < a.shape[0]:
            a[[i, i + j]] = a[[i + j, i]]
            j += 1
            pivot = a[i][i]
        if pivot == 0:
            return a
        row = a[i]
        a[i] = row / pivot
        for j in range(i + 1, a.shape[0]):
            a[j] = a[j] - a[i] * a[j][i]
    return a
print('Maden by Mykyta Dubov', 'Greetings!!!', 'This program can do some matrix operations', sep='\n\n')
print('Here is the list of operations I can ofer for you:')
print('1:Determinant' , '2:Inverse Matrix', '3:Matrix Traspose', '4:Matrix Rank', '5:Gauss elimination','6:Addition', '7:Subtraction', '8:Multiplication', '9:N-power', sep = '\n')
print()
print()
print('Please enter the number of the operation you would like to use')
operation = int(input())
re = lambda:map(int , input().split())
if operation == 1:
    print('Please enter the matrix size(just one number) and then on the next line the whole matrix ')
    n = int(input())
    a = np.zeros((n, n))
    #a = a.astype(np.int64)
    for i in range (n):
        b = list(re())
        for j in range (len(b)):
            a[i,j] = b[j]
    print(np.linalg.det(a))
if operation == 2:
    print('Please enter the matrix size(just one number) and then on the next line the whole matrix ')
    n = int(input())
    a = np.zeros((n, n))
    #a = a.astype(np.int64)
    for i in range (n):
        b = list(re())
        for j in range (len(b)):
            a[i, j] = b[j]
    print(np.linalg.inv(a))
if operation == 3:
    print('Please enter the matrix size(just one number) and then on the next line the whole matrix ')
    n, m = re()
    a = np.zeros((n, m))
    #a = a.astype(np.int64)
    for i in range (n):
        b = list(re())
        for j in range (len(b)):
            a[i, j] = b[j]
    print(np.transpose(a))
if operation == 4:
    print('Please enter the matrix size(just one number) and then on the next line the whole matrix')
    n, m = re()
    a = np.zeros((n, m))
    #a = a.astype(np.int64)
    for i in range (n):
        b = list(re())
        for j in range (len(b)):
            a[i, j] = b[j]
    print(np.linalg.matrix_rank(a))
if operation == 5:
    print('Please enter the matrix size and then on the next line the whole matrix')
    n, m = re()
    a = np.zeros((n, m))
    for i in range (n):
        b = list(re())
        for j in range (len(b)):
            a[i, j] = b[j]
    print(gauss(a))
if operation == 6:
    print('Please enter the matrix A size and then on the next string the whole matrix A')
    n, m = re()
    a = np.zeros((n, m))
    #a = a.astype(np.int64)
    for i in range (n):
        b = list(re())
        for j in range (len(b)):
            a[i, j] = b[j]
    print('The size of first summand you have already entered, all I need is the second summand,which is matrix B')
    b = np.zeros((n, m))
        #a = a.astype(np.int64)
    for i in range (n):
        c = list(re())
        for j in range (len(c)):
            b[i, j] = c[j]
    print(a + b)
if operation == 7:
    print('Please enter the matrix A size and then on the next string the whole matrix A')
    n, m = re()
    a = np.zeros((n, m))
    #a = a.astype(np.int64)
    for i in range (n):
        b = list(re())
        for j in range (len(b)):
            a[i, j] = b[j]
    print('The size of minuend you have already entered, all I need is minuend,which is matrix B')
    b = np.zeros((n, m))
        #a = a.astype(np.int64)
    for i in range (n):
        c = list(re())
        for j in range (len(c)):
            b[i, j] = c[j]
    print(a - b)
if operation == 8:
    print('Please enter the matrix A size and then on the next string the whole matrix A')
    n, m = re()
    a = np.zeros((n, m))
    #a = a.astype(np.int64)
    for i in range (n):
        b = list(re())
        for j in range (len(b)):
            a[i, j] = b[j]
    print('Please enter the second factor (matrix B) size and then on the next string the whole matrix B')
    k, l = re()
    b = np.zeros((k, l))
    #a = a.astype(np.int64)
    for i in range (k):
        c = list(re())
        for j in range (len(c)):
            b[i, j] = c[j]
    result = np.zeros((n, l))
    for i in range(len(a)):
        for j in range(len(b[0])):
            for t in range(len(b)):
                result[i][j] += a[i, t] * b[t, j]
    print(result)
if operation == 9:
    print('Please enter the matrix A size and then on the next string the whole matrix A')
    n = int(input())
    a = np.zeros((n, n))
    for i in range (n):
        b = list(re())
        for j in range (len(b)):
            a[i, j] = b[j]
    print('Please type the power in which you would like to raise you matrix')
    num = int(input())
    #a = a.astype(np.int64)
    print(np.linalg.matrix_power(a, num))
