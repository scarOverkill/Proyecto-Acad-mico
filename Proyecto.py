"""
Nombre del programa: Proyecto Programacion #2
Número de grupo de Trabajo: 05
Nombre del equipo de programacion: Team Dynamic
Fecha de elaboración del programa: 12/08/2024
Nombre del Lider Del Grupo: Miguel Alpizar Salazar
Nombres de los integrantes del grupo:
 - Justin Jesus Mendez Calvo
 - Scarlet Molina Lorio
 - Katalina Herrera Gomez
 - Miguel Alpizar Salazar
Versión del PYTHON:3.12
Nombre del IDE donde se trabajó el código: Visual Studio Code
"""

import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import *
from PIL import Image, ImageTk

#Diseño de menú
menu = tk.Tk ()
menu.title("Menú Principal")
menu.geometry("500x500")
menu.configure(background='#ADD8E6')
ancho_pantalla = menu.winfo_screenwidth() 
alto_pantalla = menu.winfo_screenheight() 
ancho_menu = 500
alto_menu = 500
posicion_x = (ancho_pantalla - ancho_menu) // 2
posicion_y = (alto_pantalla - alto_menu) // 2
menu.geometry(f"{ancho_menu}x{alto_menu}+{posicion_x}+{posicion_y}")
etiqueta = tk.Label(menu, text="¡Bienvenidos a Estudia Siempre!", bg="white", fg="#0C84B8", font=("Harrington", 16), width=300, height=2, anchor="center")
etiqueta.pack()

cuaderno = ttk.Notebook (menu)
cuaderno.pack(expand=1, fill="both")

asignaturasframe = tk.Frame (cuaderno)
estudianteframe = tk.Frame (cuaderno)
notas = tk.Frame (cuaderno)

cuaderno.add (asignaturasframe)
cuaderno.add (estudianteframe)
cuaderno.add (notas)

imagen = Image.open("fondo.jpg")
imagen = ImageTk.PhotoImage(imagen)

pestanaActiva = "#FEC798" 
pestanaInactiva = "#0C84B8"

def mostrar_asig():
    boton_estudiante.config(background=pestanaInactiva)
    boton_notas.config(background=pestanaInactiva)
    boton_asignaturas.config(background=pestanaActiva)
    cuaderno.select(asignaturasframe)

def mostrar_estu():
    boton_asignaturas.config(background=pestanaInactiva)
    boton_notas.config(background=pestanaInactiva)
    boton_estudiante.config(background=pestanaActiva)
    cuaderno.select(estudianteframe)

def mostrar_notas():
    boton_estudiante.config(background=pestanaInactiva)
    boton_asignaturas.config(background=pestanaInactiva)
    boton_notas.config(background=pestanaActiva)
    cuaderno.select(notas)





#Botones del menú
boton_asignaturas = tk.Button (menu, text="Asignaturas", width=10, height=1, anchor="center", state="normal", relief="groove",
                          foreground="black",
                          background=pestanaActiva,
                          activeforeground="#0C84B8",
                          activebackground="#FFFFFF",
                          disabledforeground="#BBBABA",
                          command=mostrar_asig )

boton_asignaturas.place(relx=0.0, rely=0.0, anchor='nw', x=50, y=100)


boton_estudiante = tk.Button (menu, text="Estudiante", width=10, height=1, anchor="center", state="normal", relief="groove",
                            foreground="black",
                          background=pestanaInactiva,
                          activeforeground="#0C84B8",
                          activebackground="#FFFFFF",
                          disabledforeground="#BBBABA",
                          command=mostrar_estu)
boton_estudiante.place(relx=0.0, rely=0.0, anchor='n', x=250, y=100)


boton_notas = tk.Button (menu, text="Notas", width=10, height=1, anchor="center", state="normal", relief="groove",
                            foreground="black",
                          background=pestanaInactiva,
                          activeforeground="#0C84B8",
                          activebackground="#FFFFFF",
                          disabledforeground="#BBBABA",
                          command=mostrar_notas)
boton_notas.place(relx=0.0, rely=0.0, anchor='ne', x=450, y=100)


boton_salir = tk.Button (menu, text="Salir", width=10, height=1, anchor="center", state="normal",
                          foreground="#FFFFFF",
                          background="#88BAD0",
                          activeforeground="#88BAD0",
                          activebackground="#FFFFFF",
                          disabledforeground="#88BAD0",command=menu.quit)

boton_salir.place(relx=1.0, rely=1.0, anchor='se', x=-10, y=-10)



"""
///////////////////////////////////////////////////////
DICCIONARIOS
///////////////////////////////////////////////////////
"""

