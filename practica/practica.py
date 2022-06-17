"""
a=[]
n=-15
while (n<0):
    a.append(n)
    n+=1   
print(a)

a=[-15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1]
n=0
while n<len(a):
    if a[n]%2==0:
        print(a[n])
    n+=1

a=[-15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1]

for i in a:
    if i%2==0:
        print(i)

a=[-15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1]
for i in a[0:3]:
    print(i)

a=[-15, -14, -13, -12, -11, -10, -9, -8, -7, -6, -5, -4, -3, -2, -1]

for i,e in enumerate(a):
    print(i,e)

lista = [1,2,5,7,8,10,13,14,15,17,20]
n=1
while n<=20:
    if not(n in lista):
        lista.insert(n-1,n)
    n+=1
print(lista)  

lista=[0,1]
c=1
while c<=28:
    lista.append(lista[c-1]+lista[c])
    c+=1
print(lista)

for i in range(29,24,-1):
    print(lista[i]/lista[i-1])

cadena = 'Hola Mundo. Esto es una practica del lenguaje de programación Python'

for i,c in enumerate(cadena):
    if c =='n':
        print(i)

dicc={'A':'1','B':'2','C':'3','D':'4','E':'5'}

for i in dicc:
    print(i)

cadena = 'Hola Mundo. Esto es una practica del lenguaje de programación Python'
lista_cadena= list(cadena)
for i in lista_cadena:
    print(i)

a=[1,2,3]
b=["peru","australia","no hay mundial"]
c=tuple(zip(a,b))
print(c)

lis = [18,21,29,32,35,42,56,60,63,71,84,90,91,100]
lis2= [i for i in lis if i%7!=0]
print(lis2)

contador=0
lis = [[1,2,3,4],'rojo','verde',[True,False,False],['uno','dos','tres']]
for i in lis:
    if type(i)==list:
        contador+=len(i)
    else:
        contador+=1
print(contador)

lis = [[1,2,3,4],'rojo','verde',[True,False,False],['uno','dos','tres']]
for i in lis:
    if type(i)!=list:
        d=lis.index(i)
        lis=lis[:d]+[[i]]+lis[d+1:]
print(lis)
"""
lis = [[1,2,3,4],'rojo','verde',[True,False,False],['uno','dos','tres']]

for indice,elemento in enumerate(lis):
    if type(elemento)!=list:
        lis[indice]=[elemento]
print(lis)






