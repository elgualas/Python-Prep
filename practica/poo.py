class Vehiculo:
    def __init__(self,color,tipo,cilindrada):
        self.color=color
        self.tipo=tipo
        self.cilindrada=cilindrada
        self.velocidad=0
        self.direccion=0
    def acelerar(self,vel):
        self.velocidad+=vel
    def frenar(self,vel):
        self.velocidad-=vel
    def doblar(self,grados):
        self.direccion+=grados
    def estado(self):
        print(f"el vehiculo se encuentra en una velocidad de {self.velocidad} km por hora y en una orientacion de {self.direccion} grados")
    def caracteristicas(self):
        print(f"las caracteristicas del vehiculo son las siguientes:\n color:{self.color}\n tipo:{self.tipo}\n cilindrada:{self.cilindrada}")

v1=Vehiculo("verde","moto",1)
#print(v1.tipo)
v2=Vehiculo("azul","auto",2)
#print(v2.color)
v3=Vehiculo("rojo","camion",3)
#print(v3.cilindrada)
v1.acelerar(30)
v2.acelerar(30)
v3.acelerar(30)
v1.doblar(30)
v2.doblar(-30)
v3.frenar(-50)
#v1.estado()
#v2.estado()
#v3.estado()
#v1.caracteristicas()
#v2.caracteristicas()
#v3.caracteristicas()


class herramientas:
    def __init__(self, lista_numeros):
        self.lista = lista_numeros

    def verifica_primo(self):
        for i in self.lista:
            if (self.__verifica_primo(i)):
                print('El elemento', i, 'SI es un numero primo')
            else:
                print('El elemento', i, 'NO es un numero primo')

    def conversion_grados(self, origen, destino):
        for i in self.lista:
            print(i, 'grados', origen, 'son', self.__conversion_grados(i, origen, destino),'grados',destino)
    
    def factorial(self):
        for i in self.lista:
            print('El factorial de ', i, 'es', self.__factorial(i))

    def __verifica_primo(self, nro):
        es_primo = True
        for i in range(2, nro):
            if nro % i == 0:
                es_primo = False
                break
        return es_primo   

    def valor_modal(self, menor):
        lista_unicos = []
        lista_repeticiones = []
        if len(self.lista) == 0:
            return None
        if (menor):
            self.lista.sort()
        else:
            self.lista.sort(reverse=True)
        for elemento in self.lista:
            if elemento in lista_unicos:
                i = lista_unicos.index(elemento)
                lista_repeticiones[i] += 1
            else:
                lista_unicos.append(elemento)
                lista_repeticiones.append(1)
        moda = lista_unicos[0]
        maximo = lista_repeticiones[0]
        for i, elemento in enumerate(lista_unicos):
            if lista_repeticiones[i] > maximo:
                moda = lista_unicos[i]
                maximo = lista_repeticiones[i]
        return moda, maximo

    def __conversion_grados(self, valor, origen, destino):
        valor_destino = None
        if (origen == 'celsius'):
            if (destino == 'celsius'):
                valor_destino = valor
            elif (destino == 'farenheit'):
                valor_destino = (valor * 9 / 5) + 32
            elif (destino == 'kelvin'):
                valor_destino = valor + 273.15
            else:
                print('Parámetro de Destino incorrecto')
        elif (origen == 'farenheit'):
            if (destino == 'celsius'):
                valor_destino = (valor - 32) * 5 / 9
            elif (destino == 'farenheit'):
                valor_destino = valor
            elif (destino == 'kelvin'):
                valor_destino = ((valor - 32) * 5 / 9) + 273.15
            else:
                print('Parámetro de Destino incorrecto')
        elif (origen == 'kelvin'):
            if (destino == 'celsius'):
                valor_destino = valor - 273.15
            elif (destino == 'farenheit'):
                valor_destino = ((valor - 273.15) * 9 / 5) + 32
            elif (destino == 'kelvin'):
                valor_destino = valor
            else:
                print('Parámetro de Destino incorrecto')
        else:
            print('Parámetro de Origen incorrecto')
        return valor_destino   

    def __factorial(self, numero):
        if(type(numero) != int):
            return 'El numero debe ser un entero'
        if(numero < 0):
            return 'El numero debe ser pisitivo'
        if (numero > 1):
            numero = numero * self.__factorial(numero - 1)
        return numero

#h=herramientas()
#print(h.verifica_primo(7))
#listado = [1,8,2,5,4,8,10,7]
#moda, repe = h.valor_modal(listado, True)
#print(moda, repe)
#print(h.conversion_grados(10, 'celsius', 'kelvin'))
#print(h.factorial(6))
h = herramientas([1,1,2,5,8,8,9,11,15,16,16,16,18,20])
h.conversion_grados('celsius','farenheit') 
h.verifica_primo()
moda, repe = h.valor_modal(False)
print('El valor modal es', moda, 'y se reptie', repe, 'veces')
h.factorial()