estudiante_dic = {}
asignaturas_dic = {}


"""
///////////////////////////////////////////////////////
FUNCIONES PARA AGREGAR/ELIMINAR/MOSTRAR ESTUDIANTES/
///////////////////////////////////////////////////////
"""

def agregarEstudiante ():
  nombre = ingNombre.get().title()
  edad = ingEdad.get().title()
  cedula = ingCed.get().title()
  
  try:
      edad = int(edad)
  except ValueError:
      messagebox.showerror("Estudiante", "La edad no es valida.")
      return

  if type(edad) == int:
      
    if nombre != "" and edad != "" and cedula != "":
        if cedula not in estudiante_dic:
            estudiante_dic[cedula] = {'edad': edad, 'nombre': nombre}

            estudiante = f"Nombre: {nombre} | Edad: {edad} | Cedula: {cedula}"
            ListasEstudiantes.insert(tk.END, estudiante)
            ingNombre.delete(0,tk.END)
            ingEdad.delete(0,tk.END)
            ingCed.delete(0,tk.END)
            nombEsCom['values'] = list(estudiante_dic.keys())
            messagebox.showinfo("Estudiante", "Estudiante agregado correctamente")
        else:
            messagebox.showerror("Estudiantes", "Este estudiante ya existe")
    else:
         messagebox.showwarning("Estudiantes", "Debes completar todos los campos.")
  else:
    print("La edad no es un numero")

def eliminarEstudiante():
    selecEstudiante = ListasEstudiantes.curselection()

    if selecEstudiante:
        index = selecEstudiante[0]
        estuBorrado = ListasEstudiantes.get(index)
        estudianteSelec = estuBorrado.split(" ")[7]
        if estudianteSelec in estudiante_dic:
            estudiante_dic.pop(estudianteSelec)
        ListasEstudiantes.delete(index)
    nombEsCom['values'] = list(estudiante_dic.keys())
     
"""
///////////////////////////////////////////////////////
FUNCIONES PARA AGREGAR/ELIMINAR/MOSTRAR ASIGNATURAS
///////////////////////////////////////////////////////
"""


def agregarAsignatura():
  codigoAsignatura = ingAsigCod.get().title()
  nombreAsignatura = ingAsigNom.get().title()
  nombreProfesor = ingAsigProf.get().title()
  if codigoAsignatura == "" or nombreAsignatura == "" or nombreProfesor == "":
      messagebox.showwarning("Asignaturas", "Debes completar todos los campos!")
  else:
      if codigoAsignatura not in asignaturas_dic:
        asignaturas_dic[codigoAsignatura] = {'nombreAsignatura': nombreAsignatura, 'nombreProfesor': nombreProfesor}
        asignatura = f"| Codigo: {codigoAsignatura} | Nombre de la asignatura: {nombreAsignatura} | Docente: {nombreProfesor} |"
        ListasAsignaturas.insert(tk.END, asignatura)
        ingAsigCod.delete(0,tk.END)
        ingAsigNom.delete(0,tk.END)
        ingAsigProf.delete(0,tk.END)

        asiEsCom['values'] = list(asignaturas_dic.keys())
        messagebox.showinfo("Asignaturas", "Asignatura Agregada!")
      else:
          messagebox.showerror("Asignaturas", "Esta asignatura ya existe")
def eliminarAsignatura():
    selecAsignatura = ListasAsignaturas.curselection()
    if selecAsignatura:
        index = selecAsignatura[0]
        asigBorrado = ListasAsignaturas.get(index)
        codigoAsignatura = asigBorrado.split(" ")[2] 
        if codigoAsignatura in asignaturas_dic:
            asignaturas_dic.pop(codigoAsignatura)
        ListasAsignaturas.delete(index)
    asiEsCom['values'] = list(asignaturas_dic.keys())



"""
///////////////////////////////////////////////////////
FUNCIONES PARA LAS NOTAS
///////////////////////////////////////////////////////
"""

def asignarNota():
    estSelectN = estSele.get()
    asiSelecN = asigSele.get()
    notaIng = nota.get()

    if notaIng != "":
        
        try:
            notaIng = int(notaIng)
        except ValueError:
            messagebox.showerror("Notas", "Ingrese un valor valido.")
            return
        if notaIng <= 100:

            if estSelectN in estudiante_dic and asiSelecN in asignaturas_dic:
                if 'materias' not in estudiante_dic[estSelectN]:
                    estudiante_dic[estSelectN]['materias'] = {}
                estudiante_dic[estSelectN]['materias'][asiSelecN] = {'nota': notaIng}
                nota.delete(0, tk.END)
                messagebox.showinfo("Notas", f"Nota asignada a {estudiante_dic[estSelectN]['nombre']} en {asignaturas_dic[asiSelecN]['nombreAsignatura']}")
            else:
                messagebox.showerror("Notas", "Selecciona un estudiante y una materia válidos")
        else:
            messagebox.showerror("Notas", "Ingrese una nota menor a 100")
    else:
        messagebox.showerror("Notas", "Ingrese una nota")



