#funcionalidades del programa 
import tkinter as tk

class Funcions():
    # codigo para validar 
    def __init__(self):
        pass

    def print(self):
        print("hola")
        
    def login(self,entradaUser,entradaCode,ventana,errorC, txtL,MenuBusqueda, InvalidCode):
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
    #menu logeo
    def validate_code(self,text: str):
        return text.isdecimal()#verdadero si es numero  
    
    def imprimir_label(self,ventana):
         # ABRIR TXT DE MATERIAS, ESTE ES EL TXT DE LA INFO DE CADA MATERIA EN CADA SEM 
        txtM = []
        with open("archivos/txtSemestre.txt") as fname:
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
     