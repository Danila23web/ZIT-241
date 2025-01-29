def find_smallest_divisor():
    
    n = int(input("Введите число (не меньшее 2): "))

    divisor = 2

    while n % divisor != 0:
        divisor += 1

    print(divisor)

find_smallest_divisor()
