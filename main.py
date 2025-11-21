"""
    - Clases
    - Constructor: init
    - Metodos: tostring, getters, setters.
    - Encapsulamiento


    - Composicion en Python:
    Tecnica que permite crear relaciones entre objetos sin depender de herencias.

"""

# ========================= #
import os
os.system("cls")
# ========================= #

from typing import Protocol

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
        if self.disponible:
            self.disponible = False
            self.__prestamos += 1

            return f"{self.titulo} prestado exitosamente. Total prestamos: {self.__prestamos}"

        return f"{self.titulo} no está disponible."

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

# ------------------- COMPOSICION EJEMPLO ------------------- #

# Diferencias
# Herencia: El usuario es un profesior.
# Composicion: Biblioteca tiene libros, usuarios, etc. Interacturar con varios obtejos por medio
# de una sola clase.

class Biblioteca:
    def __init__(self, name: str) -> None:
        self.name = name
        self.libros: list[Libro] = []
        self.usuarios = []

    def libros_disponibles(self):
        return [
            libro.titulo for libro in self.libros if libro.disponible
        ]


# Composicion:
mi_libro = LibroFisico('Cien años de soledad', 'Gabriel García', '9780307474728', True)
mi_libro_no_disponible = LibroFisico('No Disponible', 'Gabriel García', '123', False)
otro_libro = LibroFisico('El Principito', 'Antoine de Saint-Exupéry', '9780156013987', True)

biblioteca = Biblioteca("Platzi Biblioteca")
biblioteca.libros = [mi_libro, mi_libro_no_disponible, otro_libro]

print(f"Libros disponibles: {biblioteca.libros_disponibles()}")



# Prints: Clases, metodos, encapsulamiento, herencia, etc.
# # Instancias
# mi_libro = Libro('Cien años de soledad', 'Gabriel García', '9780307474728', True)
# otro_libro = Libro('El Principito', 'Antoine de Saint-Exupéry', '9780156013987', True)

# # Encapsulamiento para evitar esto:
# # mi_libro.__prestamos = 10 --> Generara error. Para eso usamos Getters y Setters.

# # Usar metodos
# mi_libro.set_prestamos(10)
# print(mi_libro.get_prestamos())

# print(mi_libro.prestar())
# print(mi_libro.prestar())
# print(mi_libro.devolver())
# print(mi_libro.prestar())

# print(mi_libro.get_prestamos())

# catalogo = [mi_libro, otro_libro]

# for libro in catalogo:
#     print(libro)