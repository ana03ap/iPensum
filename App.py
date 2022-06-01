# se importan las librerías necesarias
import tkinter as tk
from tkinter import Entry, StringVar, END, Listbox, Button, GROOVE
from Funcionalidades import MallaCurricular, Rating, Actividades, Semestre, Estudiantes

# instanciar objetos
Malla = MallaCurricular()
RatingOb = Rating()
Actividadesob = Actividades()
Semestreob = Semestre()

# Propiedades del frame
ventana = tk.Tk()
ventana.geometry("870x500+230+100")
ventana.title("iPensum")
ventana.resizable(width=0, height=0)

# CARGAR IMAGENES
inicio = tk.PhotoImage(file="imagenes/inicio.png")
# """
main = tk.PhotoImage(file="imagenes/main.png")
Busqueda = tk.PhotoImage(file="imagenes/MenuBusqueda.png")
busqE = tk.PhotoImage(file="imagenes/busqE.png")
errorC = tk.PhotoImage(file="imagenes/CamposVacios.png")
Instrucciones = tk.PhotoImage(file="imagenes/Instrucciones.png")
borrar = tk.PhotoImage(file="imagenes/BotonBorrar.png")
InvalidCode = tk.PhotoImage(file="imagenes/codeInvalid.png")
menuExtra = tk.PhotoImage(file="imagenes/menuExtra.png")
menuRating = tk.PhotoImage(file="imagenes/menuRating.png")
menuEleccion = tk.PhotoImage(file="imagenes/menuEleccion.png")
Warning = tk.PhotoImage(file="imagenes/warning.png")
Twarning = tk.PhotoImage(file="imagenes/taparWarning.png")
menuMalla = tk.PhotoImage(file="imagenes/menuMalla.png")
menuMalla2 = tk.PhotoImage(file="imagenes/menuMalla2.png")
menuMalla3 = tk.PhotoImage(file="imagenes/menuMalla3.png")

# BOTONES
botonSeguir = tk.PhotoImage(file="imagenes/botonSeguirmain.png")
Cerrar = tk.PhotoImage(file="imagenes/BotonClose.png")
botonLogin = tk.PhotoImage(file="imagenes/botonLogin.png")
botonGo = tk.PhotoImage(file="imagenes/botonGo.png")
botonGuest = tk.PhotoImage(file="imagenes/botonGuest.png")
botonStudent = tk.PhotoImage(file="imagenes/botonStudent.png")
botonTuerca = tk.PhotoImage(file="imagenes/botonTuerca.png")
botonBack = tk.PhotoImage(file="imagenes/botonBack.png")
botonMalla = tk.PhotoImage(file="imagenes/botonMalla.png")
botonSemestre = tk.PhotoImage(file="imagenes/botonSemestre.png")
botonActividades = tk.PhotoImage(file="imagenes/botonActividades.png")
botonRating = tk.PhotoImage(file="imagenes/botonRating.png")
botonAgg = tk.PhotoImage(file="imagenes/agg.png")
botonCheck = tk.PhotoImage(file="imagenes/BotonCheck.png")


def MainMenu():  # PRINCIPAL

    fondo = tk.Label(ventana, image=inicio).place(x=0, y=0)  # FRAME
    # BOTON PARA INICIAR
    botonS = tk.Button(ventana, image=botonSeguir, width=80,
                       command=MenuInicial, borderwidth=0, cursor="heart")
    botonS.place(x=767, y=384, height=76)

    # Create a Button to call close()
    tk.Button(ventana, image=borrar, command=close, borderwidth=0,
              width=50, height=50, cursor="heart").place(x=800, y=29)


