from email.mime import image
import tkinter as tk
from tkinter import Entry, StringVar

ventana = tk.Tk()
ventana.geometry("870x500")
ventana.title("iPensum")

# CARGAR IMAGENES
main = tk.PhotoImage(file="main.png")
busqG = tk.PhotoImage(file="busqG.png")
busqE = tk.PhotoImage(file="busqE.png")
desplog = tk.PhotoImage(file="depLog.png")


#MAIN
def MainMenu():
    fondo = tk.Label(ventana, image=main).place(x=0, y=0)  #FRAME

    #Propiedades del boton, command = Menu2 es lo que se debe ejecutar 
    boton = tk.Button(ventana, text="GUEST", width=12,
                      command=Menu2, font=60, bg="gray70")
    boton.place(x=240, y=420)

    boton2 = tk.Button(ventana, text="STUDENT", width=13,
                       command=Menu3, font=60, bg="gray70")
    boton2.place(x=490, y=420)


def Menu2():  # Boton que me lleva al inicio de sesión como invitado, al hundir invitado puede inciar su busqueda de forma normal
    for ele in ventana.winfo_children():
        ele.destroy()
    interfaz = tk.Canvas(ventana)
    interfaz.pack()
    label1 = tk.Label(interfaz, image=busqG)
    label1.pack()

    #Menú desplegable para elegir que desea observar
    var = tk.StringVar(ventana)
    opciones = ["Malla curricular", "Semestre específico",
                "Actividades extra", "Rating de materias en Ing de sistemas"]
    opcion = tk.OptionMenu(ventana, var, *opciones)
    opcion.pack()
    opcion.place(x=450, y=250, width=340)

    # BACK TO MAIN
    botonback = tk.Button(ventana, text="BACK", width=5,
                          command=MainMenu, font=60, bg="gray70")
    botonback.place(x=640, y=30)


def Menu4():  #Botón que me lleva a la busqueda de algo como estudiante
    for ele in ventana.winfo_children():
        ele.destroy()
    interfaz = tk.Canvas(ventana)
    interfaz.pack()
    label2 = tk.Label(interfaz, image=desplog)
    label2.pack()
    #Menú desplegable
    var = tk.StringVar(ventana)
    opciones = ["Malla curricular", "Semestre específico",
                "Actividades extra", "Rating de materias en Ing de sistemas"]
    opcion = tk.OptionMenu(ventana, var, *opciones)
    opcion.pack()
    opcion.place(x=450, y=250, width=340)
    #BACK TO MENU3
    botonback = tk.Button(ventana, text="BACK", width=5,
                          command=Menu3, font=60, bg="gray70")
    botonback.place(x=640, y=30)


def Menu3():  #Botón que me lleva al inicio de sesión como estudiante (cuando hunda estudiante, debe loguearse copiando el codigo y su usuario (no se ha hecho) para que pueda iniciar su busqueda)
    for ele in ventana.winfo_children():
        ele.destroy()
    interfaz = tk.Canvas(ventana)
    interfaz.pack()
    label2 = tk.Label(interfaz, image=busqE)
    label2.pack()

    #CAMPO DE TEXTO PARA LOGUEARSE
    entradaCode = StringVar()
    campo = Entry(ventana, textvariable=entradaCode,
                  width=40, bg="white").place(x=460, y=275, height=20)
    entradaUser = StringVar()
    campo2 = Entry(ventana, textvariable=entradaUser,
                   width=40, bg="white").place(x=460, y=350, height=20)

    #Comando boton Login, validar campos vacios
    def login():

        c1 = entradaCode.get()
        c2 = entradaUser.get()
        if(c1 == "" or c2 == ""):  # Campos vacios
            Error = tk.Label(ventana, text="Campos vacios",
                             font=20, fg="black", bg="#FAFBFD")
            Error.place(x=450, y=410)
            print("lslsl")
        else:
            Menu4()

    #BOTON LOGIN
    boton3 = tk.Button(ventana, text="LOGIN", command=login,
                       width=15, font=60, bg="gray70")
    boton3.place(x=639, y=404, height=56)

    #BACK TO MAIN
    botonback = tk.Button(ventana, text="BACK", width=5,
                          command=MainMenu, font=60, bg="gray70")
    botonback.place(x=640, y=30)


MainMenu()
ventana.mainloop()
