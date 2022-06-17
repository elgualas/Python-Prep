def pri(a):
    cont=0
    for i in range(1,a+1):
        if a%i==0:
            cont+=1
    if cont>2:
        return False
    else:
        return True
def lis_pri(a):
    se= []
    for i in a:
        if pri(i)==True:
            se.append(i)
    return se
def lis_frec(a):
    cont=0
    for i in range(1,max(a)+1):
        result=[a.count(i)]
    return result
        




print(pri(7))
print(lis_pri([2,3,4,5,6,7,8,9]))
print(lis_frec([2,3,4,2,6,2,8,2]))
