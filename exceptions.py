# Clases de excepciones personalizadas.

class BibliotecaError(Exception):
    pass

class TituloInvalidoError(BibliotecaError):
    pass


class LibroError(Exception):
    pass

class LibroNoDisponibleError(LibroError):
    pass