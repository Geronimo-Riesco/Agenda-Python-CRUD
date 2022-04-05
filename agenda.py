# Importo todo de la libreria Tkinter
from tkinter import *
from tkinter import messagebox
from sqliteBD import *

# Declaro mis constantes
ANCHO = 560
ALTO = 550
POSX = 400
POSY = 400

# Variables con las caracteristicas de la ventana
anchoAlto = str(ANCHO) + "x" + str(ALTO)
posicionX = "+" + str(POSX)
posicionY = "+" + str(POSY)
colorVentana = "light green"
colorLetra = "white"

# Funciones para darle interactividad

def mostrarMensaje(titulo, mensaje):
    messagebox.showinfo(titulo, mensaje)

def limpiarDatos():
    Id.set("")
    nombre.set("")
    apellido.set("")
    telefono.set("")
    direccion.set("")
    text.delete(1.0, END)

def guardar():
    crearTabla()
    if ((nombre.get() == "") or (apellido.get() == "")):
        mostrarMensaje("Error", "Debes rellenar los datos")
    else:
        datos = nombre.get(), apellido.get(), telefono.get(), direccion.get()
        mostrarMensaje("Guardar", "Contacto guardado")
        insertar(datos)
        limpiarDatos()
        mostrar()

def eliminar():
    if ((Id.get() == "") or (Id.get() == 0)):
        mostrarMensaje("Error", "Debes insertar un identificador válido")
    else:
        try:
            borrar(Id.get())
            mostrarMensaje("Borrar", "Contacto borrado")
            limpiarDatos()
            mostrar()
        except:
            mostrarMensaje("Error", "Identificador no encontrado")

def mostrar():
    listado = consultar()
    text.delete(1.0, END)
    text.insert(INSERT, "ID\tNombre\tApellido\tTeléfono\t\tDirección\n")
    for elemento in listado:
        Id = elemento[0]
        nombre = elemento[1]
        apellido = elemento[2]
        telefono = elemento[3]
        direccion = elemento[4]
        text.insert(INSERT, Id)
        text.insert(INSERT, "\t")
        text.insert(INSERT, nombre)
        text.insert(INSERT, "\t")
        text.insert(INSERT, apellido)
        text.insert(INSERT, "\t")
        text.insert(INSERT, telefono)
        text.insert(INSERT, "\t")
        text.insert(INSERT, direccion)
        text.insert(INSERT, "\n")

def actualizar():
    crearTabla()
    if ((Id.get() == "") or (Id.get() == 0) or (nombre.get() == "")):
        mostrarMensaje("Error", "Debes rellenar los datos")
    else:
        try:
            modificar(Id.get(), nombre.get(), apellido.get(),
                      telefono.get(), direccion.get())
            mostrarMensaje("Modificar", "Contacto modificado")
            limpiarDatos()
            mostrar()
        except:
            mostrarMensaje("Error", "Identificador no encontrado")

# Preparacion de la ventana y frame interior
ventana = Tk()
ventana.config(bg=colorVentana)
ventana.geometry(anchoAlto + posicionX + posicionY)
ventana.title("Agenda G&G Solutions")
frame = Frame()
frame.config(width=ANCHO, height=ALTO)
frame.config(bg=colorVentana)
frame.pack()

# Variables con los datos que vamos a guardar en la Base de Datos
Id = IntVar()
nombre = StringVar()
apellido = StringVar()
telefono = StringVar()
direccion = StringVar()

# Widgets (Entradas a las cajas de texto y botones que nesecitamos)
etiquetaID = Label(frame, text="ID : ").place(x=50, y=50)
cajaID = Entry(frame, textvariable=Id).place(x=130, y=50)
etiquetaNombre = Label(frame, text="Nombre : ").place(x=50, y=90)
cajaNombre = Entry(frame, textvariable=nombre).place(x=130, y=90)
etiquetaApellido = Label(frame, text="Apellido : ").place(x=50, y=130)
cajaApellido = Entry(frame, textvariable=apellido).place(x=130, y=130)
etiquetaTelefono = Label(frame, text="Teléfono : ").place(x=50, y=170)
cajaTelefono = Entry(frame, textvariable=telefono).place(x=130, y=170)
etiquetaDireccion = Label(frame, text="Dirección : ").place(x=50, y=210)
cajaDireccion = Entry(frame, textvariable=direccion).place(x=130, y=210)
text = Text(frame)
text.place(x=50, y=255, width=450, height=230)
botonAñadir = Button(frame, text="Añadir", command=guardar).place(x=147, y=500)
botonBorrar = Button(frame, text="Borrar",
                     command=eliminar).place(x=210, y=500)
botonConsultar = Button(frame, text="Consultar",
                        command=mostrar).place(x=270, y=500)
botonActualizar = Button(frame, text="Actualizar",
                         command=actualizar).place(x=348, y=500)
ventana.mainloop()
