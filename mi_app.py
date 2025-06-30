import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

# conexión a la base de datos
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Lyuz.09@",
    database="mibase"
)
cursor = conexion.cursor()

# función para guardar usuarios
def guardar_usuario():
    nombre = entry_nombre.get()
    edad = entry_edad.get()
    
    if nombre and edad:
        try:
            sql = "INSERT INTO usuarios (nombre, edad) VALUES (%s, %s)"
            valores = (nombre, edad)
            cursor.execute(sql, valores)
            conexion.commit()
            messagebox.showinfo("Éxito", "Usuario guardado correctamente")
            entry_nombre.delete(0, tk.END)
            entry_edad.delete(0, tk.END)
            mostrar_usuarios()
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error: {e}")
    else:
        messagebox.showwarning("Atención", "Completa todos los campos")

# función para mostrar usuarios
def mostrar_usuarios():
    for row in tabla_usuarios.get_children():
        tabla_usuarios.delete(row)
    cursor.execute("SELECT id, nombre, edad FROM usuarios")
    registros = cursor.fetchall()
    for reg in registros:
        tabla_usuarios.insert("", tk.END, values=reg)

# función para guardar días
def guardar_dias():
    dia = entry_dia.get()
    
    if dia:
        try:
            sql = "INSERT INTO tb_dias (nombre_dia) VALUES (%s)"
            valores = (dia,)
            cursor.execute(sql, valores)
            conexion.commit()
            messagebox.showinfo("Éxito", "Día registrado correctamente")
            entry_dia.delete(0, tk.END)
            mostrar_dias()
            actualizar_combobox_dias()
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error: {e}")
    else:
        messagebox.showwarning("Atención", "Completa el campo correspondiente")

# función para mostrar días
def mostrar_dias():
    for row in tabla_dias.get_children():
        tabla_dias.delete(row)
    cursor.execute("SELECT id, nombre_dia FROM tb_dias")
    registros = cursor.fetchall()
    for reg in registros:
        tabla_dias.insert("", tk.END, values=reg)

# actualizar opciones del combobox de días
def actualizar_combobox_dias():
    cursor.execute("SELECT id, nombre_dia FROM tb_dias")
    dias = cursor.fetchall()
    combo_dias_rutina["values"] = [f"{id_dia} - {nombre}" for id_dia, nombre in dias]

