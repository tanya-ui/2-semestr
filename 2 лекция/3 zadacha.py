a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
for i in range(b, a-1, -1):
    if i % 2 > 0:
        print( i )
input()
