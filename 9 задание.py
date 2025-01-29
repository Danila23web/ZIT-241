def is_symmetric(matrix):

    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True

matrix = [
    [1, 2, 3],
    [2, 5, 6],
    [3, 6, 9]
]

if is_symmetric(matrix):
    print("Матрица симметрична относительно главной диагонали.")
else:
    print("Матрица не симметрична относительно главной диагонали.")
