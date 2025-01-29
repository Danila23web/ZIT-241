def move_max_to_top_left(matrix):
    
    n = len(matrix)
    m = len(matrix[0])
        
    max_value = matrix[0][0]
    max_row, max_col = 0, 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] > max_value:
                max_value = matrix[i][j]
                max_row, max_col = i, j
    
    if max_row != 0:
        matrix[0], matrix[max_row] = matrix[max_row], matrix[0]
    
    if max_col != 0:
        for i in range(n):
            matrix[i][0], matrix[i][max_col] = matrix[i][max_col], matrix[i][0]
    
    return matrix

matrix = [
    [1, 2, 3],
    [7, 8, 9],
    [4, 5, 6]
]

new_matrix = move_max_to_top_left(matrix)

print("Преобразованная матрица:")
for row in new_matrix:
    print(row)