def seleccionarEstudiante():
    ceduEstu = idEstudiante.get()
    if ceduEstu in estudiante_dic:
        estudiante = estudiante_dic[ceduEstu]
        detalles = f"Nombre: {estudiante['nombre']}\nEdad: {estudiante['edad']}\nCédula: {ceduEstu}"
        
        materias = estudiante.get('materias', {})
        if materias:
            for codigo_asignatura in materias:
                datos = materias[codigo_asignatura]
                if codigo_asignatura in asignaturas_dic:
                    nombre_asignatura = asignaturas_dic[codigo_asignatura]['nombreAsignatura']
                    detalles += f"\n - Asignatura: {nombre_asignatura}\n   Nota: {datos['nota']}\n "

        else:
            detalles += "\nNo tiene materias asignadas."
        messagebox.showinfo("Estudiante", detalles)
    else:
        messagebox.showerror("Estudiante:", "Este estudiante no existe.")



"""
///////////////////////////////////////////////////////
PESTANA PARA ESTUDIANTES / AGREGAR / ELIMINAR / MOSTRAR
///////////////////////////////////////////////////////
"""

label_imagen = Label(estudianteframe, image=imagen)
label_imagen.image = imagen
label_imagen.pack()

boton_agregarEstu = tk.Button (estudianteframe, text="Agregar", width=10, height=1, anchor="center", state="normal", relief="groove",
                                font=("Helvetica", 8, "bold"),
                          foreground="black",
                          background="#F2C98D",
                          activeforeground="#0C84B8",
                          disabledforeground="#BBBABA", 
                          command=agregarEstudiante)
boton_agregarEstu.place(relx=0.0, rely=0.0, anchor='n', x=345, y=123)

boton_eliminarEstu = tk.Button (estudianteframe, text="Eliminar", width=10, height=1, anchor="center", state="normal", relief="groove",
                          foreground="black",
                          background="orange",
                          activeforeground="orange",
                          activebackground="#FFFFFF",
                          disabledforeground="#BBBABA",
                          command=eliminarEstudiante)
boton_eliminarEstu.place(relx=0.0, rely=0.0, anchor='n', x=450, y=290)

ingNombre = Entry(estudianteframe, width=15, font=("Arial", 8))
ingNombre.place(x=180, y=103)
label_NombEstu = Label (estudianteframe, text="Nombre", width=10, height=1, anchor="center", bg="#a3d4ff").place(relx=0.0, rely=0.0, x=100, y=100)

ingEdad = Entry(estudianteframe, width=15, font=("Arial", 8))
ingEdad.place(x=180, y=123)
label_EdadEstu = Label (estudianteframe, text="Edad", width=10, height=1, anchor="center", bg="#a3d4ff").place(relx=0.0, rely=0.0, x=100, y=120)

ingCed= Entry(estudianteframe, width=15, font=("Arial", 8))
ingCed.place(x=180, y=143)
label_CedulaEstu = Label (estudianteframe, text="Cedula", width=10, height=1, anchor="center", bg="#a3d4ff").place(relx=0.0, rely=0.0, x=100, y=140)

ListasEstudiantes = Listbox(estudianteframe, width=80, height=5)
ListasEstudiantes.place(x=6, y=200)
"""
///////////////////////////////////////////////////////
PESTANA PARA ASIGNATURAS / AGREGAR / ELIMINAR / MOSTRAR
///////////////////////////////////////////////////////
"""

label_imagen = Label(asignaturasframe, image=imagen)
label_imagen.image = imagen
label_imagen.pack()

boton_agregarAsig = tk.Button (asignaturasframe, text="AGREGAR", width=10, height=1, anchor="center", state="normal", relief="groove",
                                font=("Helvetica", 8, "bold"),
                          foreground="black",
                          background="#F2C98D",
                          activeforeground="#5DB1AB",
                          activebackground="#FFFFFF",
                          disabledforeground="#BBBABA",
                          command=agregarAsignatura)
boton_agregarAsig.place(relx=0.0, rely=0.0, anchor='n', x=345, y=123)

