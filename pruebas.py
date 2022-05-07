from pickletools import stringnl_noescape_pair
from  Funcionalidades import * # de aquí importo todo ## esto es supuestame te una mala practica
ventana = tk.Tk()
ventana.geometry("870x500+230+100")
ventana.title("iPensum")
#ventana.resizable(width=0, height=0)

#funcionalidades = Functions() #objeto de la clase Functions

#funcionalidades.imprimirSemestre(ventana,"Primer semestre")
def imprimirSemestre(ventana,semestre:str): #la varia semestre es la que me dice en qué semetsre se oprimió.

         # ABRIR TXT DE MATERIAS, ESTE ES EL TXT DE LA INFO DE CADA MATERIA EN CADA SEM 
        txtM = []
        with open("archivos_txt/txtSemestre.txt") as fname:
            for lineas in fname:
                txtM.append(lineas.split(","))
        i = 0
        sw = 1
        sem = []#lista de listas, cada index es una materia con todas sus caracteristicas
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
"""
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
      
     #para imprimir los labes de rating, actividades, etc

imprimirSemestre(ventana,"Primer semestre")

ventana.mainloop()
##SEM ES UNA LISTA DE LISTAS