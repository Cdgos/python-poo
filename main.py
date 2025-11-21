# Imports orden alfabetico segun PEP8
from biblioteca import Biblioteca
from exceptions import UsuarioNoEncontradoError, LibroNoDisponibleError
from usuarios import  Profesor
from data import data_libros, data_estudiantes
import os
os.system("cls")

biblioteca = Biblioteca("Platzi Biblioteca")

profesor = Profesor("Andres", "123123123")

biblioteca.usuarios = data_estudiantes
biblioteca.libros = data_libros

print("Bienvenido a Platzi Biblioteca\n")

print("Libros disponibles:\n")
for titulo in biblioteca.libros_disponibles():
    print(f"  - {titulo}")

print()

cedula = input("Digite el numero de cedula: ")

try:
    usuario = biblioteca.buscar_usuario(cedula)
    print(usuario)
except UsuarioNoEncontradoError as e:
    print(e) 
    exit()  # ⛔ Detener si el usuario no existe


titulo = input("Digite el titulo del libro: ")

try:
    libro = biblioteca.buscar_titulo(titulo)
    print(f"El libro que seleccionaste es: {libro}")
except LibroNoDisponibleError as e:
    print(e)

resultado = usuario.solicitar_libro(titulo)
print(f"\n{resultado}")

try:
    resultado_prestar = libro.prestar()
    print(f"\n{resultado_prestar}")
except LibroNoDisponibleError as e:
    print(e)
    exit()  # ⛔ Detener si el libro no está disponible

# print("\nUsuarios de la biblioteca:", biblioteca.libros)
# print("\nLibros de la biblioteca:", biblioteca.libros)

# Este no se puede agregar en el listado porque no cumple el protocolo.
# libro = Libro("Titulo de prueba", "Autor de prueba", "1231234", True)

# usuarios: list[SolicitanteProtocol] = [estudiante, estudiante_2, profesor] # Libro no se puede agregar aqui.
# for usuario in usuarios:
#     print(usuario.solicitar_libro("Titulo de ejemplo"))

# try:
#     resultado = estudiante.solicitar_libro(None)
# except BibliotecaError as e:
#     print(f"{e}, {type(e)}")
#     print(f"Error: No se pudo solicitar el libro")

# print("\n")

# resultado = estudiante.solicitar_libro("El Principito")
# print(resultado)

# print("\n")

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

# print(estudiante.solicitar_libro("Python basico"))
# print(estudiante.solicitar_libro("Python intermedio"))
# print(estudiante.solicitar_libro("Python avanzado"))
# print(estudiante.solicitar_libro("Python / Django"))

# print(estudiante.devolver_libro("Python basico"))

# print(estudiante.solicitar_libro("Python FastAPI"))
# print(estudiante.solicitar_libro("Python / Django"))

# print("\n")

# print(profesor.solicitar_libro("Python basico"))
# print(profesor.solicitar_libro("Python intermedio"))
# print(profesor.solicitar_libro("Python avanzado"))
# print(profesor.solicitar_libro("Python / Django"))






# LibroProtocol: prestar y calcular duracion,  LibroFisico y LibroElectronico que cumplan el protocolo.