def binaryToDecimal(x):
    w = 0
    for a in range(len(x)):
        w += int(x[len(x) - (a + 1)]) * pow(2, len(x) - (a + 1))
    return w


def universalToDecimal(x, y):
    w = 0
    for a in range(len(x)):
        w += int(x[len(x) - (a + 1)]) * pow(y, len(x) - (a + 1))
    return w


print(binaryToDecimal(str(input("Binary to decimal: "))))
print(universalToDecimal(str(input("Universal to decimal: ")), int(input("Universal base: "))))


def decimalToBinary(x):
    w = []
    while x > 0:
        w.append(x % 2)
        x //= 2
    w.reverse()
    return w


def universalToBinary(x, y):
    w = []
    while x > 0:
        w.append(x % y)
        x //= y
    w.reverse()
    return w


print(decimalToBinary(int(input("Decimal to binary: "))))
print(universalToBinary(int(input("Decimal to binary: ")), int(input("Universal base: "))))
