# funcionalidades del programa
import tkinter as tk
from tkinter import *

class Estudiantes():  # si me sirve
    def __init__(self, text):  # text es el código
        self.text = text

    def validar_cod(text: str):
        return text.isdecimal()  # devuelve verdadero si es numero

    def login(ventana, MenuBusqueda):
        errorC = tk.PhotoImage(file="imagenes/CamposVacios.png")
        InvalidCode = tk.PhotoImage(file="imagenes/codeInvalid.png")

        entradaUser = StringVar()
        campo = Entry(ventana, textvariable=entradaUser,
                      width=20, borderwidth=0, font=('Bahnschrift SemiBold SemiConden', 14)).place(x=457, y=279, height=24)
        entradaCode = StringVar()
        campo2 = Entry(ventana, textvariable=entradaCode,
                       width=20, borderwidth=0, font=('Bahnschrift SemiBold SemiConden', 14), validate="key", validatecommand=(ventana.register(Estudiantes.validar_cod), "%S")).place(x=457, y=352, height=24)  # se exporta y queda la función llamada desde estudiantes

    # LEER TXT DE LOGUEO PARA STUDENT
        filename = ("archivos_txt/txtLogin.txt")
        with open(filename) as file:
            lines = file.readlines()

        txtL = []
        for x in lines:
            txtL.append(x.rstrip())
            user = entradaUser.get()
            code = entradaCode.get()
            if(user == "" or code == ""):  # Campos vacios
                Error = tk.Label(ventana, image=errorC,
                                 borderwidth=0, width=190)
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


class Login():# no sirve
    def __init__(self, user, code, ventana, errorC, txtL, InvalidCode):
        self.user= user
        self.code = code
        self.ventana = ventana
        self.errorC =  errorC
        self.txtL = txtL
        self.InvalidCode = InvalidCode

    def login(entradaUser, entradaCode, ventana, errorC, txtL, MenuBusqueda, InvalidCode):

     
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
    # VALIDAR QUE SOLO META NÚMEROS AL CODIGO ESTUDIANTIL
    # menu logeo
    
