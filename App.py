from email.mime import image
import tkinter as tk

ventana = tk.Tk()
ventana.geometry ("870x500")
ventana.title("iPensum")


main = tk.PhotoImage (file = "main.png") # se carga la imagen 
busqG = tk.PhotoImage (file = "busqG.png") #se carga la imagen 
busqE = tk.PhotoImage (file = "busqE.png")
fondo = tk.Label (ventana, image = main).place (x=0,y=0) #propiedades del frame 

#prueba = tk.PhotoImage(file="Trans.png") 
#fondo = tk.Label (ventana, image = prueba).place(x=260,y=240)

def MainMenu ():
    label_ = tk.Label(ventana,image=main)
    label_.pack()
    boton=tk.Button(ventana,text="GUEST", width= 10, command= Menu2,font=60, bg= "gray") #propiedades del boton, command = Menu2 es lo q se debe ejecutar
    boton.place(x = 240,y=420)
    
    boton2 = tk.Button(ventana,text= "STUDENT", width=13, command = Menu3, font = 60, bg = "gray")
    boton2.place(x = 490,y=420)
    
def Menu2 (): # Boton que me lleva al inicio de sesión como invitado, al hundir invitado puede inciar su busqueda de forma normal
    for ele in ventana.winfo_children():
        ele.destroy()
    interfaz = tk.Canvas(ventana)
    interfaz.pack()
    label1 = tk.Label(interfaz,image=busqG)
    label1.pack()


def Menu3 (): #Boton que me lleva al inicio de sesión como estudiante (cuando hunda estudiante, debe loguearse copiando el codigo y su usuario (no se ha hecho) para que pueda iniciar su busqueda)
    for ele in ventana.winfo_children():
        ele.destroy()
    interfaz = tk.Canvas(ventana)
    interfaz.pack()
    label2 = tk.Label(interfaz,image=busqE)
    label2.pack()


MainMenu()
ventana.mainloop()


