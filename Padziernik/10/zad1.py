n=int(input("Podaj n:"))
tab=[]
for x in range (n):
    tab.append([])
    for y in range (n):
        tab[x].append(y)
print(tab)