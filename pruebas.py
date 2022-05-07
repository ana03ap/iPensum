from pickletools import stringnl_noescape_pair
from tkinter import *
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
        if txtM[i][1] == semestre:
            sem.append(txtM[i])
            i = i+1
            sw = 0
        else:
            if sw == 1:
                i = i+1
        #############################################
        """
            w=0
            for l in sem:
                string=""
                for j in sem[w]:#listas una a una
                    string += j + "\n"
                    tk.Label(ventana, bg = "white", text=string,width = 90, height=5, font=("Calibri",14,"italic")).place(x=30,y=30)
                w=w+1


        print (sem)#lista de listas de primer semestre
        print("VAMOS A IMPRIMIR EL SEMESTRE")
        string=""
        string2=""
        string= f"\tMateria Semestre Código Tipo Creditos\n\t{string2.join(sem[0])}\n\t{string2.join(sem[1])}\n\t{string2.join(sem[2])}\n\t{string2.join(sem[3])}"
        
        #print (*sem)
        #for nav in sem:
           # string += nav + "\n"
        #string = " ".join([str(item) for item in sem])
        string
        print ("")
        print ("")
        print (string)
        tk.Label(ventana, bg = "white", text=string,width = 70, justify="left", height=10, font=("Calibri",14,"italic")).place(x=0,y=0)
        ##############################################
"""
# probando con una tabla para que se vea más ordenado

    tv = ttk.Treeview(ventana, columns=("Código", "Tipo", "Créditos"))

    i = 0
    j = 2

    tv.column("#0", width=170)
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

    elif semestre == 'Cuarto semestre':
        # el primer valor va en código, segundo en tió y así )
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


imprimirSemestre(ventana, "Noveno semestre")

ventana.mainloop()
# SEM ES UNA LISTA DE LISTAS
