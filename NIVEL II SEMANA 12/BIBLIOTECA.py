# Clase Libro
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"{self.titulo} por {self.autor} (Categoría: {self.categoria}, ISBN: {self.isbn})"

# Clase Usuario
class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []

    def prestar_libro(self, libro):
        self.libros_prestados.append(libro)

    def devolver_libro(self, libro):
        self.libros_prestados.remove(libro)

    def __str__(self):
        return f"Usuario: {self.nombre}, ID: {self.id_usuario}, Libros prestados: {[libro.titulo for libro in self.libros_prestados]}"

# Clase Biblioteca
class Biblioteca:
    def __init__(self):
        self.libros = {}
        self.usuarios = {}
        self.ids_usuarios = set()

    def añadir_libro(self, libro):
        self.libros[libro.isbn] = libro

    def quitar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]

    def registrar_usuario(self, usuario):
        if usuario.id_usuario not in self.ids_usuarios:
            self.usuarios[usuario.id_usuario] = usuario
            self.ids_usuarios.add(usuario.id_usuario)

    def dar_baja_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            del self.usuarios[id_usuario]
            self.ids_usuarios.remove(id_usuario)

    def prestar_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios and isbn in self.libros:
            usuario = self.usuarios[id_usuario]
            libro = self.libros[isbn]
            usuario.prestar_libro(libro)

    def devolver_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios and isbn in self.libros:
            usuario = self.usuarios[id_usuario]
            libro = self.libros[isbn]
            usuario.devolver_libro(libro)

    def buscar_libro(self, criterio, valor):
        resultados = []
        for libro in self.libros.values():
            if (criterio == "titulo" and valor in libro.titulo) or \
               (criterio == "autor" and valor in libro.autor) or \
               (criterio == "categoria" and valor == libro.categoria):
                resultados.append(libro)
        return resultados

    def listar_libros_prestados(self, id_usuario):
        if id_usuario in self.usuarios:
            usuario = self.usuarios[id_usuario]
            return usuario.libros_prestados

# Pruebas del sistema
biblioteca = Biblioteca()

# Añadir libros
libro1 = Libro("El Quijote", "Miguel de Cervantes", "Novela", "1234567890")
libro2 = Libro("Cien Años de Soledad", "Gabriel García Márquez", "Novela", "0987654321")
biblioteca.añadir_libro(libro1)
biblioteca.añadir_libro(libro2)

# Registrar usuarios
usuario1 = Usuario("Juan Pérez", "001")
usuario2 = Usuario("Ana Gómez", "002")
biblioteca.registrar_usuario(usuario1)
biblioteca.registrar_usuario(usuario2)

# Prestar y devolver libros
biblioteca.prestar_libro("001", "1234567890")
biblioteca.devolver_libro("001", "1234567890")

# Buscar libros
resultados = biblioteca.buscar_libro("autor", "Gabriel García Márquez")
for libro in resultados:
    print(libro)

# Listar libros prestados
libros_prestados = biblioteca.listar_libros_prestados("001")
for libro in libros_prestados:
    print(libro)