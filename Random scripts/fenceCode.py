
k = int(input("Podaj klucz: "))
komb = str(input("Podaj kombinacje: "))

def deszyfr():
    l = str(input("Podaj tekst do rozszyfrowania: ")).lower()
    print("Deszyfrowanie: ")
    tekst=""
    for x in range (len(l)//k):
        for y in range(k):
                tekst+=l[(int(komb.index(str(y)))*len(l)//k)+x]
    print(tekst)
    

def szyfr():
    l = str(input("Podaj tekst do szyfrowania: ")).lower()
    print("Szyfrowanie: ")
    z=[]
    a=len(l)
    if(a%k!=0):
        for x in range(k-a%k):
            l+="@"
    c=0
    for a in range (int(len(l)/k)):
        z.append([])
        for b in range (k):
            z[a].append(l[c])
            c+=1
    c=0

    for f in range(len(z)):
        print(z[f])

    tekst=""
    for y in range(k):
        for f in range(len(z)):
            tekst+=str(z[f][int(komb[c])])
        c+=1
    print(tekst)

if(int(input("[0]Szyfrowanie\n[1]Rozszyfrowanie\n"))==0):
    szyfr()
else:
    deszyfr()