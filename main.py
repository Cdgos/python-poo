# Imports orden alfabetico segun PEP8
from biblioteca import Biblioteca
from libros import LibroFisico
from usuarios import Estudiante, Profesor, SolicitanteProtocol
import os
os.system("cls")

biblioteca = Biblioteca("Platzi Biblioteca")

# Polimorfismo segun el usuario, solicita un libro.
estudiante = Estudiante("Sebastian", "1192892619", "Ingeniera de Sistemas")
estudiante_2 = Estudiante("Johan", "213123", "Profesor")
profesor = Profesor("Andres", "123123123")

# Este no se puede agregar en el listado porque no cumple el protocolo.
# libro = Libro("Titulo de prueba", "Autor de prueba", "1231234", True)

usuarios: list[SolicitanteProtocol] = [estudiante, estudiante_2, profesor] # Libro no se puede agregar aqui.

for usuario in usuarios:
    print(usuario.solicitar_libro("Titulo de ejemplo"))

# Composicion:
mi_libro = LibroFisico('Cien años de soledad', 'Gabriel García', '9780307474728', True)
mi_libro_no_disponible = LibroFisico('No Disponible', 'Gabriel García', '123', False)
otro_libro = LibroFisico('El Principito', 'Antoine de Saint-Exupéry', '9780156013987', True)

biblioteca.libros = [mi_libro, mi_libro_no_disponible, otro_libro]

print(biblioteca.libros)



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