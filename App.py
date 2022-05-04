import code
from email.mime import image
import tkinter as tk
from tkinter import Entry, Menu, StringVar, Widget, font
from cv2 import split


# Propiedades del frame
ventana = tk.Tk()
ventana.geometry("870x500+230+100")
ventana.title("iPensum")
ventana.resizable(width=0, height=0)

# CARGAR IMAGENES
inicio = tk.PhotoImage(file="inicio.png")
main = tk.PhotoImage(file="main.png")
Busqueda = tk.PhotoImage(file="MenuBusqueda.png")
busqE = tk.PhotoImage(file="busqE.png")
botonGuest = tk.PhotoImage(file="botonGuest.png")
botonStudent = tk.PhotoImage(file="botonStudent.png")
botonTuerca = tk.PhotoImage(file="botonTuerca.png")
botonBack = tk.PhotoImage(file="botonBack.png")
botonMalla = tk.PhotoImage(file="botonMalla.png")
botonSemestre = tk.PhotoImage(file="botonSemestre.png")
botonActividades = tk.PhotoImage(file="botonActividades.png")
botonRating = tk.PhotoImage(file="botonRating.png")
errorC = tk.PhotoImage(file="CamposVacios.png")
botonLogin = tk.PhotoImage(file="botonLogin.png")
Instrucciones = tk.PhotoImage(file="Instrucciones.png")
botonSeguir = tk.PhotoImage(file="botonSeguirmain.png")
eleccion = tk.PhotoImage(file="elegirSemestre.png")
borrar = tk.PhotoImage(file="BotonBorrar.png")
InvalidCode = tk.PhotoImage(file="codeInvalid.png")
semPlantilla = tk.PhotoImage(file="semestrePlantilla.png")

# BOTONES 
BotonPrimer = tk.PhotoImage(file="BotonPrimer.png")
BotonSegundo = tk.PhotoImage(file="BotonSegundo.png")
BotonTercero = tk.PhotoImage(file="BotonTercero.png")
BotonCuarto = tk.PhotoImage(file="BotonCuarto.png")
BotonQuinto = tk.PhotoImage(file="BotonQuinto.png")
BotonSexto = tk.PhotoImage(file="BotonSexto.png")
BotonSeptimo = tk.PhotoImage(file="BotonSeptimo.png")
BotonOctavo = tk.PhotoImage(file="BotonOctavo.png")
BotonNoveno = tk.PhotoImage(file="BotonNoveno.png")
BotonDecimo = tk.PhotoImage(file="BotonDecimo.png")


# NOTAAAAAAAA  -> font=("Calibri",14,"bold")


def MainMenu(): #PRINCIPAL

    fondo = tk.Label(ventana, image=inicio).place(x=0, y=0)  # FRAME
    # BOTON PARA INICIAR
    botonS = tk.Button(ventana, image=botonSeguir, width=80,
                       command=Menu1, borderwidth=0, cursor="heart")
    botonS.place(x=767, y=384, height=76)

    # Create a Button to call close()
    tk.Button(ventana, image=borrar, command=close, borderwidth=0,
              width=50, height=50, cursor="heart").place(x=800, y=29)

def Menu1():  # La manera en la que desea ingresar (GUEST OR STUDENT)
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

