from turtle import color


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
print(v1.tipo)
v2=Vehiculo("azul","auto",2)
print(v2.color)
v3=Vehiculo("rojo","camion",3)
print(v3.cilindrada)
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
from funciones import pri,lis_frec,temp,fac

class func:
    def __init__(self,a,lista,grados,b):
        self.a=a
        self.lista=lista
        self.grados=grados
        self.b=b




    
