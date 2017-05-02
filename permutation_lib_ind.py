def samFact(n):
    ans=1
    for i in range(1,n+1):
        ans*=i
    return(ans)

def samSwap(mylist,a,b):
    temp = mylist[a]
    mylist[a]=mylist[b]
    mylist[b]=temp
    return(mylist)

def samReverse(mylist,a):
    leng=int((len(mylist)+a)/2)
    for i in range(a,leng):
        mylist = samSwap(mylist,i,len(mylist)+a-i-1)
    return(mylist)


def samPermutation(perma):
    x=y=0
    for i in range(len(perma)-2,-1,-1):
        if perma[i]<perma[i+1]:
            break
    x=i
    for i in range(i,len(perma),1):
        if perma[x]< perma[i]:
            y=i
    perma = samSwap(perma,x,y)
    perma = samReverse(perma,x+1)
    return(perma)

#Example
value=['a','b','c','d']
vfact=samFact(len(value))
print(value)
for i in range(1,vfact):
    value=samPermutation(value)
    print(value)
