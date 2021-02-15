import math
a = int(input("Введите первый катет: "))
b = int(input("Введите второй катет: "))
l = math.sqrt(a*a + b*b)
print("Гипотенуза равна: " + str(l))
