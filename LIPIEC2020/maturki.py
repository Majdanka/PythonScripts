def zad4_1(): 
    max=0
    wynik=[]
    with open("identyfikator.txt",'r') as file:
        for line in file:
            z=0
            for i in range (3,9):
                z+=int(line[i])
            if z>max:
                wynik=[]
                wynik.append(line.replace('\n',''))
                max=z
            elif z==max:
                wynik.append(line.replace('\n',''))
                max=z
    print(wynik)
def zad4_2(): 
    wynik=[]
    with open("identyfikator.txt",'r') as file:
        for line in file:
            if line[0]==line[2]:
                wynik.append(line.replace('\n',''))
            else:
                flag=True
                for i in range (3,5):
                    if line[i]!=line[11-i]:
                        flag=False
                if flag:
                    wynik.append(line.replace('\n',''))
    print(wynik)
def zad4_3():
    wartosci = {
        'A':10,
        'B':11,
        'C':12,
        'D':13,
        'E':14,
        'F':15,
        'G':16,
        'H':17,
        'I':18,
        'J':19,
        'K':20,
        'L':21,
        'M':22,
        'N':23,
        'O':24,
        'P':25,
        'Q':26,
        'R':27,
        'S':28,
        'T':29,
        'U':30,
        'V':31,
        'W':32,
        'X':33,
        'Y':34,
        'Z':35
    }
    wagi = [7, 3, 1, 0, 7, 3, 1, 7, 3]
    wynik=[]
    with open("identyfikator.txt",'r') as file:
        for line in file:
            z=0
            for i in range (0,len(line)-1):
                if line[i] in wartosci:
                    z+=wartosci[line[i]]*wagi[i]
                    print(line[i],wartosci[line[i]],wagi[i],z)
                else:
                    z+=int(line[i])*wagi[i]
                    print(line[i],wagi[i],z)
            print(z, line[3], line)
            if z%10!=int(line[3]):
                wynik.append(line.replace('\n',''))
    print(wynik)
def zad5():
    wynik={
        '1':0,
        '2':0,
        '3':0,
        '4':0,
        '5':0,
        '6':0,
        '7':0,
        '8':0,
        '9':0,
        '10':0,
        '11':0,
        '12':0,
        '13':0,
        '14':0,
        '15':0,
    }
    for x in range (1,16):
        print("Program ",x,"-minutowy",wynik[str(x)])
zad5()