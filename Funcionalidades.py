#funcionalidades del programa 
import tkinter as tk

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
        
    def login(self,entradaUser,entradaCode,ventana,errorC, txtL,MenuBusqueda, InvalidCode):
        self.user = self.entradaUser.get()
        self.code = self.entradaCode.get()
        if(self.user == "" or self.code == ""):  # Campos vacios
            self.Error = tk.Label(ventana, image=errorC, borderwidth=0, width=190)
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
    #menu logeo
    def validate_code(self, text: str):
        return self.text.isdecimal()#verdadero si es numero  
    

    # para abrir el archivo y que imprima dependiendo al semestre selecionado
    def imprimirSemestre(self, ventana,semestre:str): #la varia semestre es la que me dice en qué semetsre se oprimió.

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
        print (sem)
        print("VAMOS A IMPRIMIR EL SEMESTRE")
        string=""
        print (*sem)
        for nav in sem:
            string += nav + "\n"
        #string = " ".join([str(item) for item in sem])
        print ("")
        print ("")
        print (string)
        tk.Label(ventana, bg = "white", text=string,width = 90, height=5, font=("Calibri",14,"italic")).place(x=30,y=30)
        ##############################################
     
     #para imprimir los labes de rating, actividades, etc
    def imprimirLabel(self):
         pass

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