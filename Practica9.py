class Libro:
    def __init__(self, titulo, autor, anio, genero, isbn):
        # Inicializa un nuevo objeto Libro con los atributos especificados.
        self.titulo = titulo
        self.autor = autor
        self.anio = anio
        self.genero = genero
        self.isbn = isbn

    def __str__(self):
        # Devuelve una representación en cadena del libro.
        return f"{self.titulo}, {self.autor}, {self.anio}, {self.genero}, ISBN: {self.isbn}"


class Inventario:
    def __init__(self):
        # Inicializa un nuevo inventario como una lista vacía de libros.
        self.libros = []

    def agregar_libro(self, libro):
        # Agrega un libro al inventario.
        self.libros.append(libro)

    def eliminar_libro(self, isbn):
        # Elimina un libro del inventario según el ISBN.
        self.libros = [libro for libro in self.libros if libro.isbn != isbn]

    def buscar_libro(self, titulo):
        # Busca un libro en el inventario por su título.
        for libro in self.libros:
            if libro.titulo.lower() == titulo.lower():
                return libro
        return None

    def listar_libros(self):
        # Lista todos los libros en el inventario.
        if not self.libros:
            print("No hay libros en el inventario.")
        else:
            for libro in self.libros:
                print(libro)


def main():
    # Crea una instancia del inventario.
    inventario = Inventario()

    # Agrega ejemplos de libros al inventario.
    libro1 = Libro("Cien Años de Soledad", "Gabriel García Márquez", 1967, "Realismo Mágico", "1234567890")
    libro2 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", 1605, "Novela", "0987654321")
    libro3 = Libro("1984", "George Orwell", 1949, "Distopía", "1122334455")

    inventario.agregar_libro(libro1)
    inventario.agregar_libro(libro2)
    inventario.agregar_libro(libro3)

    # Bucle principal del programa para interactuar con el usuario.
    while True:
        # Muestra el menú de opciones.
        print("\nMenú de opciones:")
        print("1. Agregar libro")
        print("2. Eliminar libro")
        print("3. Buscar libro")
        print("4. Listar libros")
        print("5. Salir")

        # Pide al usuario que elija una opción.
        opcion = input("Elija una opción: ")

        if opcion == '1':
            # Opción para agregar un nuevo libro.
            titulo = input("Título: ")
            autor = input("Autor: ")
            anio = input("Año: ")
            genero = input("Género: ")
            isbn = input("ISBN: ")
            libro = Libro(titulo, autor, anio, genero, isbn)
            inventario.agregar_libro(libro)
            print("Libro agregado.")
        elif opcion == '2':
            # Opción para eliminar un libro por ISBN.
            isbn = input("ISBN del libro a eliminar: ")
            inventario.eliminar_libro(isbn)
            print("Libro eliminado.")
        elif opcion == '3':
            # Opción para buscar un libro por título.
            titulo = input("Título del libro a buscar: ")
            libro = inventario.buscar_libro(titulo)
            if libro:
                print("Libro encontrado:", libro)
            else:
                print("Libro no encontrado.")
        elif opcion == '4':
            # Opción para listar todos los libros en el inventario.
            print("Listado de libros en el inventario:")
            inventario.listar_libros()
        elif opcion == '5':
            # Opción para salir del programa.
            print("Saliendo del programa.")
            break
        else:
            # Mensaje de error para opciones no válidas.
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    # Punto de entrada del programa.
    main()