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
            return list_un
        

print(lis_frec([2,5,3,2,6,2,8,2,9,7]))
