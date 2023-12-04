tab=[]
for x in range (2):
    tab.append([])
    for y in range (3):
        tab[x].append(y)
print("Wypisanie do zadania:")
c=0
for x in range (len(tab[0])):
    print("Kolumna "+str(x))
    for y in range (len(tab)):
        print(" "+str(tab[y][x]))