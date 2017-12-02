from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog

def operacion():
    puntaje = 0
    numero1 = num1.get()
    numero2 = num2.get()
    numero3 = num3.get()
    numero4 = num4.get()
    numero5 = num5.get()
    numero6 = num6.get()
    numero7 = num7.get()
    numero8 = num8.get()
    numero9 = num9.get()
    nombre = nombreJugador.get()
    if numero1==1:
        puntaje = puntaje + 1
    if numero2==1:
        puntaje = puntaje + 1
    if numero3==3:
        puntaje = puntaje + 1
    if numero4==2:
        puntaje = puntaje + 1
    if numero5==1:
        puntaje = puntaje + 1
    if numero6==3:
        puntaje = puntaje + 1
    if numero7==1:
        puntaje = puntaje + 1
    if numero8==2:
        puntaje = puntaje + 1
    if numero9==3:
        puntaje = puntaje + 1

    if puntaje == 0:
        comentario = "Gracias por contestar la encuesta"
    if puntaje<=3 and puntaje>0:
        comentario = "Gracias por contestar la encuesta"
    if puntaje<=6 and puntaje>3:
        comentario = "Gracias por contestar la encuesta"
    if puntaje<9 and puntaje>6:
        comentaio = "Gracias por contestar la encuesta"
    if puntaje == 9:
        comentario = "Gracias por contestar la encuesta"
    messagebox.showinfo("resultado",comentario)
    guardar = open("respuestas.txt","a")
    guardar.write(nombre + " obtuvo " + str(puntaje) + " puntos" + "\n")


def cerrar():
    ventana.destroy()

ventana = Tk()
ventana.title("Test")
ventana.geometry("1000x600+200+0")
ventana.configure(background="black")
num1=IntVar()
num2=IntVar()
num3=IntVar()
num4=IntVar()
num5=IntVar()
num6=IntVar()
num7=IntVar()
num8=IntVar()
num9=IntVar()
bienvenida = Label(ventana,text="Cuanto sabes? (encuesta)",fg="red",bg="black",font=("helvetica",20)).place(x=300,y=10)
preg1 = Label(ventana,text="1 :¿Cual de estas razas es más inteligente?",bg="black",fg="red").place(x=0,y=60)
preg2 = Label(ventana,text="2 :¿En que año empezó a gobernar Manuel Odría?",bg="black",fg="red").place(x=350,y=60)
preg3 = Label(ventana,text="3 :¿Cantante de rock peruano?",bg="black",fg="red").place(x=700,y=60)
preg4 = Label(ventana,text="4 :¿Nobel de literatura?",bg="black",fg="red").place(x=0,y=200)
preg5 = Label(ventana,text="5 :¿crees que Paolo Guerrero ira al mundial?",bg="black",fg="red").place(x=350,y=200)
preg6 = Label(ventana,text="6 :Favorito en este mundial Rusia 2018",bg="black",fg="red").place(x=700,y=200)
preg7 = Label(ventana,text="7 :¿Ministro de economía?",bg="black",fg="red").place(x=0,y=340)
preg8 = Label(ventana,text="8 :¿En que año se independizo el Perú?",bg="black",fg="red").place(x=350,y=340)
preg9 = Label(ventana,text="9 :¿Quien fue el último inca?",bg="black",fg="red").place(x=700,y=340)
alt11 = Radiobutton(ventana,text="Rot Wailer",value=1,variable=num1,fg="red",bg="black").place(x=10,y=90)
alt12 = Radiobutton(ventana,text="Pastor alemon",value=2,variable=num1,fg="red",bg="black").place(x=10,y=120)
alt13 = Radiobutton(ventana,text="perro peruano",value=3,variable=num1,fg="red",bg="black").place(x=10,y=150)
alt21 = Radiobutton(ventana,text="1948",value=1,variable=num2,fg="red",bg="black").place(x=350,y=90)
alt22 = Radiobutton(ventana,text="1950",value=2,variable=num2,fg="red",bg="black").place(x=350,y=120)
alt23 = Radiobutton(ventana,text="1960",value=3,variable=num2,fg="red",bg="black").place(x=350,y=150)
alt31 = Radiobutton(ventana,text="Isman",value=1,variable=num3,fg="red",bg="black").place(x=700,y=90)
alt32 = Radiobutton(ventana,text="Talia",value=2,variable=num3,fg="red",bg="black").place(x=700,y=120)
alt33 = Radiobutton(ventana,text="Wicho",value=3,variable=num3,fg="red",bg="black").place(x=700,y=150)
alt41 = Radiobutton(ventana,text="Joaquin Cortazar",value=1,variable=num4,fg="red",bg="black").place(x=10,y=230)
alt42 = Radiobutton(ventana,text="Vargas Llosa",value=2,variable=num4,fg="red",bg="black").place(x=10,y=260)
alt43 = Radiobutton(ventana,text="Fujimori",value=3,variable=num4,fg="red",bg="black").place(x=10,y=290)
alt51 = Radiobutton(ventana,text="Claro",value=1,variable=num5,fg="red",bg="black").place(x=350,y=230)
alt52 = Radiobutton(ventana,text="Eso espero",value=2,variable=num5,fg="red",bg="black").place(x=350,y=260)
alt53 = Radiobutton(ventana,text="no irá",value=3,variable=num5,fg="red",bg="black").place(x=350,y=290)
alt61 = Radiobutton(ventana,text="Brazil",value=1,variable=num6,fg="red",bg="black").place(x=700,y=230)
alt62 = Radiobutton(ventana,text="Alemania",value=2,variable=num6,fg="red",bg="black").place(x=700,y=260)
alt63 = Radiobutton(ventana,text="Perú",value=3,variable=num6,fg="red",bg="black").place(x=700,y=290)
alt71 = Radiobutton(ventana,text="Fernando Zavala",value=1,variable=num7,fg="red",bg="black").place(x=10,y=370)
alt72 = Radiobutton(ventana,text="Alfredo Thorne",value=2,variable=num7,fg="red",bg="black").place(x=10,y=400)
alt73 = Radiobutton(ventana,text="Victor Velaun",value=3,variable=num7,fg="red",bg="black").place(x=10,y=430)
alt81 = Radiobutton(ventana,text="1824",value=1,variable=num8,fg="red",bg="black").place(x=350,y=370)
alt82 = Radiobutton(ventana,text="1821",value=2,variable=num8,fg="red",bg="black").place(x=350,y=400)
alt83 = Radiobutton(ventana,text="1819",value=3,variable=num8,fg="red",bg="black").place(x=350,y=430)
alt91 = Radiobutton(ventana,text="Pizarro",value=1,variable=num9,fg="red",bg="black").place(x=700,y=370)
alt92 = Radiobutton(ventana,text="Yupanqui",value=2,variable=num9,fg="red",bg="black").place(x=700,y=400)
alt93 = Radiobutton(ventana,text="Atahualpa",value=3,variable=num9,fg="red",bg="black").place(x=700,y=430)
boton = Button(ventana,bg="green",width = 17, height = 2,text="resultado",command=operacion).place(x=350,y = 500)
boton2 = Button(ventana,bg="green",width = 17, height = 2,text="cerrar",command=cerrar).place(x=850,y = 500)
nombres = simpledialog.askstring("participante","nombre del participante: ")
nombreJugador = StringVar()
nombreJugador.set(nombres)
ventana.mainloop()
