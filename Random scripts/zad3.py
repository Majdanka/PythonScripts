sa = ['a', 'ą', 'e', 'ę', 'i', 'o', 'u' , 'y']
tx=input("Podaj tekst:")
tx1=""
tx2=""
for x in range(len(tx)):
    if tx[x].lower() in sa:
        tx1+=str(tx[x])
    else:
        tx2+=str(tx[x])
print(str(tx1+tx2).replace("_", ""))