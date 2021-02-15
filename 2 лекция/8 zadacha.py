import math
P = float(input("Процентная ставка по вкладу: "))
X, Y = float(input("Рублей: ")), float(input("Копеек: "))
s = round((X + Y) * (1 + P/100))
print(str(s)+ " рублей")