def MenuInicial():  # La manera en la que desea ingresar (GUEST OR STUDENT)
    for ele in ventana.winfo_children():
        ele.destroy()
    interfaz = tk.Canvas(ventana)
    interfaz.pack()
    label1 = tk.Label(interfaz, image=main)
    label1.pack()

    # Propiedades del boton, command = MenuBusqueda y command = MenuLogueo es lo que se debe ejecutar
    # BOTON PARA INVITADOS
    botonG = tk.Button(ventana, image=botonGuest, width=150,
                       command=MenuBusqueda, cursor="heart", borderwidth=0)
    botonG.place(x=235, y=400, height=60)
    # BOTON PARA ESTUDIANTES
    botonE = tk.Button(ventana, image=botonStudent, width=150,
                       command=MenuLogueo, cursor="heart", borderwidth=0)
    botonE.place(x=490, y=400, height=60)
    # BOTON INSTRUCCIONES
    botonT = tk.Button(ventana, image=botonTuerca, width=44,
                       borderwidth=0, command=MenuInstrucciones, cursor="heart")
    botonT.place(x=786, y=20, height=52)
    # Create a Button to call close()
    tk.Button(ventana, image=Cerrar, command=close, borderwidth=0,
              width=50, height=50, cursor="heart").place(x=10, y=3)


def MenuLogueo():  # Menu que me lleva al inicio de sesión como estudiante - LOGUEO-
    # deberá ingresar un usuario x y su código estudiantil

    for ele in ventana.winfo_children():
        ele.destroy()
    interfaz = tk.Canvas(ventana)
    interfaz.pack()
    label2 = tk.Label(interfaz, image=busqE)
    label2.pack()

    # CAMPO DE TEXTO PARA LOGUEARSE
    entradaUser = StringVar()  # usuario ingresado
    campo = Entry(ventana, textvariable=entradaUser,
                  width=20, borderwidth=0, font=('Bahnschrift SemiBold SemiConden', 14)).place(x=457, y=279, height=24)
    entradaCode = StringVar()  # código ingresado
    campo2 = Entry(ventana, textvariable=entradaCode,
                   width=20, borderwidth=0, font=('Bahnschrift SemiBold SemiConden', 14), validate="key", validatecommand=(ventana.register(Estudiantes.validarCod), "%S")).place(x=457, y=352, height=24)

    # LEER TXT DE LOGUEO PARA VERIFICAR EL CÓDIGO ESTUDIANTIL
    filename = ("archivos_txt/txtLogin.txt")
    with open(filename) as file:
        lines = file.readlines()

    txtL = []
    for x in lines:
        txtL.append(x.rstrip())
    # VALIDAR QUE LOS CAMPOS NO ESTÉN VACIOS, SI LO ESTAN SALDRÁ UNA ADVERTENCIA

    def login():
        user = entradaUser.get()
        code = entradaCode.get()
        if(user == "" or code == ""):  # Campos vacios
            Error = tk.Label(ventana, image=errorC, borderwidth=0, width=190)
            Error.place(x=447, y=394, height=45)

        else:  # Los campos no están vacios
            # Buscar en el txt que ese código sea de la universidad del Norte
            if code in txtL:
                MenuBusqueda()  # Si el código se encuentra que pase a la siguiente
            else:  # Si el código no se encuentra, saldrá en pantalla una advertencia
                Error = tk.Label(ventana, image=InvalidCode,
                                 borderwidth=0, width=194)
                # sino, le sale una advertencia
                Error.place(x=440, y=394, height=45)

    # BOTON LOGIN
    boton3 = tk.Button(ventana, image=botonLogin,
                       command=login, width=190, borderwidth=0, cursor="heart")
    boton3.place(x=620, y=404, height=56)

    # BACK TO MAIN
    botonB = tk.Button(ventana, image=botonBack, width=60,
                       command=MenuInicial, borderwidth=0, cursor="heart")
    botonB.place(x=750, y=11, height=69)

    # Create a Button to call close()
    tk.Button(ventana, image=Cerrar, command=close, borderwidth=0,
              width=50, height=50, cursor="heart").place(x=10, y=3)


