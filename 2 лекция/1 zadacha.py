
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
if a <= b:
    for i in range(a, b + 1):
        print(i)
else:
    print("Число a должно быть меньше b ")

