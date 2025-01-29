array = [3, 25, 18, 9, 12, 6, 30, 15, 7, 22, 8, 5, 20, 11, 19]

original_array = array.copy()

transformed_array = [0 if x < 10 else 1 if x > 20 else x for x in array]

print("Исходный массив:", " ".join(map(str, original_array)))
print("Преобразованный массив:", " ".join(map(str, transformed_array)))