def MenuBusqueda():  # En este menu, puede elegir que desea buscar
    for ele in ventana.winfo_children():
        ele.destroy()
    interfaz = tk.Canvas(ventana)
    interfaz.pack()
    label1 = tk.Label(interfaz, image=Busqueda)
    label1.pack()

    # RETURN MALLA
    botonM = tk.Button(ventana, image=botonMalla, width=190,
                       borderwidth=0, command=MenuMalla, cursor="heart")
    botonM.place(x=476, y=284, height=20)
    # RETURN SEMESTRE ESPECIFICO
    botonS = tk.Button(ventana, image=botonSemestre, width=225,
                       borderwidth=0, command=MenuEleccionSemestre, cursor="heart")
    botonS.place(x=482, y=307, height=49)
    # RETURN ACTIVIDADES EXTRACURRICULARES
    botonA = tk.Button(ventana, image=botonActividades,
                       width=310, borderwidth=0, command=MenuActividades, cursor="heart")
    botonA.place(x=482, y=350, height=40)
    # RETURN RATING ZONE
    botonR = tk.Button(ventana, image=botonRating, width=140,
                       borderwidth=0, cursor="heart", command=MenuRating)
    botonR.place(x=480, y=386, height=45)

    # BACK TO MAIN
    botonB = tk.Button(ventana, image=botonBack, width=60,
                       command=MenuInicial, borderwidth=0, cursor="heart")
    botonB.place(x=750, y=11, height=72)

    # Create a Button to call close()
    tk.Button(ventana, image=Cerrar, command=close, borderwidth=0,
              width=50, height=50, cursor="heart").place(x=10, y=3)


def MenuEleccionSemestre():  # Elección de semestre que desea ver
    for ele in ventana.winfo_children():
        ele.destroy()
    interfaz = tk.Canvas(ventana)
    interfaz.pack()
    label1 = tk.Label(interfaz, image=menuEleccion)
    label1.pack()

    def getTextInput():  # Validando lo que ingresa el estudiante
        sw = 0
        result = entrada.get()  # Entrada que ingresa el usuario
        if result == "":  # aca valido que no este vacio
            Error = tk.Label(ventana, image=Warning, borderwidth=0)
            Error.place(x=400, y=240, height=30)

            sw = 1
        if result != "Primer semestre" and result != "Segundo semestre" and result != "Tercer semestre" and result != "Cuarto semestre" and result != "Quinto semestre" and result != "Sexto semestre" and result != "Septimo semestre" and result != "Sexto semestre" and result != "Septimo semestre" and result != "Octavo semestre" and result != "Noveno semestre" and result != "Decimo semestre" and result != "null":
            # aca valido que si este entre primer y decimo semestre
            Error = tk.Label(ventana, image=Warning, borderwidth=0)
            Error.place(x=400, y=240, height=30)
            sw = 1
        if sw == 0:
            tapar = tk.Label(ventana, image=Twarning, borderwidth=0)
            tapar.place(x=400, y=240, height=30)
            if result == "Primer semestre":
                # se crea la tabla por semestre ingresado con los obejtos instanciados de las clases
                Semestreob.mostrarSemestre(label1, result)
            elif result == "Segundo semestre":
                Semestreob.mostrarSemestre(label1, result)
            elif result == "Tercer semestre":
                Semestreob.mostrarSemestre(label1, result)
            elif result == "Cuarto semestre":
                Semestreob.mostrarSemestre(label1, result)
            elif result == "Quinto semestre":
                Semestreob.mostrarSemestre(label1, result)
            elif result == "Sexto semestre":
                Semestreob.mostrarSemestre(label1, result)
            elif result == "Septimo semestre":
                Semestreob.mostrarSemestre(label1, result)
            elif result == "Octavo semestre":
                Semestreob.mostrarSemestre(label1, result)
            elif result == "Noveno semestre":
                Semestreob.mostrarSemestre(label1, result)
            elif result == "Decimo semestre":
                Semestreob.mostrarSemestre(label1, result)
    # Lo que ingresa el estudiante
    entrada = StringVar()
    semestreOP = Entry(ventana, textvariable=entrada, width=45, bg="gray62", borderwidth=0,
                       font=('Bahnschrift SemiBold SemiConden', 14), fg="black").place(x=145, y=187, height=45)
    tk.Button(ventana, height=49, width=57, image=botonCheck, borderwidth=0,
              command=getTextInput).place(x=85, y=185)

    # Back to menu de busqueda, para buscar algo nuevo, es decir, semestre, malla, acts extra, etc.
    botonB = tk.Button(ventana, image=botonBack, width=60,
                       command=MenuBusqueda, borderwidth=0, cursor="heart")
    botonB.place(x=750, y=11, height=72)

    # Create a Button to call close()
    tk.Button(ventana, image=Cerrar, command=close, borderwidth=0,
              width=50, height=50, cursor="heart").place(x=10, y=3)


