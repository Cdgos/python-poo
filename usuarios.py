from typing import Protocol

"""
HERENCIA
    Herencia Simple: 1 sola clase padre y 2 clases hijas

POLIMORFISMO con Protocol.

"""

class SolicitanteProtocol(Protocol):

    # Definicion del Protocolo para poder usarlo dentro de todas las subclases de Usuario.
    def solicitar_libro(self, titulo: str) -> str:
        """ Metodo que debe implementar cualquier solicitante """
        ...

class Usuario:

    def __init__(self, nombre: str, cedula: str):
        self.nombre = nombre
        self.cedula = cedula
        self.libros_prestados: list[str] = []

    def solicitar_libro(self, titulo: str):
        return f"Solicitud de libro '{titulo}' realizada"


# Estudiante Hereda de Usuario
class Estudiante(Usuario):

    def __init__(self, nombre: str, cedula: str, carrera: str):
        """
            “Ejecuta el método __init__ de la clase padre (Usuario) antes de seguir 
            con el código del hijo”.

            super() -> Llama metodos de la clase Padre. 
        """
        super().__init__(nombre, cedula)

        self.carrera = carrera
        self.limite_libros = 3

    def solicitar_libro(self, titulo: str):

        if len(self.libros_prestados) < self.limite_libros:

            # Hereda de Usuario:
            self.libros_prestados.append(titulo)

            return f"Prestamo del libro '{titulo}' autorizado"
        else:
            return f"No puedes prestar más libros. Límite alcanzado: {self.limite_libros}"


    def devolver_libro(self, titulo: str):

        self.libros_prestados.remove(titulo)

        return f"Devolucion del libro '{titulo}' realizada"

class Profesor(Usuario):

    def __init__(self, nombre: str, cedula: str):
        super().__init__(nombre, cedula)

        # El profesor no tiene limite de libros, es distinto al Estudiante.
        self.limite_libros = None

    def solicitar_libro(self, titulo: str):

        if titulo in self.libros_prestados:
            return f"El libro '{titulo}' ya fue prestado"

        # Hereda de Usuario:
        self.libros_prestados.append(titulo)

        return f"Prestamo del libro '{titulo}' autorizado"