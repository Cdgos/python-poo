from typing import Protocol
from exceptions import LibroNoDisponibleError

"""
    - Clases
    - Constructor: init
    - Metodos: tostring, getters, setters.
    - Encapsulamiento
    - Composicion en Python:
    Tecnica que permite crear relaciones entre objetos sin depender de herencias.

"""

class LibroProtocol(Protocol):

    def prestar(self) -> str:
        """ Metodo de prestar un libro """
        ...

    def devolver(self) -> str:
        """ Metodo de devolver un libro """
        ...

    def calcular_duracion(self) -> str:
        """ Metodo de calcular duracion de prestamo de un libro """
        ...


class Libro:

    # Constructor
    def __init__(self, titulo: str, autor: str, isbn: str, disponible: bool):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = disponible
        # Encapsulamiento: doble _ para evitar que accedan.
        self.__prestamos = 0

    # Metodos

    # Metodo toString: return --> str.
    def __str__(self):
        return f"{self.titulo} por {self.autor}, disponible: {self.disponible}"

    # Una buena practica es que los metodos retorne.
    def prestar(self):

        if not self.disponible:
            raise LibroNoDisponibleError(f"El libro con titulo {self.titulo} no se encuentra disponible.")

        self.disponible = False
        self.__prestamos += 1

        return f"{self.titulo} prestado exitosamente. Total prestamos: {self.__prestamos}"

    def devolver(self):
        self.disponible = True

        return f"{self.titulo} devuelto y disponible nuevamente."
    
    def es_popular(self):
        return self.__prestamos > 5
    
    # Metodos Getter y Setter:
    def get_prestamos(self):
        return self.__prestamos
    
    def set_prestamos(self, prestamos: int):
        self.__prestamos = prestamos


class LibroFisico(Libro):
    def calcular_duracion(self):
        return "7 dias"


class LibroDigital(Libro):
    def calcular_duracion(self):
        return "14 dias"