def MenuMalla():  # Menu cuando haya elegido malla curricular
    for ele in ventana.winfo_children():
        ele.destroy()
    interfaz = tk.Canvas(ventana)
    interfaz.pack()
    label1 = tk.Label(interfaz, image=menuMalla)
    label1.pack()
    # los labels tienen los nombres del semestre correpondiente
    tk.Label(ventana, bg="white", text="• " + Malla.mostrarMalla("1"), width=0, height=0,
             font=("Bahnschrift SemiBold Condensed", 13), justify="left").place(x=90, y=160)

    tk.Label(ventana, bg="white", text="• " + Malla.mostrarMalla("2"), width=0, height=0,
             font=("Bahnschrift SemiBold Condensed", 13), justify="left").place(x=540, y=160)

    tk.Label(ventana, bg="white", text="• " + Malla.mostrarMalla("3"), width=0, height=0,
             font=("Bahnschrift SemiBold Condensed", 13), justify="left").place(x=90, y=340)

    tk.Label(ventana, bg="white", text="• " + Malla.mostrarMalla("4"), width=0, height=0,
             font=("Bahnschrift SemiBold Condensed", 13), justify="left").place(x=540, y=340)

    # Back to menu de busqueda, para buscar algo de nuevo
    botonB = tk.Button(ventana, image=botonBack, width=60,
                       command=MenuBusqueda, borderwidth=0, cursor="heart")
    botonB.place(x=747, y=11, height=69)

    # Create a Button to call close()
    tk.Button(ventana, image=Cerrar, command=close, borderwidth=0,
              width=35, height=40, cursor="heart").place(x=6, y=3)

    # Go to other plantilla
    botonB = tk.Button(ventana, image=botonGo, width=60,
                       borderwidth=0, cursor="heart", command=MenuMalla2)
    botonB.place(x=806, y=22, height=55)


def MenuMalla2():  # Menu cuando haya elegido que desea ver la malla
    for ele in ventana.winfo_children():
        ele.destroy()
    interfaz = tk.Canvas(ventana)
    interfaz.pack()
    label1 = tk.Label(interfaz, image=menuMalla2)
    label1.pack()

    # los labels tienen los nombres del semestre correpondiente
    tk.Label(ventana, bg="white", text="• " + Malla.mostrarMalla("5"), width=0, height=0,
             font=("Bahnschrift SemiBold Condensed", 13), justify="left").place(x=90, y=155)

    tk.Label(ventana, bg="white", text="• " + Malla.mostrarMalla("6"), width=0, height=0,
             font=("Bahnschrift SemiBold Condensed", 13), justify="left").place(x=540, y=155)

    tk.Label(ventana, bg="white", text="• " + Malla.mostrarMalla("7"), width=0, height=0,
             font=("Bahnschrift SemiBold Condensed", 13), justify="left").place(x=90, y=340)

    tk.Label(ventana, bg="white", text="• " + Malla.mostrarMalla("8"), width=0, height=0,
             font=("Bahnschrift SemiBold Condensed", 13), justify="left").place(x=540, y=340)

    # Back to menu de busqueda, para buscar algo de nuevo
    botonB = tk.Button(ventana, image=botonBack, width=60,
                       command=MenuMalla, borderwidth=0, cursor="heart")
    botonB.place(x=747, y=11, height=69)

    # Create a Button to call close()
    tk.Button(ventana, image=Cerrar, command=close, borderwidth=0,
              width=35, height=40, cursor="heart").place(x=6, y=3)

    # Se dirige para el siguiente menu donde se encuentran los otros semestres
    botonB = tk.Button(ventana, image=botonGo, width=60,
                       borderwidth=0, cursor="heart", command=MenuMalla3)
    botonB.place(x=806, y=22, height=55)


