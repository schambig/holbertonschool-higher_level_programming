#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i in row:
            if i is not row[len(row) - 1]:
                print("{:d}".format(i), end=' ')
            else:
                print("{:d}".format(i), end='')
        print()

# The code below also works
#    for i in range(0, len(matrix)):
#        for j in range(0, len(matrix[i])):
#            if (j == len(matrix[i]) - 1):
#                print("{:d}".format(matrix[i][j]), end='')
#            else:
#                print("{:d}".format(matrix[i][j]), end=' ')
#        print(end='\n')
