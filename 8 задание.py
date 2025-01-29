def count_numbers_with_digits(n, digits):
    
    count = 0
    for number in range(100, n + 1):
        if all(int(digit) in digits for digit in str(number)):
            count += 1
    return count

while True:
    try:
        n = int(input("Введите значение N (210 < N < 231): "))
        if 210 < n < 231:
            break
        else:
            print("Число N должно быть в диапазоне от 211 до 230.")
    except ValueError:
        print("Пожалуйста, введите корректное целое число.")

while True:
    try:
        digits_input = input("Введите цифры a, b, c через запятую (например, 1,2,3): ")
        digits = set(map(int, digits_input.split(',')))
        if all(0 <= digit <= 9 for digit in digits):
            break
        else:
            print("Все цифры должны быть от 0 до 9.")
    except ValueError:
        print("Пожалуйста, введите корректные цифры через запятую.")
        
result = count_numbers_with_digits(n, digits)
print(f"Количество чисел на отрезке [100, {n}], состоящих из цифр {digits}: {result}")