boton_eliminarAsig = tk.Button (asignaturasframe, text="Eliminar", width=10, height=1, anchor="center", state="normal", relief="groove",
                          foreground="black",
                          background="orange",
                          activeforeground="orange",
                          activebackground="#FFFFFF",
                          disabledforeground="#BBBABA",
                          command=eliminarAsignatura)
boton_eliminarAsig.place(relx=0.0, rely=0.0, anchor='n', x=450, y=290)

ingAsigCod = Entry(asignaturasframe, width=15, font=("Arial", 8))
ingAsigCod.place(x=180, y=103)
label_idAsignatura = Label (asignaturasframe, text="Codigo", width=10, height=1, anchor="center", bg="#a4d5ff").place(relx=0.0, rely=0.0, x=100, y=100)

ingAsigNom = Entry(asignaturasframe, width=15, font=("Arial", 8))
ingAsigNom.place(x=180, y=123)
label_Asignatura = Label (asignaturasframe, text="Asignatura", width=10, height=1, anchor="center", bg="#a4d5ff").place(relx=0.0, rely=0.0, x=100, y=120)

ingAsigProf= Entry(asignaturasframe, width=15, font=("Arial", 8))
ingAsigProf.place(x=180, y=143)
label_nomProfe = Label (asignaturasframe, text="Docente", width=10, height=1, anchor="center", bg="#a4d5ff").place(relx=0.0, rely=0.0, x=100, y=140)

ListasAsignaturas = Listbox(asignaturasframe, width=80, height=5)
ListasAsignaturas.place(x=6, y=200)

"""
///////////////////////////////////////////////////////
PESTANA DE SELECCIONAR ESTUDIANTE
///////////////////////////////////////////////////////
"""


label_imagen = Label(notas, image=imagen)
label_imagen.image = imagen
label_imagen.pack()

label_separador = Label(notas, text="", width=100, height=15, bg="#F9E6CB", )
label_separador.place(x=1, y=230)
label_separador.lift

idEstudiante = Entry(notas, width=15, font=("Arial", 8))
idEstudiante.place(x=215, y=310)
label_idEstudiante = Label (notas, text="ID", width=3, height=1, anchor="center", bg="#F9E6CB", font=("Helvetica", 8, "bold")).place(relx=0.0, rely=0.0, x=183, y=308)
label_idEstudiante = Label (notas, text="Seleccionar estudiante",bg="#F9E6CB", font=("Helvetica", 8, "bold"), anchor="center").place(relx=0.0, rely=0.0, x=200, y=280)

boton_mostrarEstudiante = tk.Button (notas, text="Mostrar", width=10, height=1, anchor="center", state="normal",relief="groove",
                                font=("Helvetica", 8, "bold"),
                          foreground="black",
                          background="#F2C98D",
                          activeforeground="#5DB1AB",
                          activebackground="#FFFFFF",
                          disabledforeground="#BBBABA",
                          command=seleccionarEstudiante)
boton_mostrarEstudiante.place(relx=0.0, rely=0.0, anchor='n', x=250, y=350)

"""
///////////////////////////////////////////////////////
PESTANA DE NOTAS
///////////////////////////////////////////////////////
"""



estSele = tk.StringVar()
nombEsCom = ttk.Combobox(notas, textvariable=estSele, height=10, width=10)
nombEsCom.place(x=180, y=103)
label_CEstudiante = Label (notas, text="Estudiante",bg="#a3d4ff", anchor=CENTER)
label_CEstudiante.place(x=100, y=100)

asigSele = tk.StringVar()
asiEsCom = ttk.Combobox(notas, textvariable=asigSele, height=10, width=10)
asiEsCom.place(x=180, y=128)
label_CAsignatura = Label (notas, text="Asignatura", bg="#a3d4ff", anchor=CENTER)
label_CAsignatura.place(x=100, y=126)

nota = Entry(notas, width=5)
nota.place(x=180, y=155)
label_nota = Label (notas, text="Nota", bg="#a3d4ff", anchor=CENTER)
label_nota.place(x=120, y=155)

label_Asignar = Label (notas, text="Asignar una nota!", bg="#b0d5ff")
label_Asignar.place(x=210, y=70)
boNota = tk.Button(notas, width=10, height=1, text="Agregar Nota", command=asignarNota, foreground="black", relief="groove",
                          background="#F2C98D", font=("Helvetica", 8, "bold"),
                          activeforeground="#5DB1AB",
                          activebackground="#FFFFFF",
                          disabledforeground="#BBBABA",)
boNota.place(x=205, y=200)



menu.mainloop()