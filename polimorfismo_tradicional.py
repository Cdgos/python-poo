# ========================= #
import os
os.system("cls")
# ========================= #

# Polimorfismo (poli => muchas / morfos: formas)

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
# miVehiculo.desplazamiento()

miVehiculo2 = Coche()
# miVehiculo2.desplazamiento()

miVehiculo3 = Camion()
# miVehiculo3.desplazamiento()

def desplazamientoVehiculo(vehiculo: Vehiculo):
    vehiculo.desplazamiento()


desplazamientoVehiculo(miVehiculo)
desplazamientoVehiculo(miVehiculo2)
desplazamientoVehiculo(miVehiculo3)

"""
    En este ejemplo se demuestra el concepto de POLIMORFISMO en programación orientada a objetos.
    "Polimorfismo" proviene del griego y significa "muchas formas". En este contexto, se refiere a que 
    diferentes clases pueden compartir un mismo método (mismo nombre), pero con comportamientos distintos 
    dependiendo del objeto que lo invoque.

    - Se define una clase base llamada 'Vehiculo' que contiene el método 'desplazamiento()', pero sin 
      implementación (solo un 'pass').
    - Luego se crean tres clases hijas: 'Coche', 'Moto' y 'Camion', que heredan de 'Vehiculo' y cada una 
      redefine el método 'desplazamiento()' con su propio comportamiento.
    - Gracias al polimorfismo, una misma función llamada 'desplazamientoVehiculo()' puede recibir 
      cualquier objeto que sea de tipo 'Vehiculo' (o una subclase suya) y ejecutar el método 
      correspondiente según el tipo real del objeto pasado.

    En otras palabras:
        - Si se pasa un objeto de tipo Moto → ejecuta el desplazamiento de Moto.
        - Si se pasa un objeto de tipo Coche → ejecuta el desplazamiento de Coche.
        - Si se pasa un objeto de tipo Camion → ejecuta el desplazamiento de Camion.

    Además, en la definición de la función:
        def desplazamientoVehiculo(vehiculo: Vehiculo):
    se usa una ANOTACIÓN DE TIPO (type hint), indicando que el parámetro 'vehiculo' debe ser un objeto 
    de tipo 'Vehiculo' o de alguna clase que herede de ella.

    Esto mejora la legibilidad y ayuda a detectar errores con herramientas de análisis estático,
    pero en tiempo de ejecución Python sigue siendo dinámico, es decir, no obliga estrictamente el tipo.

    Resultado esperado:
        Me desplazo utilizando dos ruedas
        Me desplazo utilizando cuatro ruedas
        Me desplazo utilizando seis ruedas
"""
