#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix[0])):
        for c in range(len(matrix[0])):
            if c != len(matrix[1]) - 1:
                print('{}'.format(matrix[i][c]), end=" ")
            else:
                print('{}'.format(matrix[i][c]), end="")
        print("",  end="$\n")


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_matrix_integer(matrix)
print("--")
print_matrix_integer()