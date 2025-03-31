import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas")
        # Campo de entrada.
        self.entry = tk.Entry(root, width=40)
        self.entry.grid(row=0, column=0, padx=10, pady=10)
        self.entry.bind("<Return>", lambda _: self.add_task())

        # Botón para añadir tarea
        self.add_button = tk.Button(root, text="Añadir Tarea", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=10, pady=10)

        # Lista de tareas
        self.task_list = tk.Listbox(root, width=50, height=15, selectmode=tk.SINGLE)
        self.task_list.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        # Botones para completar y eliminar tareas
        self.complete_button = tk.Button(root, text="Completar Tarea", command=self.complete_task)
        self.complete_button.grid(row=2, column=0, padx=10, pady=5)
        self.delete_button = tk.Button(root, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.grid(row=2, column=1, padx=10, pady=5)

        # Atajos de teclado
        self.root.bind("<c>", lambda _: self.complete_task())
        self.root.bind("<Delete>", lambda _: self.delete_task())
        self.root.bind("<d>", lambda _: self.delete_task())
        self.root.bind("<Escape>", lambda _: self.root.quit())

    def add_task(self):
        task = self.entry.get()
        if task.strip():
            self.task_list.insert(tk.END, task)
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Por favor ingresa una tarea válida.")

    def complete_task(self):
        try:
            index = self.task_list.curselection()[0]
            task = self.task_list.get(index)
            self.task_list.delete(index)
            self.task_list.insert(tk.END, f"[COMPLETADA] {task}")
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor selecciona una tarea.")

    def delete_task(self):
        try:
            index = self.task_list.curselection()[0]
            self.task_list.delete(index)
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor selecciona una tarea.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()