def MenuLogueo():  # Menu que me lleva al inicio de sesión como estudiante - LOGUEO-

    for ele in ventana.winfo_children():
        ele.destroy()
    interfaz = tk.Canvas(ventana)
    interfaz.pack()
    label2 = tk.Label(interfaz, image=busqE)
    label2.pack()

    # VALIDAR QUE SOLO META NÚMEROS AL CODIGO ESTUDIANTIL
    def validate_code(text: str):
        return text.isdecimal()

    # CAMPO DE TEXTO PARA LOGUEARSE
    entradaUser = StringVar()
    campo = Entry(ventana, textvariable=entradaUser,
                  width=20, borderwidth=0, font=('Ubuntu', 14, "italic")).place(x=457, y=279, height=24)
    entradaCode = StringVar()
    campo2 = Entry(ventana, textvariable=entradaCode,
                   width=20, borderwidth=0, font=('Ubuntu', 14, "italic"), validate="key", validatecommand=(ventana.register(validate_code), "%S")).place(x=457, y=352, height=24)

    # LEER TXT DE LOGUEO PARA STUDENT
    filename = ("txtLogin.txt")
    with open(filename) as file:
        lines = file.readlines()

    txtL = []
    for x in lines:
        txtL.append(x.rstrip())
    # print (txtL) # lista con los códigos estudiantiles

    # VALIDAR QUE LOS CAMPOS NO ESTÉN VACIOS, SI LO ESTAN SALDRÁ UNA ADVERTENCIA

    def login():
        user = entradaUser.get()
        code = entradaCode.get()
        if(user == "" or code == ""):  # Campos vacios
            Error = tk.Label(ventana, image=errorC, borderwidth=0, width=190)
            Error.place(x=447, y=394, height=45)

        else:  # sino esta vacio
            # Buscar en el txt que ese código sea de la universidad del Norte
            if code in txtL:
                MenuBusqueda()  # Si el código se encuentra que pase a la siguiente
            else:
                Error = tk.Label(ventana, image=InvalidCode,
                                 borderwidth=0, width=194)
                # sino, el sale una advertencia
                Error.place(x=440, y=394, height=45)

    # BOTON LOGIN
    boton3 = tk.Button(ventana, image=botonLogin,
                       command=login, width=190, borderwidth=0, cursor="heart")
    boton3.place(x=620, y=404, height=56)

    # BACK TO MAIN
    botonB = tk.Button(ventana, image=botonBack, width=60,
                       command=Menu1, borderwidth=0, cursor="heart")
    botonB.place(x=750, y=11, height=69)

def MenuBusqueda():  # En este menu, puede elegir que desea buscar 
    for ele in ventana.winfo_children():
        ele.destroy()
    interfaz = tk.Canvas(ventana)
    interfaz.pack()
    label1 = tk.Label(interfaz, image= Busqueda)
    label1.pack()

    # RETURN MALLA
    botonM = tk.Button(ventana, image=botonMalla, width=190,
                       borderwidth=0, cursor="heart")
    botonM.place(x=476, y=284, height=20)
    # RETURN SEMESTRE ESPECIFICO
    botonS = tk.Button(ventana, image=botonSemestre, width=225,
                       borderwidth=0, command=MenuEleccionSemestre, cursor="heart")
    botonS.place(x=482, y=307, height=49)

    # RETURN ACTIVIDADES EXTRACURRICULARES
    botonA = tk.Button(ventana, image=botonActividades,
                       width=310, borderwidth=0, cursor="heart")
    botonA.place(x=482, y=350, height=40)
    # RETURN RATING ZONE
    botonR = tk.Button(ventana, image=botonRating, width=140,
                       borderwidth=0, cursor="heart")
    botonR.place(x=480, y=389, height=45)

    # BACK TO MAIN
    botonB = tk.Button(ventana, image=botonBack, width=60,
                       command=Menu1, borderwidth=0, cursor="heart")
    botonB.place(x=750, y=11, height=72)

