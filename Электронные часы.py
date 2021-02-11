import math
n = float(input("Сколько минут прошло с начала суток?: "))
a = 1440 - n
b = a/60 - 24
if n > 1440:
    print("Это больше чем минут в сутках!")
    input()
else:
    if b < 0:
        b = math.floor(-b)
    if b > 0:
        b = math.floor(b)
        if a > 60:
            a = a - 60
        if a > 60:
            a = a - 60
        if a > 60:
            a = a - 60
        if a > 60:
            a = a - 60
        if a > 60:
            a = a - 60
        if a > 60:
            a = a - 60
        if a > 60:
            a = a - 60
        if a > 60:
            a = a - 60
        if a > 60:
            a = a - 60
        if a > 60:
            a = a - 60
        if a > 60:
            a = a - 60
        if a > 60:
            a = a - 60
        if a > 60:
            a = a - 60
        if a > 60:
            a = a - 60
        if a > 60:
            a = a - 60
        if a > 60:
            a = a - 60
        if a > 60:
            a = a - 60
        if a > 60:
            a = a - 60
        if a > 60:
            a = a - 60
        if a > 60:
            a = a - 60
        if a > 60:
            a = a - 60
        if a > 60:
            a = a - 60
        if a > 60:
            a = a - 60
        if a == 60:
            a = 00
        print("Сейчас " + str(b) + " Часов " + str(a) + " минут до конца дня")
        input()
