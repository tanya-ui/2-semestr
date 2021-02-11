import math
n = float(input("Введите количество учеников: "))
k = float(input("Введите количество яблок: "))
a = k/n
b = math.floor( a )
c = a - b
if a < 1:
    print("Ученики не получили яблок. Остаток в корзине: " + str(round(k)))
if a > 1:
    print ("Каждый ученик получил по: " +str(b) + " Яблок \nОстаток в корзине: " + str(round(c, 3)))
input("Нажмите ENTER для выхода")