class MallaCurricular:
    #ListMat[]
     def imprimirSemestre(self, label1, semestre: str):
        from tkinter import ttk

        # ABRIR TXT DE MATERIAS, ESTE ES EL TXT DE LA INFO DE CADA MATERIA EN CADA SEM
        txtM = []
        with open("archivos_txt/txtSemestre.txt") as fname:
            for lineas in fname:
                txtM.append(lineas.split(","))
        i = 0
        sw = 1
        verificar = 0
        sem = []  # lista de listas, cada index es una materia con todas sus caracteristicas

        for lines in txtM:
            # ES IGUAL A XXXX SEMESTRE (SIRVE CON TODOS)
            if txtM[i][1] == semestre:
                sem.append(txtM[i])
                i = i+1 #entra a la lista de x semestre y empieza a iterar dentro 
                sw = 0
            else:
                if sw == 1: #cuando es x semestre, sw=1 pero i sigue iterando 
                    i = i+1

        # probando con una tabla para que se vea más ordenado

        tv = ttk.Treeview(label1, columns=("Código", "Tipo", "Créditos"),
                          selectmode= "none", cursor="heart", height= 6, show="tree headings", style="Foo2.Treeview")

        i = 0

        tv.column("#0", width=250)
        tv.column("Código", width=80, anchor=CENTER)
        tv.column("Tipo", width=80, anchor=CENTER)
        tv.column("Créditos", width=80, anchor=CENTER)

        tv.heading("#0", text="Materia", anchor=CENTER)
        tv.heading("Código", text="Código", anchor=CENTER)
        tv.heading("Tipo", text="Tipo", anchor=CENTER)
        tv.heading("Créditos", text="Créditos", anchor=CENTER)
        j = 2
        # el primer valor va en código, segundo en tió y así
        tv.insert("", END, text=sem[i][0], values=(
            sem[i][j], sem[0][j+1], sem[0][j+2]))
        # el primer valor va en código, segundo en tió y así )
        tv.insert("", END, text=sem[i+1][0],
                  values=(sem[i+1][j], sem[i+1][j+1], sem[i+1][j+2]))
        # el primer valor va en código, segundo en tió y así )
        tv.insert("", END, text=sem[i+2][0],
                  values=(sem[i+2][j], sem[i+2][j+1], sem[i+2][j+2]))
        # el primer valor va en código, segundo en tió y así )
        tv.insert("", END, text=sem[i+3][0],
                  values=(sem[i+3][j], sem[i+3][j+1], sem[i+3][j+2]))
        # el primer valor va en código, segundo en tió y así )
        tv.insert("", END, text=sem[i+4][0],
                  values=(sem[i+4][j], sem[i+4][j+1], sem[i+4][j+2]))

        if semestre == 'Cuarto semestre':
            tv.insert(
                "", END, text=sem[i+5][0], values=(sem[i+5][j], sem[i+5][j+1], sem[i+5][j+2]))

        elif semestre == 'Quinto semestre':
            tv.insert(
                "", END, text=sem[i+5][0], values=(sem[i+5][j], sem[i+5][j+1], sem[i+5][j+2]))

        elif semestre == 'Octavo semestre':
            tv.insert(
                "", END, text=sem[i+5][0], values=(sem[i+5][j], sem[i+5][j+1], sem[i+5][j+2]))

        elif semestre == 'Noveno semestre':
            tv.insert(
                "", END, text=sem[i+5][0], values=(sem[i+5][j], sem[i+5][j+1], sem[i+5][j+2]))
            tv.insert(
                "", END, text=sem[i+6][0], values=(sem[i+6][j], sem[i+6][j+1], sem[i+6][j+2]))
        tv.place(x=200,y=270)
        
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview",
                        background = "silver",
                        foreground="black",
                        rowheight = 30, 
                        fieldbackground = "silver")

     def imprimirMalla(self,semestre:str):
        # abrir el txt 
        # ABRIR TXT DE MATERIAS, ESTE ES EL TXT DE LA INFO DE CADA MATERIA EN CADA SEM
        txtM = []
        with open("archivos_txt/txtMalla.txt") as fname:
            for lineas in fname:
                    txtM.append(lineas.split(","))
        i = 0
        sw = 1
        sem = []  # lista de listas, cada index es una materia con todas sus caracteristicas

        for lines in txtM:
                # ES IGUAL A XXXX SEMESTRE (SIRVE CON TODOS)
            if txtM[i][0] == semestre:
                    sem.append(txtM[i][1])
                    i = i+1 #entra a la lista de x semestre y empieza a iterar dentro 
                    sw = 0
            else:
                    if sw == 1: #cuando es x semestre, sw=1 pero i sigue iterando 
                        i = i+1

        string = "• ".join([str(item) for item in sem])
        return string

class Actividades():
    def imprimirActividades(ventana):
        with open("archivos_txt/txtActividadesExtra.txt") as fname:
         lines = fname.readlines()
         # Conver list to str
        string = "".join([str(item) for item in lines])
        tk.Label(ventana, bg="white", text=string, width=50, height=10,
             font=("Bahnschrift SemiBold Condensed", 16), justify="left").place(x=310, y=218)


 
     
class Materia:
    def __init__(self, codigoM, tipoM, semestre, nombreMat, numeroCred, preferencia):
        self.codigoM = codigoM
        self.tipoM = tipoM
        self.semestre = semestre
        self.nombreMat = nombreMat
        self.numeroCred = numeroCred
        self.preferencia = preferencia


class Electiva(Materia):  # ver si es importante agregar la lista electivas

    Electivas = ["Elect. en historia",
                 "Elect. en humanidades ",
                 "Elect. ciencias de la vida",
                 "Elect. en ciencias básicas",
                 "Elect. básica profesional ",
                 "Elect. en ética",
                 "Elect. en ciencias sociales",
                 "Elect. innovación DLLO y SOC",
                 "Elect. profesional I ",
                 "Elect. en redes ",
                 "Elect. en filosofía",
                 "Elect. CS de la computación ",
                 "Elect. gestión informática",
                 "Elect. profesional II",
                 "Elect. estudios del Caribe",
                 "Elect. profesional III"]

    def __init__(self, nombreElect, tipoM, preferencia, semestre):
        super().__init__(tipoM, preferencia, semestre)
        self.nombreElect = nombreElect


class Obligatoria(Materia):
    def __init__(self, nombreA, tipoM, preferencia, semestre):
        super().__init__(tipoM, preferencia, semestre)
        self.nombreA = nombreA