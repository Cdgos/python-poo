from libros import Libro
from exceptions import UsuarioNoEncontradoError
from usuarios import Usuario

# ------------------- COMPOSICION EJEMPLO ------------------- #

# Diferencias
# Herencia: El usuario es un profesior.
# Composicion: Biblioteca tiene libros, usuarios, etc. Interacturar con varios obtejos por medio
# de una sola clase.

class Biblioteca:
    def __init__(self, name: str) -> None:
        self.name = name
        self.libros: list[Libro] = []
        self.usuarios: list[Usuario] = []

    def libros_disponibles(self):
        return [
            libro.titulo for libro in self.libros if libro.disponible
        ]
    
    def buscar_usuario(self, cedula: str):

        for usuario in self.usuarios:
            if usuario.cedula == cedula:
                return usuario
            
        raise UsuarioNoEncontradoError(f"El usuario con la cedula '{cedula}' no fue encontrado.")