def MenuMalla3():  # Menu cuando haya elegido que desea ver la mall

    for ele in ventana.winfo_children():
        ele.destroy()
    interfaz = tk.Canvas(ventana)
    interfaz.pack()
    label1 = tk.Label(interfaz, image=menuMalla3)
    label1.pack()
    # los labels tienen los nombres del semestre correpondiente
    tk.Label(ventana, bg="white", text="• " + Malla.mostrarMalla("9"), width=0, height=0,
             font=("Bahnschrift SemiBold Condensed", 13), justify="left").place(x=90, y=180)

    tk.Label(ventana, bg="white", text="• " + Malla.mostrarMalla("10"), width=0, height=0,
             font=("Bahnschrift SemiBold Condensed", 13), justify="left").place(x=540, y=180)

    # Back to menu de busqueda, para buscar algo de nuevo
    botonB = tk.Button(ventana, image=botonBack, width=60,
                       command=MenuMalla2, borderwidth=0, cursor="heart")
    botonB.place(x=750, y=11, height=69)

    # Create a Button to call close()
    tk.Button(ventana, image=Cerrar, command=close, borderwidth=0,
              width=35, height=40, cursor="heart").place(x=6, y=3)


def MenuActividades():  # Menu de actividades extracurriculares
    for ele in ventana.winfo_children():
        ele.destroy()
    interfaz = tk.Canvas(ventana)
    interfaz.pack()
    label1 = tk.Label(interfaz, image=menuExtra)
    label1.pack()

    # Imprimir la información del txt como string
    Actividadesob.mostrarActividades(ventana)

    # BACK TO MAIN
    botonB = tk.Button(ventana, image=botonBack, width=60,
                       command=MenuBusqueda, borderwidth=0, cursor="heart")
    botonB.place(x=750, y=11, height=69)

    # Create a Button to call close()
    tk.Button(ventana, image=Cerrar, command=close, borderwidth=0,
              width=50, height=50, cursor="heart").place(x=10, y=3)


def MenuRating():  # Menu de rating zone
    for ele in ventana.winfo_children():
        ele.destroy()
    interfaz = tk.Canvas(ventana)
    interfaz.pack()
    label1 = tk.Label(interfaz, image=menuRating)
    label1.pack()

    # Imprimir la información del txt como string
    RatingOb.mostrarRating(ventana)

    # Permite al usuario agregar sus materias favoritas
    def addSubject():
        mat = entrada.get()
        if mat != "":
            lstMaterias.insert(END, entrada.get())

    lstMaterias = Listbox(ventana, width=33, height=8, bg="gray77",
                          relief=GROOVE, bd=0, font=('Ubuntu', 12, "italic"))
    lstMaterias.place(x=490, y=270)
    entrada = StringVar()

    txtMateria = Entry(ventana, textvariable=entrada, width=24, bg="gray61", borderwidth=0, font=(
        'Ubuntu', 12, "italic"), fg="gray20").place(x=525, y=235)
    btnAgregar = Button(ventana, image=botonAgg, height=40, width=40,
                        command=addSubject, borderwidth=0).place(x=750, y=226)

    # BACK TO MAIN
    botonB = tk.Button(ventana, image=botonBack, width=60,
                       command=MenuBusqueda, borderwidth=0, cursor="heart")
    botonB.place(x=750, y=11, height=69)

    # Create a Button to call close()
    tk.Button(ventana, image=Cerrar, command=close, borderwidth=0,
              width=35, height=30, cursor="heart").place(x=10, y=5)


def MenuInstrucciones():  # Interfaz de instrucciones de la app

    for ele in ventana.winfo_children():
        ele.destroy()
    interfaz = tk.Canvas(ventana)
    interfaz.pack()
    label1 = tk.Label(interfaz, image=Instrucciones)
    label1.pack()

    # Boton back
    botonB = tk.Button(ventana, image=botonBack, width=60,
                       command=MenuInicial, borderwidth=0, cursor="heart")
    botonB.place(x=45, y=11, height=72)
    # Create a Button to call close()
    tk.Button(ventana, image=Cerrar, command=close, borderwidth=0,
              width=35, height=50, cursor="heart").place(x=10, y=3)


def close():   # Cerrar ventana hundiendo la x en la esquina superior izquierda
    # ventana.destroy()
    ventana.quit()


MainMenu()
ventana.mainloop()
