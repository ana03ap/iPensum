# Funcionalidades del programa con programación orientada a objetos 
import tkinter as tk
from tkinter import Entry,  StringVar, END, CENTER


class Estudiantes():
    def __init__(self, text):  #Text es el código
        self.text = text

    def validarCod(text: str):
        return text.isdecimal()  # Devuelve verdadero si es numero

    def login(ventana, MenuBusqueda):  #Para verificar si el estudiante si pertenece a la universidad
        errorC = tk.PhotoImage(file="imagenes/CamposVacios.png")
        InvalidCode = tk.PhotoImage(file="imagenes/codeInvalid.png")

        entradaUser = StringVar()
        campo = Entry(ventana, textvariable=entradaUser,
                      width=20, borderwidth=0, font=('Bahnschrift SemiBold SemiConden', 14)).place(x=457, y=279, height=24)
        entradaCode = StringVar()
        campo2 = Entry(ventana, textvariable=entradaCode,
                       width=20, borderwidth=0, font=('Bahnschrift SemiBold SemiConden', 14), validate="key", validatecommand=(ventana.register(Estudiantes.validarCod), "%S")).place(x=457, y=352, height=24)  # se exporta y queda la función llamada desde estudiantes

        # Leer txt de logueo para estudiantes 
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

            else:  # El campo esta vacío
                # Buscar en el txt que ese código sea de la universidad del Norte
                if code in txtL:
                    MenuBusqueda()  # Si el código se encuentra que pase a la siguiente
                else:
                    Error = tk.Label(ventana, image=InvalidCode,
                                     borderwidth=0, width=194)
                    # Sino, le sale una advertencia
                    Error.place(x=440, y=394, height=45)


class MallaCurricular():

    def mostrarMalla(self, semestre: str):  # Imprime la malla completa
        malla = []

        with open("archivos_txt/txtMalla.txt") as fname:
            for lineas in fname:
                m = Materia(0, 0, lineas.split(",")[0], lineas.split(
                    ",")[1], 0, 0)  # se instancia un objeto
                m = [m.semestre, m.nombreMat]  # se vuelve a la
                malla.append(m)
        i = 0
        sw = 1
        global sem
        sem = []  # Lista de listas, cada index es una materia con todas sus caracteristicas

        for lines in malla:
            # Es igual a xxx semestre (funciona para todos)
            print(malla[i][0])
            if malla[i][0] == semestre:
                sem.append(malla[i][1])
                i = i+1  # Entra a la lista de x semestre y empieza a iterar dentro
                sw = 0
            else:
                if sw == 1:  # Cuando es x semestre, sw=1 pero i sigue iterando
                    i = i+1
        # Convertir a string la información del txt 
        string = "• ".join([str(item) for item in sem])
        return string


class Semestre():

    # Imprime semestre por semestre dependiendo del input ingresado
    def mostrarSemestre(self, label1, semestre: str):
        from tkinter import ttk
        # Se abre el txt de materias 
        txtS = []
        with open("archivos_txt/txtSemestre.txt") as fname:
            for lineas in fname:
                m = Materia(lineas.split(",")[2], lineas.split(",")[3], lineas.split(",")[
                            1], lineas.split(",")[0], lineas.split(",")[4], 0)  # se instancia un objeto
                m = [m.nombreMat, m.semestre, m.codigoM,
                     m.tipoM, m.numeroCred]  # se vuelve a la
                txtS.append(lineas.split(","))
        i = 0
        sw = 1
        sem = []  # lista de listas, cada index es una materia con todas sus caracteristicas

        for lines in txtS:
            # ES IGUAL A XXXX SEMESTRE (SIRVE CON TODOS)
            if txtS[i][1] == semestre:
                sem.append(txtS[i])
                i = i+1  # entra a la lista de x semestre y empieza a iterar dentro
                sw = 0
            else:
                if sw == 1:  # cuando es x semestre, sw=1 pero i sigue iterando
                    i = i+1

        # Imprimir semestre con una tabla

        tv = ttk.Treeview(label1, columns=("Código", "Tipo", "Créditos"),
                          selectmode="none", cursor="heart", height=6, show="tree headings", style="Foo2.Treeview")
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
        # El primer valor va en código, segundo en tipo etc
        tv.insert("", END, text=sem[i][0], values=(
            sem[i][j], sem[0][j+1], sem[0][j+2]))
        # El primer valor va en código, segundo en tipo etc
        tv.insert("", END, text=sem[i+1][0],
                  values=(sem[i+1][j], sem[i+1][j+1], sem[i+1][j+2]))
        # El primer valor va en código, segundo en tipo etc
        tv.insert("", END, text=sem[i+2][0],
                  values=(sem[i+2][j], sem[i+2][j+1], sem[i+2][j+2]))
        # El primer valor va en código, segundo en tipo etc
        tv.insert("", END, text=sem[i+3][0],
                  values=(sem[i+3][j], sem[i+3][j+1], sem[i+3][j+2]))
        # El primer valor va en código, segundo en tipo etc
        tv.insert("", END, text=sem[i+4][0],
                  values=(sem[i+4][j], sem[i+4][j+1], sem[i+4][j+2]))

        # Estos semestres tiene más materias, por lo que se agrega otra fila
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
        tv.place(x=200, y=270)

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview",
                        background="silver",
                        foreground="black",
                        rowheight=30,
                        fieldbackground="silver")


class Actividades():
    # Imprime las actividades que se pueden realizar
    def mostrarActividades(self, ventana):
        with open("archivos_txt/txtActividadesExtra.txt") as fname:
            lines = fname.readlines()
            # Conver list to str
        string = "".join([str(item) for item in lines])
        tk.Label(ventana, bg="white", text=string, width=50, height=10,
                 font=("Bahnschrift SemiBold Condensed", 16), justify="left").place(x=310, y=218)


class Rating():  # Clase rating 
    def mostrarRating(self, ventana):
        # Imprimir la información del txt como string
        with open("archivos_txt/txtRating.txt") as fname:
            lines = fname.readlines()
     # Conver list to str
        string = "• ".join([str(item) for item in lines])
        tk.Label(ventana, bg="gray77", text="• " + string, width=30, height=6,
                 font=("Bahnschrift SemiBold SemiConden", 15), justify="left").place(x=80, y=257)

    def addSubject(self, entrada, lstMaterias):  # agrega materias que el usuario escriba
        mat = entrada.get()
        if mat != "":
            lstMaterias.insert(END, entrada.get())


class Materia(): # Clase materia, los atributos es la información de básica que se dece conocer acerca de cada materia 
    def __init__(self, codigoM, tipoM, semestre, nombreMat, numeroCred, preferencia):
        self.codigoM = codigoM
        self.tipoM = tipoM
        self.semestre = semestre
        self.nombreMat = nombreMat
        self.numeroCred = numeroCred



class Electiva(Materia):  #Clase electivas, la cual herede de materia porque las electivas tambien son materias 

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

    def __init__(self, nombreElect, tipoM, semestre):
        super().__init__(tipoM, semestre)
        self.nombreElect = nombreElect


class Obligatoria(Materia): #Clase obligatorias la cual herede de materia porque las obligatorias tambien son materias 
    def __init__(self, nombreA, tipoM, semestre):
        super().__init__(tipoM,semestre)
        self.nombreA = nombreA
