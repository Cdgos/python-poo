# Polimorfismo (poli => muchas / morfos: formas)

# ========================= #
import os
os.system("cls")
# ========================= #

from typing import Protocol

class DesplazamientoProtocol(Protocol):
    def desplazamiento(self):
        ...

class Vehiculo:
    def desplazamiento(self):
        pass


class Coche(Vehiculo):
    def desplazamiento(self):
        print("Me desplazo utilizando cuatro ruedas")


class Moto(Vehiculo):
    def desplazamiento(self):
        print("Me desplazo utilizando dos ruedas")


class Camion(Vehiculo):
    def desplazamiento(self):
        print("Me desplazo utilizando seis ruedas")


miVehiculo = Moto()
miVehiculo2 = Coche()
miVehiculo3 = Camion()

vehiculos: list[DesplazamientoProtocol] = [miVehiculo, miVehiculo2, miVehiculo3]

for vehiculo in vehiculos:
    vehiculo.desplazamiento()


"""
    En este ejemplo se demuestra el concepto de POLIMORFISMO en programación orientada a objetos,
    pero usando un enfoque más moderno con 'Protocol' del módulo 'typing'.

    🔹 Concepto general:
        El polimorfismo permite que diferentes clases tengan métodos con el mismo nombre, pero
        con comportamientos distintos. En este caso, todas las clases ('Coche', 'Moto', 'Camion')
        comparten el método 'desplazamiento()', pero cada una lo implementa de forma diferente.

    🔹 Uso de Protocol:
        - 'Protocol' es una forma más flexible de tipado estructural introducida en Python.
        - En lugar de basarse en la herencia (como cuando una clase hija extiende una clase base),
          el protocolo define una "interfaz" o "contrato" que cualquier clase puede cumplir
          simplemente implementando los métodos especificados.
        - Aquí se define 'DesplazamientoProtocol' con un único método requerido: 'desplazamiento()'.
          Cualquier clase que tenga ese método será considerada válida para este tipo.

    🔹 Cómo funciona el código:
        1. Se definen tres clases ('Coche', 'Moto' y 'Camion'), cada una con su propio método 
           'desplazamiento()' que imprime un mensaje diferente.
        2. Se crean tres instancias de estas clases.
        3. Se declara una lista llamada 'vehiculos' con anotación de tipo:
               list[DesplazamientoProtocol]
           Esto significa que la lista puede contener cualquier objeto que implemente un método 
           'desplazamiento()', sin importar su clase o herencia.
        4. Se recorre la lista con un bucle 'for', y se llama 'vehiculo.desplazamiento()' en cada uno.
           Python ejecuta el método correspondiente según el tipo real del objeto (Moto, Coche o Camion).

    🔹 Ventajas de usar Protocol:
        - No obliga a heredar de una clase base.
        - Permite un tipado más flexible (tipado estructural).
        - Mejora la legibilidad y el autocompletado en editores modernos.

    🔹 Resultado esperado:
        Me desplazo utilizando dos ruedas
        Me desplazo utilizando cuatro ruedas
        Me desplazo utilizando seis ruedas
"""