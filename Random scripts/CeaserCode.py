def decode(l, w):
    alf = ["a",
           "b",
           "c",
           "d",
           "e",
           "f",
           "g",
           "h",
           "i",
           "j",
           "k",
           "l",
           "m",
           "n",
           "o",
           "q",
           "p",
           "r",
           "s",
           "t",
           "w",
           "v",
           "x",
           "y",
           "z", ]
    if l == " ":
        return l
    for i in range(len(alf)):
        if l == alf[i]:
            if i > 2:
                return alf[i - w]
            else:
                return alf[23 - w + i]


z = []
a = str(input("Podaj tekst do rozszyfrowania: ")).lower()
b = int(input("Podaj ile offseta: "))
for x in range(len(a)):
    z.append(decode(a[x], b))
print(z)
