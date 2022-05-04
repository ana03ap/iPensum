from cgitb import grey
import tkinter as tk
from tkinter import *
from email.mime import image
from tkinter import Entry, StringVar, Widget, font
# CARGAR IMAGENES
# creamos una clase que hereda de frame
# esta es la entrada principal


class MyVentana(Frame):
    """ Gestion de Frames. """

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        """ Initialize the frame. """
        self.pack()
        self.create_widgets()

    # BOTON PARA INICIAR

    def create_widgets(self):
        self.fondo = tk.Label(image=inicio).place(x=0, y=0)  # FRAME
        self.botonS = tk.Button(image=botonSeguir, width=80, cursor="heart",
                                command=self.Menu1, borderwidth=0)
        self.botonS.place(x=767, y=384, height=76)

    def Menu1(self):
        """_summary_
        """
        # La manera en la que desea ingresar (GUEST OR STUDENT)
        for ele in ventana.winfo_children():
            ele.destroy()
        self.interfaz = tk.Canvas(ventana)
        self.interfaz.pack()
        self.fondo = tk.Label(image=main).place(x=0, y=0)  # FRAM
        #self.label1 = tk.Label(self.interfaz, image=main)
        # self.label1.pack()

        # Propiedades del boton, command = Menu2 y command = Menu3 es lo que se debe ejecutar
        # BOTON PARA INVITADOS
        self.botonG = tk.Button(ventana, image=botonGuest, width=150, cursor="heart",
                                command=self.Menu2, borderwidth=0)
        self.botonG.place(x=235, y=400, height=60)
        # BOTON PARA ESTUDIANTES
        self.botonE = tk.Button(ventana, image=botonStudent, width=150, cursor="heart",
                                command=self.Menu3, borderwidth=0)
        self.botonE.place(x=490, y=400, height=60)
        # BOTON INSTRUCCIONES
        self.botonT = tk.Button(ventana, image=botonTuerca, width=44, cursor="heart",
                                borderwidth=0, command=self.MenuInstrucciones)
        self.botonT.place(x=786, y=20, height=52)

    def Menu2(self):  # Al hundir invitado puede inciar su busqueda de forma normal
        for ele in ventana.winfo_children():
            ele.destroy()
        self.interfaz2 = tk.Canvas(ventana)
        self.interfaz2.pack()
        self.fondo = tk.Label(image=busqG).place(x=0, y=0)  # FRAM
        #self.label2 = tk.Label(self.interfaz2, image=busqG)
        # self.label2.pack()

        # RETURN MALLA
        self.botonM = tk.Button(ventana, image=botonMalla,
                                width=190, cursor="heart", borderwidth=0)
        self.botonM.place(x=476, y=287, height=20)
        # RETURN SEMESTRE ESPECIFICO
        self.botonS = tk.Button(
            ventana, image=botonSemestre, width=225, cursor="heart", borderwidth=0)
        self.botonS.place(x=484, y=307, height=49)
        # RETURN ACTIVIDADES EXTRACURRICULARES
        self.botonA = tk.Button(ventana, image=botonActividades,
                                width=310, cursor="heart", borderwidth=0)
        self.botonA.place(x=484, y=350, height=40)
        # RETURN RATING ZONE
        self.botonR = tk.Button(
            ventana, image=botonRating, width=140, borderwidth=0)
        self.botonR.place(x=480, y=391, height=45)

        # BACK TO MAIN
        self.botonB = tk.Button(ventana, image=botonBack, width=60,
                                command=self.Menu1, borderwidth=0)
        self.botonB.place(x=714, y=11, height=72)
        # BOTON INSTRUCCIONES
        self.botonT = tk.Button(ventana, image=botonTuerca, width=44,
                                borderwidth=0, command=self.MenuInstrucciones)
        self.botonT.place(x=778, y=20, height=52)

    def Menu3(self):  # Botón que me lleva al inicio de sesión como estudiante - LOGUEO-
        for ele in ventana.winfo_children():
            ele.destroy()
        self.interfaz3 = tk.Canvas(ventana)
        self.interfaz3.pack()
        self.fondo = tk.Label(image=busqE).place(x=0, y=0)  # FRAM
        # self.label3 = tk.Label(self.interfaz3, image=)
       # self.label3.pack()

        # VALIDAR QUE SOLO META NÚMEROS AL CODIGO ESTUDIANTIL
        def validate_code(text: str):
            return text.isdecimal()

        # CAMPO DE TEXTO PARA LOGUEARSE
        self.entradaUser = StringVar()
        self.campo = Entry(ventana, textvariable=self.entradaUser,
                           width=20, borderwidth=0, font=89).place(x=460, y=279, height=24)
        self.entradaCode = StringVar()
        self.campo2 = Entry(ventana, textvariable=self.entradaCode,
                            width=20, borderwidth=0, font=89, validate="key",
                            validatecommand=(self.register(validate_code), "%S")).place(x=460, y=352, height=24)

        # VALIDAR QUE LOS CAMPOS NO ESTÉN VACIOS, SI LO ESTAN SALDRÁ UNA ADVERTENCIA

        def login():
            c1 = self.entradaUser.get()
            c2 = self.entradaCode.get()
            if(c1 == "" or c2 == ""):  # Campos vacios
                Error = tk.Label(ventana, image=errorC,
                                 borderwidth=0, width=190)
                Error.place(x=447, y=396, height=45)

            else:  # sino esta vacio
                self.Menu4()
                '''
                # no se no me sale 
                #abrir txt de login
                i=0 
                lista = []
                filename = ("txtLogin.txt")
                with open (filename) as file:
                    for lineas in file:
                        lista.append(lineas.split(","))
    
                    for lines in lineas:
                        if c1==lista[i][0] and c2 == lista[i][1]:
                            Menu4()
                            break
                        else:
                            Error = tk.Label(ventana, text= "error", font = 20, fg= "#E41111", bg="#FAFBFD")
                            Error.place(x= 514, y = 410)
                        i=i+1
                '''
        # BOTON LOGIN
        self.boton3 = tk.Button(ventana, image=botonLogin,
                                command=login, width=190, borderwidth=0)
        self.boton3.place(x=620, y=404, height=56)

        # BACK TO MAIN
        self.botonB = tk.Button(ventana, image=botonBack, width=60,
                                command=self.Menu1, borderwidth=0)
        self.botonB.place(x=720, y=11, height=69)
        # BOTON INSTRUCCIONES
        self.botonT = tk.Button(ventana, image=botonTuerca, width=48,
                                borderwidth=0, command=self.MenuInstrucciones)
        self.botonT.place(x=785, y=20, height=52)

    def Menu4(self):  # Botón que me lleva a la busqueda como estudiante
        for ele in ventana.winfo_children():
            ele.destroy()
        self.interfaz = tk.Canvas(ventana)
        self.interfaz.pack()
        self.fondo = tk.Label(image=desplog).place(x=0, y=0)  # FRAM
        #label1 = tk.Label(interfaz, image=desplog)
        # label1.pack()

        # RETURN MALLA
        self.botonM = tk.Button(
            ventana, image=botonMalla, width=190, borderwidth=0)
        self.botonM.place(x=476, y=287, height=20)
        # RETURN SEMESTRE ESPECIFICO
        self.botonS = tk.Button(ventana, image=botonSemestre, width=225,
                                borderwidth=0, command=self.MenuEleccion)
        self.botonS.place(x=484, y=307, height=49)
        # RETURN ACTIVIDADES EXTRACURRICULARES
        self.botonA = tk.Button(ventana, image=botonActividades,
                                width=310, borderwidth=0)
        self.botonA.place(x=484, y=350, height=40)
        # RETURN RATING ZONE
        self.botonR = tk.Button(
            ventana, image=botonRating, width=140, borderwidth=0)
        self.botonR.place(x=480, y=391, height=45)

        # BOTON INSTRUCCIONES
        self.botonT = tk.Button(ventana, image=botonTuerca, width=44,
                                borderwidth=0, command=self.MenuInstrucciones)
        self.botonT.place(x=778, y=20, height=52)

        # BACK TO MENU3 (LOGUEO)
        botonB = tk.Button(ventana, image=botonBack, width=60,
                           command=self.Menu3, borderwidth=0)
        botonB.place(x=710, y=11, height=72)

    def MenuInstrucciones(self):  # Instrucciones de la app
        for ele in ventana.winfo_children():
            ele.destroy()
        self.interfaz = tk.Canvas(ventana)
        self.interfaz.pack()
        self.fondo = tk.Label(image=Instrucciones).place(x=0, y=0)  # FRAM
        #label1 = tk.Label(interfaz, image=Instrucciones)
        # label1.pack()

        botonI = tk.Button(ventana, image=botonIns, width=60,
                           command=self.Menu1, borderwidth=0)
        botonI.place(x=775, y=11, height=72)

    def MenuEleccion(self):  # Elección de semestre que desea ver
        for ele in ventana.winfo_children():
            ele.destroy()
        self.interfaz = tk.Canvas(ventana)
        self.interfaz.pack()
        self.fondo = tk.Label(image=eleccion).place(x=0, y=0)  # FRAM
        #label1 = tk.Label(interfaz, image=eleccion)
        # label1.pack()

        # BOTON PRIMER SEMESTRE
        # BOTON SEGUNDO SEMESTRE
        # BOTON SEGUNDO SEMESTRE
        # BOTON TERCER SEMESTRE
        # BOTON CUARTO SEMESTRE
        # BOTON QUINTO SEMESTRE
        # BOTON INSTRUCCIONES
        self.botonT = tk.Button(ventana, image=botonTuerca, width=44,
                                borderwidth=0, command=self.MenuInstrucciones)
        self.botonT.place(x=778, y=22, height=52)

        # BACK TO MENU4 (LO QUE QUIERE BUSCAR)
        self.botonB = tk.Button(ventana, image=botonBack, width=60,
                                command=self.Menu4, borderwidth=0)
        self.botonB.place(x=710, y=11, height=72)


