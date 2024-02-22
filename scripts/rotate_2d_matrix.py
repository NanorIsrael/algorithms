matrix = [[1, 2, 3],
[4, 5, 6],
[7, 8, 9]]

# [7, 4, 1]
# [8, 5, 2]
# [9, 6, 3]
def rotate_matrix(matrix):
	if len(matrix) == 0:
		return matrix
	new_matrix = []
	for i in range(len(matrix)):
		new_row = []
		for j in range(i, len(matrix[i])):
			matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

	for i in range(len(matrix)):
		matrix[i].reverse()

rotate_matrix(matrix)
print(matrix)