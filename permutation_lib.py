from math import factorial

def swap(mylist,a,b):
    mylist[a], mylist[b] = mylist[b], mylist[a]
    return(mylist)

def permutation(perma):
    x=y=0
    for i in range(len(perma)-2, -1, -1):
        if perma[i]<perma[i+1]:
            break
    x=i
    for i in range(i,len(perma),1):
        if perma[x]< perma[i]:
            y=i
    perma = swap(perma, x, y)
    perma[x+1:] = reversed(perma[x+1:])
    return(perma)

#Example
value=['a', 'b', 'c']
print(value)
for i in range(1, factorial(len(value))):
    value=permutation(value)
    print(value)
