mass = [1,2,546,12,3,531,22,213]

def countSort(a):
    acc=[]
    for i in range(1010):
        acc+=[0]
    for i in a:
        acc[i]+=1
    j=0
    for i in range(1010):
        if acc[i]>0:
            for k in range(acc[i]):
                a[j]=i
                j+=1

    return  a
print(countSort(mass))