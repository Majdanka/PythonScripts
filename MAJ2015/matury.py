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
    with open('./MAJ2015/liczby.txt','r') as f:
        l=1
        minw=minl=maxw=maxl=0
        for line in f:
            line=line.replace('\n','')
            line=int(line,2)
            if(l==1):
                minw=line
                minl=l
            if(line>maxw):
                maxw=line
                maxl=l
            if(line<minw):
                minw=line
                minl=l
            l+=1
        print("Min: "+str(minl),"Max: "+str(maxl))
zad4_3()
            