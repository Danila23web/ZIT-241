def reverse_number(n):

    if n < 10:
        print(n, end="")
    else:
        print(n % 10, end="") 
        reverse_number(n // 10)

num = int(input("Введите число: "))

print("Число в обратном порядке:", end=" ")
reverse_number(num)
print()