alf = ['T','U','V','K','L','M','N','W','F', 'X','Y','Z','G','H','I','J','O','P','A','B','C','D','E','R','S','Q']
znaki=[]
for x in range(5):
    znaki.append(str(input("Podaj znak: ")).upper())
print(znaki)
for x in range (len(znaki)):
    for y in range (len(znaki)):
        if(alf.index(str(znaki[x]))<alf.index(str(znaki[y]))):
            p=znaki[x]
            znaki[x]=znaki[y]
            znaki[y]=p
print(znaki)