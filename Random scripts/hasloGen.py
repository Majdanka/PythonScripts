alfabet = [
    'a',
    'b',
    'c',
    'd',
    'e',
    'f',
    'g',
    'h',
    'i',
    'j',
    'k',
    'l',
    'm',
    'n',
    'o',
    'p',
    'q',
    'r',
    's',
    't',
    'u',
    'v',
    'w',
    'x',
    'y',
    'z'
]
znakiSpecjalne = [
    '!',
    '@',
    '#',
    '$',
    '%',
    '^',
    '&',
    '*',
    '(',
    ')',
    '-',
    '_',
    '+',
    '=',
    '[',
    ']',
    '{',
    '}',
]

def hasloGen(alfabet, znakiSpecjalne, dlugosc, c, d, z):
    import random
    haslo = ''
    if c:
        haslo+=str(random.randint(0,9))
    if d:
        haslo+=alfabet[random.randint(0,len(alfabet)-1)].upper()
    if z:
        haslo+=znakiSpecjalne[random.randint(0,len(znakiSpecjalne)-1)]
    for i in range(int(dlugosc)-len(haslo)):
        haslo+=alfabet[random.randint(0,len(alfabet)-1)]
    return haslo

dlugosc = 0
while dlugosc < 5:
    dlugosc = int(input('Podaj dlugosc hasla (min 5): '))
c=d=z=False
if(input('Czy haslo ma zawierac cyfry? (t/n) ') == 't'):
    c=True
if(input('Czy haslo ma zawierac duze litery? (t/n) ') == 't'):
    d=True
if(input('Czy haslo ma zawierac znaki specjalne? (t/n) ') == 't'):
    z=True
file = open('hasla.txt', 'w')
for i in range(int(input('Ile hasel wygenerowac? '))):
    file.write(hasloGen(alfabet, znakiSpecjalne, dlugosc, c, d, z) + '\n')