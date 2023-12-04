def nwd(a, b):
    if a == b:
        return a
    if a < 0:
        a *= -1
    if b > a:
        p = a
        a = b
        b = p
    while a % b != 0:
        p = b
        b = a % p
        a = p
    return b


def nww(a, b):
    return (a * b) / nwd(a, b)


x = [int(input("Licznik 1: ")), int(input("Mianownik 1: "))]
y = [int(input("Licznik 2: ")), int(input("Mianownik 2: "))]

dz = input("Wybierz działanie + - * / ")

if dz == '+':
    m = nww(x[1], y[1])

    x[0] = x[0] * (m / x[1])
    x[1] = m
    y[0] = y[0] * (m / y[1])
    y[1] = m

    z = nwd(int(x[0] + y[0]), int(x[1] * y[1]))

    print("Wynik: " + str(int(x[0] + y[0]) // z) + "/" + str(int(m) // z))

elif dz == '-':
    m = nww(x[1], y[1])
    x[0] = x[0] * (m / x[1])
    x[1] = m
    y[0] = y[0] * (m / y[1])
    y[1] = m
    z = nwd(int(x[0] - y[0]), int(x[1] * y[1]))
    print("Wynik: " + str(int(x[0] - y[0]) // z) + "/" + str(int(m) // z))

elif dz == "*":

    z = nwd(int(x[0] * y[0]), int(x[1] * y[1]))

    print("Wynik: " + str(int(x[0] * y[0]) // z) + "/" + str(int(x[1] * y[1]) // z))

elif dz == "/":

    z = nwd(int(x[0] * y[1]), int(x[1] * y[0]))

    print("Wynik: " + str(int(x[0] * y[1]) // z) + "/" + str(int(x[1] * y[0]) // z))
