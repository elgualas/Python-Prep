from pip import main


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
    list_un=[]
    list_mod=[]
    if len(a)==0:
        return None
    for elementos in a:
        if elementos in list_un:
            i=list_un.index(elementos)
            list_mod[i]+=1
        else:
            list_un.append(elementos)
            list_mod.append(1)
    moda=list_un[0]
    rep=list_mod[0]
    print(list_un)
    print(list_mod)
    for i,elementos in enumerate(list_un):
        if list_mod[i]>rep:
            moda=list_un[i]
            rep=list_mod[i]
    return moda, rep

print(lis_frec([5,3,2,6,2,3,3,3,3,8,2,2,9,7]))
