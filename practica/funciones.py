
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
def lis_frec(a,menor):
    list_un=[]
    list_mod=[]
    if (menor):
        a.sort()
    else:
        a.sort(reverse=True)
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

def temp(t,o,c):
    if o=="k":
        if c=="f":
            res=(t-273.15)(9/5)+32
        elif c=="c":
            res=t-273,15
    elif o=="f":
        if c=="k":
            res=(t-32)(5/9)+273.15
        elif c=="c":
            res=(t-32)(5/9)
    elif o=="c":
        if c=="f":
            res=t*(9/5)+32
        elif c=="k":
            res=t+273.15
    return res

def fac(a):
    x=1
    while True:
        if a<=1:
            print("Ingresa un numero que no sea 1,0 o negativo")
            break
        else:
            for i in range(1,a+2):
                x*=i
            break
    return x
print(fac(0))
