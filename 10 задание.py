import os

def read_matrix_from_file(filename):
    
    try:
        with open(filename, "r", encoding="utf-8") as file:
            matrix = [list(map(float, line.strip().split())) for line in file]
        return matrix
    except FileNotFoundError:
        print(f"Ошибка: файл '{filename}' не найден.")
        return None
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return None


def write_result_to_file(filename, results):
    
    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write("\n".join(results) + "\n")
    except Exception as e:
        print(f"Ошибка при записи файла: {e}")


def is_symmetric(matrix):
    
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True


def move_max_to_top_left(matrix):
    
    n, m = len(matrix), len(matrix[0])

    max_value = float('-inf')
    max_row, max_col = 0, 0

    for i in range(n):
        for j in range(m):
            if matrix[i][j] > max_value:
                max_value = matrix[i][j]
                max_row, max_col = i, j

    if max_row != 0:
        matrix[0], matrix[max_row] = matrix[max_row], matrix[0]

    if max_col != 0:
        for row in matrix:
            row[0], row[max_col] = row[max_col], row[0]

    return matrix

input_file = "Кучма ЗИТ-241 ввод.txt"
output_file = "Кучма ЗИТ-241 вывод.txt"

if not os.path.exists(input_file):
    print(f"Ошибка: файл '{input_file}' не найден. Убедитесь, что он находится в правильной папке.")
else:
    matrix = read_matrix_from_file(input_file)

    if matrix is not None and len(matrix) > 0:
        if len(matrix) == len(matrix[0]):
            symmetric_result = "Матрица симметрична." if is_symmetric(matrix) else "Матрица не симметрична."
        else:
            symmetric_result = "Матрица не квадратная. Проверка симметричности невозможна."

        transformed_matrix = move_max_to_top_left(matrix)

        output_data = [symmetric_result, "Преобразованная матрица:"]
        output_data += [" ".join(map(str, row)) for row in transformed_matrix]

        write_result_to_file(output_file, output_data)
        print(f"Результаты сохранены в файл {output_file}.")