def MenuEleccionSemestre():  # Elección de semestre que desea ver
    for ele in ventana.winfo_children():
        ele.destroy()
    interfaz = tk.Canvas(ventana)
    interfaz.pack()
    label1 = tk.Label(interfaz, image=eleccion)
    label1.pack()

    # BOTON PRIMER SEMESTRE
    botonPrimer = tk.Button(ventana, image=BotonPrimer, width=90,
                            height=85, command=MenuSemestre, borderwidth=0, cursor="heart")
    botonPrimer.place(x=190, y=250)
    # BOTON SEGUNDO SEMESTRE
    botonSegundo = tk.Button(ventana, image=BotonSegundo,
                             width=90, height=89, command=MenuSemestre, borderwidth=0, cursor="heart")
    botonSegundo.place(x=290, y=245)
    # BOTON TERCER SEMESTRE
    botonTercero = tk.Button(ventana, image=BotonTercero,
                             width=95, height=87, command=MenuSemestre, borderwidth=0, cursor="heart")
    botonTercero.place(x=387, y=247)
    # BOTON CUARTO SEMESTRE
    botonCuarto = tk.Button(ventana, image=BotonCuarto, width=95,
                            height=85, command=MenuSemestre, borderwidth=0, cursor="heart")
    botonCuarto.place(x=480, y=247)
    # BOTON QUINTO SEMESTRE
    botonQuinto = tk.Button(ventana, image=BotonQuinto, width=90,
                            height=87, command=MenuSemestre, borderwidth=0, cursor="heart")
    botonQuinto.place(x=580, y=246)
    # BOTON SEXTO SEMESTRE
    botonSexto = tk.Button(ventana, image=BotonSexto, width=90,
                           height=89, command=MenuSemestre, borderwidth=0, cursor="heart")
    botonSexto.place(x=184, y=338)
    # BOTON SEPTIMO SEMESTRE
    botonSeptimo = tk.Button(ventana, image=BotonSeptimo, width=85,
                             height=89, command=MenuSemestre, borderwidth=0, cursor="heart")
    botonSeptimo.place(x=290, y=338)
    # BOTON OCTAVO SEMESTRE
    botonOctavo = tk.Button(ventana, image=BotonOctavo, width=87,
                            height=87, command=MenuSemestre, borderwidth=0, cursor="heart")
    botonOctavo.place(x=388, y=338)
    # BOTON NOVENO SEMESTRE
    botonNoveno = tk.Button(ventana, image=BotonNoveno, width=90,
                            height=87, command=MenuSemestre, borderwidth=0, cursor="heart")
    botonNoveno.place(x=488, y=340)
    # BOTON DECIMO SEMESTRE
    botonDecimo = tk.Button(ventana, image=BotonDecimo, width=92,
                            height=89, command=MenuSemestre, borderwidth=0, cursor="heart")
    botonDecimo.place(x=583, y=338)

    # BACK TO MENU4 (LO QUE QUIERE BUSCAR)
    botonB = tk.Button(ventana, image=botonBack, width=60,
                       command=MenuBusqueda, borderwidth=0, cursor="heart")
    botonB.place(x=750, y=11, height=72)

def MenuSemestre():  # Dependiendo de que semestre escoga, saldrá información acerca de esto
    for ele in ventana.winfo_children():
        ele.destroy()
    interfaz = tk.Canvas(ventana)
    interfaz.pack()
    label1 = tk.Label(interfaz, image=semPlantilla)
    label1.pack()
    
    # BACK TO MENU ESCOGENCIA (LO QUE QUIERE BUSCAR)
    botonB = tk.Button(ventana, image=botonBack, width=60,
                    command=MenuEleccionSemestre, borderwidth=0, cursor="heart")
    botonB.place(x=757, y= 7, height=72)

    ##############################################
    # ABRIR TXT DE MATERIAS, ESTE ES EL TXT DE LA INFO DE CADA MATERIA EN CADA SEM
        
    txtM = []
    with open("txtSemestre.txt") as fname:
        for lineas in fname:
            txtM.append(lineas.split(","))
    i = 0
    sw = 1
    sem = []
    for lines in lineas:
        # ES IGUAL A XXXX SEMESTRE (SIRVE CON TODOS)
        if txtM[i][1] == "Sexto semestre":
            sem.append(txtM[i])
            i = i+1
            sw = 0
        else:
            if sw == 1:
                i = i+1
        #############################################
    print (sem)
    string = " ".join([str(item) for item in sem[0]])
    print ("")
    print ("")
    print (string)
    tk.Label(ventana, bg = "white", text=string,width = 90, height=2, font=("Calibri",14,"italic")).place(x=0,y=380)
    ##############################################


def MenuInstrucciones():  # Instrucciones de la app

    for ele in ventana.winfo_children():
        ele.destroy()
    interfaz = tk.Canvas(ventana)
    interfaz.pack()
    label1 = tk.Label(interfaz, image=Instrucciones)
    label1.pack()

    # Boton back
    botonB = tk.Button(ventana, image=botonBack, width=60,
                       command=Menu1, borderwidth=0, cursor="heart")
    botonB.place(x=11, y=11, height=72)

def close():   # Cerrar ventana en donde estemos
    # ventana.destroy()
    ventana.quit()


'''
def MenuMalla (): #Menu cuando haya elegido que desea ver la malla 
    for ele in ventana.winfo_children():
        ele.destroy()
    interfaz = tk.Canvas(ventana)
    interfaz.pack()
    label1 = tk.Label(interfaz, image= #debe ser malla)
    label1.pack()
    
'''

# def MenuActividades ():
# def MenuRating():

MainMenu()
ventana.mainloop()
