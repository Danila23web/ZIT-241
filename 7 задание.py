array = [5, 3, 7, 9, 2, 3, 10, 15, 7, 20, 11, 2, 5, 4, 6]

duplicates = set([x for x in array if array.count(x) > 1])

if duplicates:
    print("Повторяющиеся элементы:", ", ".join(map(str, duplicates)))
else:
    print("Повторяющиеся элементы отсутствуют.")
