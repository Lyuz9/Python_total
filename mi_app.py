import tkinter as tk
from tkinter import messagebox
import mysql.connector

# datos de conexión
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Lyuz.09@",  # pon tu password si la tienes
    database="mibase"
)

cursor = conexion.cursor()

def guardar():
    nombre = entry_nombre.get()
    edad = entry_edad.get()
    
    if nombre and edad:
        try:
            sql = "INSERT INTO usuarios (nombre, edad) VALUES (%s, %s)"
            valores = (nombre, edad)
            cursor.execute(sql, valores)
            conexion.commit()
            messagebox.showinfo("Éxito", "Datos guardados correctamente")
            entry_nombre.delete(0, tk.END)
            entry_edad.delete(0, tk.END)
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error: {e}")
    else:
        messagebox.showwarning("Atención", "Completa todos los campos")

# interfaz Tkinter
ventana = tk.Tk()
ventana.title("Registro de Usuarios")
ventana.geometry("300x200")

tk.Label(ventana, text="Nombre").pack()
entry_nombre = tk.Entry(ventana)
entry_nombre.pack()

tk.Label(ventana, text="Edad").pack()
entry_edad = tk.Entry(ventana)
entry_edad.pack()

tk.Button(ventana, text="Guardar", command=guardar).pack(pady=10)

ventana.mainloop()

# cerrar conexión al cerrar la app
conexion.close()
