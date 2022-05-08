# funcionalidades del programa
import tkinter as tk
from tkinter import *


class Functions():
    # codigo para validar
    """ 
    def __init__(self,entradaUser,entradaCode,ventana,errorC, txtL ,MenuBusqueda, InvalidCode, text):
        self.entradaUser = entradaUser
        self.entradaCode = entradaCode
        self.ventana = ventana
        self.errorC =  errorC
        self.text=text
"""

    def printear(self):
        print("hola")

    def login(self, entradaUser, entradaCode, ventana, errorC, txtL, MenuBusqueda, InvalidCode):
        self.user = self.entradaUser.get()
        self.code = self.entradaCode.get()
        if(self.user == "" or self.code == ""):  # Campos vacios
            self.Error = tk.Label(ventana, image=errorC,
                                  borderwidth=0, width=190)
            self.Error.place(x=447, y=394, height=45)

        else:  # sino esta vacio
            # Buscar en el txt que ese código sea de la universidad del Norte
            if self.code in txtL:
                MenuBusqueda()  # Si el código se encuentra que pase a la siguiente
            else:
                Error = tk.Label(ventana, image=InvalidCode,
                                 borderwidth=0, width=194)
                # sino, el sale una advertencia
                Error.place(x=440, y=394, height=45)

    # VALIDAR QUE SOLO META NÚMEROS AL CODIGO ESTUDIANTIL
    # menu logeo
    def validate_code(self, text: str):
        return self.text.isdecimal()  # verdadero si es numero

    # para abrir el archivo y que imprima dependiendo al semestre selecionado

    def imprimirSemestre(self, label1, semestre: str):
        from tkinter import ttk

        # ABRIR TXT DE MATERIAS, ESTE ES EL TXT DE LA INFO DE CADA MATERIA EN CADA SEM
        txtM = []
        with open("archivos_txt/txtSemestre.txt") as fname:
            for lineas in fname:
                txtM.append(lineas.split(","))
        i = 0
        sw = 1
        sem = []  # lista de listas, cada index es una materia con todas sus caracteristicas

        for lines in lineas:
            # ES IGUAL A XXXX SEMESTRE (SIRVE CON TODOS)
            if txtM[i][1] == semestre:
                sem.append(txtM[i])
                i = i+1
                sw = 0
            else:
                if sw == 1:
                    i = i+1
            

    # probando con una tabla para que se vea más ordenado

        tv = ttk.Treeview(label1, columns=("Código", "Tipo", "Créditos"),
                          selectmode="none", cursor="heart")

        i = 0
        j = 2

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
        tv.place(x=80,y=210)
        #tv.pack()


""""
inicializamos la clase
class Alumno:
    # inicializamos los atributos
  def inicializar(self,nombre,nota):
      self.nombre=nombre
      self.nota=nota
 
 
    # función para imprimir los datos
  def imprimir(self):
      print("Nombre: ",self.nombre)
      print("Nota: ",self.nota)
 
 
    # función para obtener el resultado
  def resultado(self):
      if self.nota < 5:
                              print("El alumno ha suspendido")
      else:
                              print("El alumno ha aprobado")
 
 
 
     """
