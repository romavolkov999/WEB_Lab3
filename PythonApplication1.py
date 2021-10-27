from sys import stdin
from copy import deepcopy
import numpy

class Matrix:
    # initialization
    def __init__(self, matrix):
        self.matrix = deepcopy(matrix)
    # string
    def __str__(self):
        return '\n'.join('\t'.join(map(str, row)) for row in self.matrix)
    # appeal
    def __getitem__(self, idx):
        return self.matrix[idx]
    # m1 > m2
    def __gt__(self, other):
        return numpy.linalg.det(self.matrix) > numpy.linalg.det(other.matrix)
    # m1 < m2
    def __lt__(self, other):
        return numpy.linalg.det(self.matrix) < numpy.linalg.det(other.matrix)
    # m1 = m2
    def __eq__(self, other):
        return numpy.linalg.det(self.matrix) == numpy.linalg.det(other.matrix)
    # m1 + m2
    def __add__(self, other):
        other = Matrix(other)
        result = []
        numbers = []
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                sum = other[i][j] + self.matrix[i][j]
                numbers.append(sum)
                if len(numbers) == len(self.matrix):
                    result.append(numbers)
                    numbers = []
        return Matrix(result)
    # m1 * m2
    def __mul__(self, other):
        result = Matrix([[0,0],[0,0]])
        for i in range(len(self.matrix)):
            for j in range(len(other.matrix[0])):
                for k in range(len(other.matrix)):
                    result[i][j] += self[i][k] * other[k][j]
        return result

m1 = Matrix([[1,1],[2,2]])
m2 = Matrix([[1,2],[5,6]])

if (m1 > m2):
    print("m1 is more than m2")
elif (m1 < m2):
    print("m2 is more than m1")
else:
    print("m1 equals m2")

print("\nSum:")
print(m1 + m2)
print("\nMultiplication: ")
print(m1 * m2)