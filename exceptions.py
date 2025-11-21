# Clases de excepciones personalizadas.

class BibliotecaError(Exception):
    """ Excepcion base para errores de la biblioteca """
    pass


class LimitePrestamosError(BibliotecaError):
    """ Se excedio el limite de prestamos permitidos """
    pass


class TituloInvalidoError(BibliotecaError):
    """ El titulo del libro no es valido """
    pass


class LibroNoDisponibleError(BibliotecaError):
    """ El libro no esta disponible para prestamo """
    pass


class UsuarioNoEncontradoError(BibliotecaError):
    """ El usuario no fue encontrado en el sistema """
    pass