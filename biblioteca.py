from libros import Libro

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