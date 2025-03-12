import tkinter as tk
from tkinter import messagebox, Listbox, Scrollbar

class GestorInformacion:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Información")

        # Etiqueta
        self.label = tk.Label(root, text="Ingrese información:")
        self.label.pack(pady=10)

        # Campo de texto
        self.entry = tk.Entry(root, width=50)
        self.entry.pack(pady=10)

        # Botón "Agregar"
        self.add_button = tk.Button(root, text="Agregar", command=self.agregar_informacion)
        self.add_button.pack(pady=5)

        # Lista para mostrar datos
        self.lista = Listbox(root, width=50, height=10)
        self.lista.pack(pady=10)

        # Barra de desplazamiento
        self.scrollbar = Scrollbar(root)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.lista.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.lista.yview)

        # Botón "Limpiar"
        self.clear_button = tk.Button(root, text="Limpiar", command=self.limpiar)
        self.clear_button.pack(pady=5)

    def agregar_informacion(self):
        # Obtener el texto del campo de entrada.
        info = self.entry.get()
        if info:
            # Agregar la información a la lista
            self.lista.insert(tk.END, info)
            # Limpiar el campo de entrada
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Por favor, ingrese información.")

    def limpiar(self):
        # Limpiar el campo de entrada y la lista
        self.entry.delete(0, tk.END)
        self.lista.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = GestorInformacion(root)
    root.mainloop()