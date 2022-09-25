import tkinter as tk
from tkinter import ttk
from tkinter import Canvas

from matplotlib.figure import Figure
from scipy.stats import skew
from statistics import mode
from scipy.stats import kurtosis
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
NavigationToolbar2Tk)
import metodosAlgoritmos as ma




master=tk.Tk()
master.geometry("1380x980")




vectorResultadosNumeros=[]


fig = Figure(figsize=(5, 5),
                 dpi=100)
canvas = FigureCanvasTkAgg(fig,
                               master=master)

variable_a=tk.IntVar()
label_k=tk.Label(master,text="Ingresa un valor de K")
texto_k=tk.Entry(master,textvariable =variable_a)

variable_g=tk.IntVar()
label_g=tk.Label(master,text="Ingrese un valor de G")
texto_g=tk.Entry(master,textvariable =variable_g)

variable_x0=tk.IntVar()
label_x0=tk.Label(master,text="ingrese una semilla")
texto_x0=tk.Entry(master,textvariable =variable_x0)


variable_a=tk.IntVar()
label_a=tk.Label(master,text="Ingrese un valor de A")
texto_a=tk.Entry(master,textvariable =variable_a)

variable_b=tk.IntVar()
label_b=tk.Label(master,text="Ingrese una valor de B")
texto_b=tk.Entry(master,textvariable =variable_b)

variable_c=tk.IntVar()
label_c=tk.Label(master,text="Ingrese una valor de C")
texto_c=tk.Entry(master,textvariable =variable_c)


def generarSecuencia():
    if varStringGenerador.get() == "Visual Base":
        res =ma.VisualBase(texto_x0.get())
        vectorResultadosNumeros.append(res)
        print(vectorResultadosNumeros)

    elif varStringGenerador.get() == "Congruencial Multiplicativo":
        res = ma.ConguencialMultplicativo(texto_g.get(),texto_k.get(),texto_x0.get())
        vectorResultadosNumeros.append(res)
        print(vectorResultadosNumeros)
    elif varStringGenerador.get() == "Congruencial Cuadratico":
        res = ma.CongruencialCuadratico(texto_g.get(),texto_a.get(),texto_b.get(),texto_c.get(),texto_x0.get())
        vectorResultadosNumeros.append(res)
        print(vectorResultadosNumeros)
botonGenerar=tk.Button(master,text="Generar secuencia",command=generarSecuencia)




def algoritmoSeleccionado(event):

    global label_k
    global texto_k

    global label_g
    global texto_g


    global label_x0
    global texto_x0

    global label_c
    global texto_c

    global label_b
    global texto_b

    global label_a
    global texto_a

    global botonGenerar

    if varStringGenerador.get()=="Visual Base":
        label_x0.place(x=0,y=90)
        texto_x0.place(x=0,y=110)
        botonGenerar.place(x=0,y=130)
        print(texto_x0.get())
    elif varStringGenerador.get()=="Congruencial Multiplicativo":
        label_g.place(x=0,y=90)
        texto_g.place(x=0,y=110)
        label_k.place(x=0,y=130)
        texto_k.place(x=0,y=150)
        label_x0.place(x=0,y=170)
        texto_x0.place(x=0,y=190)
        botonGenerar.place(x=0,y=210)

        print()
    elif varStringGenerador.get()=="Congruencial Cuadratico":
        label_g.place(x=0, y=90)
        texto_g.place(x=0, y=110)
        label_a.place(x=0,y=130)
        texto_a.place(x=0,y=150)
        label_b.place(x=0,y=170)
        texto_b.place(x=0,y=190)
        label_c.place(x=0,y=210)
        texto_c.place(x=0,y=230)
        label_x0.place(x=0, y=250)
        texto_x0.place(x=0, y=270)
        botonGenerar.place(x=0, y=290)

        print()
















LabelGrafica=tk.Label(master,text="Eliga como generar su secuencia pseudoAleatoria")

varStringGenerador=tk.StringVar()

listboxAl=ttk.Combobox(master,
                     textvariable=varStringGenerador,
                     height=6)
listboxAl["values"]=["Visual Base","Congruencial Multiplicativo","Congruencial Cuadratico"]
listboxAl["state"]="readonly"

LabelGrafica.place(x=0,y=50)
listboxAl.place(x=0,y=70)
listboxAl.config(width = 30)


listboxAl.bind("<<ComboboxSelected>>",algoritmoSeleccionado)

tk.mainloop()