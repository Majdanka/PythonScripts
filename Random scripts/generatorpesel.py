wagi = [1,3,7,9,1,3,7,9,1,3]
def generatorPesel():
    from random import randint
    pesel = ""
    rok = randint(0,99)
    miesiac = randint(1,12)
    flag = randint(0,1)
    if miesiac in [1,3,5,7,8,10,12]:
        dzien = randint(1,31)
    elif miesiac in [4,6,9,11]:
        dzien = randint(1,30)
    else:
        if rok%4==0:
            dzien = randint(1,29)
        else:
            dzien = randint(1,28)
    if flag:
        miesiac+=20
    if rok<10:
        rok = "0"+str(rok)
    if(miesiac<10):
        miesiac = "0"+str(miesiac)
    if dzien<10:
        dzien="0"+str(dzien)
    pesel+=str(rok)+str(miesiac)+str(dzien)+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))+str(randint(0,9))
    kontr = 0
    for i in range(10):
        kontr+=(int(pesel[i])*wagi[i])%10
    kontr = 10-kontr%10
    if kontr%10==0:
        kontr = 0
    pesel+=str(kontr)
    return pesel
with open("./pesel.txt","w") as file:
    for i in range(100):
        generatorPesel()
        file.write(generatorPesel()+"\n")