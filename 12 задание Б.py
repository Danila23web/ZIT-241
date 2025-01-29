def find_two_max(second_max, first_max):
    
    num = int(input())

    if num == 0:
        return second_max

    if num > first_max:
        return find_two_max(first_max, num)
    elif num > second_max:
        return find_two_max(num, first_max)
    else:
        return find_two_max(second_max, first_max)

print("Введите последовательность чисел (завершите ввод 0):")
second_max_value = find_two_max(float('-inf'), float('-inf'))

if second_max_value == float('-inf'):
    print("Второго максимального элемента нет.")
else:
    print("Второй по величине элемент:", second_max_value)
