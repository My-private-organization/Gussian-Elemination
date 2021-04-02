import numpy as num
import math


# setting default value to true for d


def GaussianElimination(A, B, d=True):

    matrixDimension = int(math.sqrt(A.size))

    for i in range(matrixDimension - 1):
        for j in range(i + 1, matrixDimension):
            tempVar = A[j][i]
            A[j] = A[j] - (A[i] * (tempVar / A[i][i]))
            B[j] = B[j] - (B[i] * (tempVar / A[i][i]))

            if d:

                print("Matrix A:")
                for p in range(matrixDimension):

                    for q in range(matrixDimension):
                        print(format(A[p][q], '.4f'), end='  ')
                    print()

                print("Matrix B:")
                for p in range(matrixDimension):
                    print(format(B[p][0], '.4f'))
                print()

    resultList = []

    for i in range(matrixDimension - 1, -1, -1):
        sum = 0
        for j in range(matrixDimension - 1, i, -1):
            sum += A[i][j] * resultList[matrixDimension - 1 - j]

        resultList.append((B[i] - sum) / A[i][i])

    resultList.reverse()

    return num.array(resultList)


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

A = num.array(matrixA)
B = num.array(matrixB)

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