# función para guardar rutina
def guardar_rutina():
    seleccionado = combo_dias_rutina.get()
    if not seleccionado:
        messagebox.showwarning("Atención", "Selecciona un día")
        return

    try:
        id_dia = int(seleccionado.split("-")[0].strip())
    except:
        messagebox.showerror("Error", "Formato de día inválido")
        return

    nombre_rutina = entry_nombre_rutina.get()
    s1 = entry_serie1.get()
    s2 = entry_serie2.get()
    s3 = entry_serie3.get()
    s4 = entry_serie4.get()
    fallo = entry_fallo.get()

    if not nombre_rutina:
        messagebox.showwarning("Atención", "Completa el nombre de la rutina")
        return

    try:
        valores = (
            id_dia,
            nombre_rutina,
            int(s1),
            int(s2),
            int(s3),
            int(s4),
            int(fallo)
        )
        sql = """
        INSERT INTO tb_rutina 
        (id_dia, nombre_rutina, serie1, serie2, serie3, serie4, fallo)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(sql, valores)
        conexion.commit()
        messagebox.showinfo("Éxito", "Rutina registrada correctamente")
        # limpiar
        entry_nombre_rutina.delete(0, tk.END)
        entry_serie1.delete(0, tk.END)
        entry_serie2.delete(0, tk.END)
        entry_serie3.delete(0, tk.END)
        entry_serie4.delete(0, tk.END)
        entry_fallo.delete(0, tk.END)
        mostrar_rutinas()
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {e}")
        
# función para mostrar las rutinas
def mostrar_rutinas():
    for row in tabla_rutinas.get_children():
        tabla_rutinas.delete(row)
    sql = """
    SELECT r.id, d.nombre_dia, r.nombre_rutina, r.serie1, r.serie2, r.serie3, r.serie4, r.fallo
    FROM tb_rutina r
    INNER JOIN tb_dias d ON r.id_dia = d.id
    """
    cursor.execute(sql)
    registros = cursor.fetchall()
    for reg in registros:
        tabla_rutinas.insert("", tk.END, values=reg)

# ventana principal
ventana = tk.Tk()
ventana.title("App con Pestañas")
ventana.geometry("700x400")

# crear notebook (pestañas)
notebook = ttk.Notebook(ventana)
notebook.pack(expand=True, fill="both")

# primera pestaña: registro de usuarios
frame_registro = ttk.Frame(notebook)
notebook.add(frame_registro, text="Registrar Usuario")

# segunda pestaña: lista de usuarios
frame_lista = ttk.Frame(notebook)
notebook.add(frame_lista, text="Lista de Usuarios")

# tercera pestaña: registro de días
frame_dias = ttk.Frame(notebook)
notebook.add(frame_dias, text="Registrar Día")

# cuarta pestaña: lista de días
frame_lista_dias = ttk.Frame(notebook)
notebook.add(frame_lista_dias, text="Lista de Días")

# quinta pestaña: registrar rutina
frame_rutina = ttk.Frame(notebook)
notebook.add(frame_rutina, text="Registrar Rutina")

# sexta pestaña: lista de rutinas
frame_lista_rutinas = ttk.Frame(notebook)
notebook.add(frame_lista_rutinas, text="Lista de Rutinas")

# contenidos de la primera pestaña
ttk.Label(frame_registro, text="Nombre").pack()
entry_nombre = ttk.Entry(frame_registro)
entry_nombre.pack()

ttk.Label(frame_registro, text="Edad").pack()
entry_edad = ttk.Entry(frame_registro)
entry_edad.pack()

ttk.Button(frame_registro, text="Guardar Usuario", command=guardar_usuario).pack(pady=10)

# contenidos de la segunda pestaña
tabla_usuarios = ttk.Treeview(frame_lista, columns=("ID", "Nombre", "Edad"), show="headings")
tabla_usuarios.heading("ID", text="ID")
tabla_usuarios.heading("Nombre", text="Nombre")
tabla_usuarios.heading("Edad", text="Edad")
tabla_usuarios.pack(expand=True, fill="both")

# registro de días
ttk.Label(frame_dias, text="Día de la semana").pack()
entry_dia = ttk.Entry(frame_dias)
entry_dia.pack()

ttk.Button(frame_dias, text="Guardar Día", command=guardar_dias).pack(pady=10)

# consultar días
tabla_dias = ttk.Treeview(frame_lista_dias, columns=("ID", "Día"), show="headings")
tabla_dias.heading("ID", text="ID")
tabla_dias.heading("Día", text="Día")
tabla_dias.pack(expand=True, fill="both")

# registrar rutina
ttk.Label(frame_rutina, text="Día de la semana").pack()
combo_dias_rutina = ttk.Combobox(frame_rutina, state="readonly")
combo_dias_rutina.pack()

ttk.Label(frame_rutina, text="Nombre de la rutina").pack()
entry_nombre_rutina = ttk.Entry(frame_rutina)
entry_nombre_rutina.pack()

ttk.Label(frame_rutina, text="Serie 1").pack()
entry_serie1 = ttk.Entry(frame_rutina)
entry_serie1.pack()

ttk.Label(frame_rutina, text="Serie 2").pack()
entry_serie2 = ttk.Entry(frame_rutina)
entry_serie2.pack()

ttk.Label(frame_rutina, text="Serie 3").pack()
entry_serie3 = ttk.Entry(frame_rutina)
entry_serie3.pack()

ttk.Label(frame_rutina, text="Serie 4").pack()
entry_serie4 = ttk.Entry(frame_rutina)
entry_serie4.pack()

ttk.Label(frame_rutina, text="Fallo").pack()
entry_fallo = ttk.Entry(frame_rutina)
entry_fallo.pack()

ttk.Button(frame_rutina, text="Guardar Rutina", command=guardar_rutina).pack(pady=10)

# tabla de rutinas
tabla_rutinas = ttk.Treeview(
    frame_lista_rutinas,
    columns=("ID", "Día", "Rutina", "S1", "S2", "S3", "S4", "Fallo"),
    show="headings"
)
tabla_rutinas.heading("ID", text="ID")
tabla_rutinas.heading("Día", text="Día")
tabla_rutinas.heading("Rutina", text="Nombre Rutina")
tabla_rutinas.heading("S1", text="Serie1")
tabla_rutinas.heading("S2", text="Serie2")
tabla_rutinas.heading("S3", text="Serie3")
tabla_rutinas.heading("S4", text="Serie4")
tabla_rutinas.heading("Fallo", text="Fallo")
tabla_rutinas.pack(expand=True, fill="both")

# actualizar datos al iniciar
mostrar_usuarios()
mostrar_dias()
actualizar_combobox_dias()
mostrar_rutinas()

ventana.mainloop()
conexion.close()
