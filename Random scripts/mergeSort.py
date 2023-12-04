def Sort(T):
    if len(T) > 1:
        s = len(T) // 2
        L = T[:s]
        R = T[s:]
        Sort(R)
        Sort(L)
        Merge(T,L,R)
def Merge(T,L,R):
    c1=c2=0
    ti=0
    while len(L)>c1 and len(R)>c2:
            if L[c1]<R[c2]:
                T[ti]=L[c1]
                c1+=1
                ti+=1
            else:
                T[ti]=R[c2]
                c2+=1
                ti+=1
    while c1<len(L):
            T[ti]=L[c1]
            c1+=1
            ti+=1
    while c2<len(R):
            T[ti]=R[c2]
            c2+=1
            ti+=1
T=[5,4,7,3,6,1,3,24,243,214,45,4646,53453453,2]
print(T)
Sort(T)
print(T)