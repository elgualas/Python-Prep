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
"""
cadena = 'Hola Mundo. Esto es una practica del lenguaje de programación Python'

for i,c in enumerate(cadena):
    if c =='n':
        print(i)





