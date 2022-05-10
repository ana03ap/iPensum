from pickletools import stringnl_noescape_pair
from tkinter import *
from tkinter import font

from cv2 import BORDER_WRAP
# de aquí importo todo ## esto es supuestame te una mala practica
from Funcionalidades import *
import tkinter as tk
ventana = tk.Tk()
ventana.geometry("870x500+230+100")
ventana.title("iPensum")
#ventana.resizable(width=0, height=0)

# funcionalidades = Functions() #objeto de la clase Functions

#funcionalidades.imprimirSemestre(ventana,"Primer semestre")


# la varia semestre es la que me dice en qué semetsre se oprimió.
def imprimirSemestre(ventana, semestre: str):

    from tkinter import ttk
    # ABRIR TXT DE MATERIAS, ESTE ES EL TXT DE LA INFO DE CADA MATERIA EN CADA SEM
    txtM = []
    with open("archivos_txt/txtSemestre.txt") as fname:
        for lineas in fname:
            txtM.append(lineas.split(","))
    i = 0
    sw = 1
    sem = []  # lista de listas, cada index es una materia con todas sus caracteristicas
    # print(sem[5])

    for lines in lineas:
        # ES IGUAL A XXXX SEMESTRE (SIRVE CON TODOS)
        print(txtM[i][1])
        if txtM[i][1] == semestre:
            sem.append(txtM[i])
            i = i+1
            sw = 0
        else:
            if sw == 1:
                i = i+1
        #############################################
        

# probando con una tabla para que se vea más ordenado

    tv = ttk.Treeview(ventana, columns=("Código", "Tipo", "Créditos"), selectmode="none")
    
   
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

    tv.pack()
 # para imprimir los labes de rating, actividades, etc


imprimirSemestre(ventana, "Tercer semestre")

ventana.mainloop()
# SEM ES UNA LISTA DE LISTAS
