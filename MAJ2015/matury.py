def zad4_1():
    with open('liczby.txt','r') as f:
        cg=0
        for line in f:
            c0=c1=0
            for i in range(1, len(str(line))-1):
                if int(line[i])==0:
                    c0+=1
                elif int(line[i])==1:
                    c1+=1
            if c0>c1:
                cg+=1
    print(cg)
def zad4_2():
    with open('liczby.txt','r') as f:
        c2=c8=0
        for l in f:
            line=l.replace('\n','')
            if str(line[len((line))-1])=='0':
                c2+=1
                if str(line[len(line)-4:len(line)-1])=="000":
                    c8+=1
        print(c2,c8)
def zad4_3():
    with open('liczby.txt','r') as f:
        maxW=0
        minW=0
        max=0
        min=10000000000000000000000
        for line in f:
            index=0
            c=0
            line=line.replace('\n','')
            for i in range(0,len(line)-1):
                if line[i]==1:
                    c+=1*pow(2,len(line)-i-1)
            if c>max:
                max=c
                maxW=index
            elif c<min:
                min=c
                minW=index
            index+=1
zad4_3()
            