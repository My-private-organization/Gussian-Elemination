import numpy as np
from math import sqrt


def GaussianElimination(A, B, d=True):

    matrixDimension = int(sqrt(A.size))

    for i in range(matrixDimension - 1):
        for j in range(i + 1, matrixDimension):
            a = A[j][i]
            A[j] = A[j] - (A[i] * (a / A[i][i]))
            B[j] = B[j] - (B[i] * (a / A[i][i]))
            if d:
                print("A:")
                for x in range(matrixDimension):
                    for y in range(matrixDimension):
                        print(format(A[x][y], '.4f'), end='  ')
                    print()

                print("B:")
                for x in range(matrixDimension):
                    print(format(B[x][0], '.4f'))

                print()

    res = []

    for i in range(matrixDimension - 1, -1, -1):
        sum = 0
        for j in range(matrixDimension - 1, i, -1):
            sum += A[i][j] * res[matrixDimension - 1 - j]
        res.append((B[i] - sum) / A[i][i])

    res.reverse()

    result = np.array(res)

    return result


print('Enter number of unknown variable: ')

numberOfUnKnownVariable = int(input())

matrixA = []

print('Please enter matrix A in row major order: ')

for i in range(numberOfUnKnownVariable):
    inputSequence = input()
    res = list(map(float, inputSequence.split(' ')))
    matrixA.append(res)

matrixB = []

print('Please enter matrix B in row major order: ')

for i in range(numberOfUnKnownVariable):
    b = [float(input())]
    matrixB.append(b)

A = np.array(matrixA)
B = np.array(matrixB)

print('Enter the value of d:(1 for true and 2 for false)')

temp = int(input())

if temp == 1:
    d = True
else:
    d = False

value = GaussianElimination(A, B, d)

print("Sample output:-")

for i in range(numberOfUnKnownVariable):
    print(format(value[i][0], '.4f'))
