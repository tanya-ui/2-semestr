a = int(input("Напишите число: "))
if a == 0:
    print(0)
else:
    fib_prev, fib_next = 0, 1
    b = 1
    while fib_next <= a:
        if fib_next == a:
            print("Результат" + str(b))
            break
        fib_prev, fib_next = fib_next, fib_prev + fib_next
        b += 1
    else:
        print("Результат: " + str(-1))