'''
class Menu2():
    def __init__(self, master=None):
            super().__init__(master)
            self.master = master
            """ Initialize the frame. """
            self.pack()
            self.create_widgets()
            
        # BOTON PARA INICIAR

    def create_widgets(self):
            self.fondo = tk.Label(image=inicio).place(x=0, y=0)  # FRAME
            self.botonS = tk.Button(image=botonSeguir, width=80,cursor="heart",
                                    command=self.Menu1, borderwidth=0)
            self.botonS.place(x=767, y=384, height=76)
       

    def Menu2(self):  # Al hundir invitado puede inciar su busqueda de forma normal
        for ele in self.winfo_children():
            ele.destroy()
        self.interfaz2 = tk.Canvas(ventana)
        self.interfaz2.pack()
        self.label2 = tk.Label(self.interfaz, image=busqG)
        self.label2.pack()

        # RETURN MALLA
        self.botonM = tk.Button(ventana, image=botonMalla, width=190, cursor="heart",borderwidth=0)
        self.botonM.place(x=476, y=287, height=20)
        # RETURN SEMESTRE ESPECIFICO
        self.botonS = tk.Button(ventana, image=botonSemestre, width=225, cursor="heart",borderwidth=0)
        self.botonS.place(x=484, y=307, height=49)
        # RETURN ACTIVIDADES EXTRACURRICULARES
        self.botonA = tk.Button(ventana, image=botonActividades,
                        width=310, cursor="heart",borderwidth=0)
        self.botonA.place(x=484, y=350, height=40)
        # RETURN RATING ZONE
        self.botonR = tk.Button(self, image=botonRating, width=140, borderwidth=0)
        self.botonR.place(x=480, y=391, height=45)

        # BACK TO MAIN
        self.botonB = tk.Button(ventana, image=botonBack, width=60,
                        command=self.Menu1, borderwidth=0)
        self.botonB.place(x=714, y=11, height=72)
        # BOTON INSTRUCCIONES
        self.botonT = tk.Button(self, image=botonTuerca, width=44,
                        borderwidth=0, command=self.MenuInstrucciones)
        self.botonT.place(x=778, y=20, height=52)

class Menu1(MyVentana):
    """ Gestion de Frames. """

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        """ Initialize the frame. """
        

    def create_widgets(self, Menu2):
        # Propiedades del boton, command = Menu2 y command = Menu3 es lo que se debe ejecutar
        for ele in ventana.winfo_children():
            ele.destroy()
        #FONDO
        self.fondo = tk.Label(image=main.place(x=0, y=0))  # FRAME
        # BOTON PARA INVITADOS

        self.botonG = tk.Button(ventana, image=botonGuest, width=150,
                                command=Menu2, borderwidth=0)
        self.botonG.place(x=235, y=400, height=60)
        # BOTON PARA ESTUDIANTES
        self.botonE = tk.Button(ventana, image=botonStudent, width=150,
                                command=Menu3, borderwidth=0)
        self.botonE.place(x=490, y=400, height=60)
        # BOTON INSTRUCCIONES
        self.botonT = tk.Button(ventana, image=botonTuerca, width=44,
                                borderwidth=0, command=MenuInstrucciones)
        self.botonT.place(x=786, y=20, height=52)

        self.menu1.destroy()

class Menu2(Frame):
    pass


class Menu3(Frame):
    pass


class Menu4(Frame):
    pass


class MenuInstrucciones(Frame):
    pass
'''
ventana = tk.Tk()
# cargar imagenes
inicio = tk.PhotoImage(file="inicio.png")
main = tk.PhotoImage(file="main.png")
busqG = tk.PhotoImage(file="busqG.png")
busqE = tk.PhotoImage(file="busqE.png")
desplog = tk.PhotoImage(file="depLog.png")
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
botonIns = tk.PhotoImage(file="botonIns.png")
botonSeguir = tk.PhotoImage(file="botonSeguirmain.png")
eleccion = tk.PhotoImage(file="elegirSemestre.png")

ventana.title("iPensum")
ventana.geometry("870x500")
ventana.resizable(width=0, height=0)

app = MyVentana(master=ventana)
app.mainloop()
