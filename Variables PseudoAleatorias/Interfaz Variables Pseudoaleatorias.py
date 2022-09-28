import statistics
import tkinter as tk
from tkinter import ttk
from tkinter import Canvas
import tkinter.messagebox


from matplotlib.figure import Figure
from scipy import stats

from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
NavigationToolbar2Tk)
import metodosAlgoritmos as ma
import metodosVariables as mv
from scipy.stats import chi2
from scipy.stats import lognorm




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
    elif varStringGenerador.get()=="Fortran":
        res = ma.Fortran(texto_x0.get())
        vectorResultadosNumeros.append(res)
        print(vectorResultadosNumeros)


botonGenerar=tk.Button(master,text="Generar secuencia",command=generarSecuencia)




def algoritmoSeleccionado(event):

    global label_k
    global texto_k
    label_k.place_forget()
    texto_k.place_forget()

    global label_g
    global texto_g
    label_g.place_forget()
    texto_g.place_forget()

    global label_x0
    global texto_x0
    label_x0.place_forget()
    texto_x0.place_forget()

    global label_c
    global texto_c
    label_c.place_forget()
    texto_c.place_forget()

    global label_b
    global texto_b
    label_b.place_forget()
    texto_b.place_forget()

    global label_a
    global texto_a
    label_a.place_forget()
    texto_a.place_forget()

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
    elif varStringGenerador.get()=="Fortran":
        label_x0.place(x=0, y=90)
        texto_x0.place(x=0, y=110)
        botonGenerar.place(x=0, y=130)
        print(texto_x0.get())




variable_Me=tk.DoubleVar()
label_Me=tk.Label(master,text="Ingresa un valor de media")
texto_Me=tk.Entry(master,textvariable =variable_Me)

variable_Va=tk.DoubleVar()
label_Va=tk.Label(master,text="Ingrese un valor de media")
texto_Va=tk.Entry(master,textvariable=variable_Va)


variable_Ta=tk.DoubleVar()
label_Ta=tk.Label(master,text="Ingrese un valor de media")
texto_Ta=tk.Entry(master,textvariable=variable_Ta)


variable_Ca=tk.IntVar()
label_Ca=tk.Label(master,text="Ingrese la cantidad de variables que quiere")
texto_Ca=tk.Entry(master,textvariable=variable_Ca)


def generarVariable():
    fig.clear()
    if varStringVariable.get() == "Box Muller":
        if (len(vectorResultadosNumeros)>=2):

            resul=mv.boxMuller(vectorResultadosNumeros,variable_Me.get(),variable_Va.get(),variable_Ca.get())
            plot = fig.add_subplot(111)
            #plot.plot(resul,norm.pdf(resul, norm.pdf(resul,statistics.mean(resul),statistics.stdev(resul))))
            plot.hist(resul,80)
            #plot.plot(resul)
            #FPD_normal=stats.norm(10,2).pdf(resul)
            #plot.plot(resul,FPD_normal)
            canvas.draw()

            print(resul)
            canvas.get_tk_widget().place(x=600)
        else:
            tkinter.messagebox.showinfo("NO se puede realizar la accion","Se necesita minimo 2 secuencias apra generar una vairables")
    elif varStringVariable.get() == "Logaritmica Normal":

        if(len(mv.listaXI)>=1):
            resul=mv.logaritmica(variable_Ca.get())
            plot=fig.add_subplot(111)

            #sigma = 0.6  # parametro
            #lognormal = stats.lognorm(sigma)
            #x=np.linspace(lognormal.ppf(min(resul)),lognormal.ppf(max(resul)),100)
            #fp=lognormal.pdf(resul)
            ##sigma = 1  # parametro
            ##lognormal = stats.lognorm(sigma)
            #x = np.linspace(lognormal.ppf(0.01),lognormal.ppf(0.99), 100)
            ##fp = lognormal.pdf(resul)
            ##plot.plot(resul,fp)
            plot.hist(resul,80)
            canvas.draw()
            print()
            canvas.get_tk_widget().place(x=600)
        else:
            tkinter.messagebox.showinfo("No se puede realizar la accion","Se necesita minimo que genera una vez unas variables de distribucion normal para hacer el proceso")
    elif varStringVariable.get()=="Chi cuadrado normal":
        if len(mv.listaXI)>=3:

            resul = mv.chi2(variable_Ca.get())
            print(resul)
            plot = fig.add_subplot(111)
            plot.hist(resul)
            canvas.draw()
            canvas.get_tk_widget().place(x=600)
        else:
            tkinter.messagebox.showinfo("No se puede realizar la accion","Se necesita minimo que genere 3 secuencias de variables de distribucion normal para hacer este proceso")
    elif varStringVariable.get()=="T":
        if(len(mv.listaXI)>=1 and len(mv.listaCHI2)>1):
            resul=mv.t(variable_Ca.get())
            print(resul)
            plot = fig.add_subplot(111)
            plot.hist(resul)
            canvas.draw()
            canvas.get_tk_widget().place(x=600)
        else:
            tkinter.messagebox.showinfo("No se puede realizar la accion",
                                    "Se necesita minimo que genera una vez unas variables de distribucion normal para hacer el proceso\n tambien que tenga un conjunto mayor a 1 de variables de chi2")


    elif varStringVariable.get() == "F":
        if len(mv.listaCHI2)>=2:
            resul=mv.f(variable_Ca.get())
            print(resul)
            plot = fig.add_subplot(111)
            plot.hist(resul)
            canvas.draw()
            canvas.get_tk_widget().place(x=600)
        else:
            tkinter.messagebox.showinfo("No se puede realizar la accion",
                                    "Se necesita minimo que genera 2 veces unas variables de distribucion chi2 para hacer el proceso")

    elif varStringVariable.get() == "Exponencial":

        if variable_Ta.get()!=0 and len(mv.listaXI)>=1:
            resul=mv.exponencual(variable_Ca.get(),variable_Ta.get())
            print(resul)
            plot = fig.add_subplot(111)
            plot.hist(resul)
            canvas.draw()
            canvas.get_tk_widget().place(x=600)
        else:
            tkinter.messagebox.showinfo("No se puede realizar la accion",
                                    "Se necesita minimo que genera una vez unas variables de distribucion normal para hacer el proceso")


    print()

botonVariable=tk.Button(master,text="Generar secuencia",command=generarVariable)

def borrarSecuencia():
    global  vectorResultadosNumeros
    vectorResultadosNumeros.clear()
    print(vectorResultadosNumeros)

    tk.messagebox.showinfo("Secuenvia Elminada",
                                "La secuencia se elimino con exito")

botonBorrarSecuencia=tk.Button(master,text="Borrar secuencias existentes",command=borrarSecuencia)
botonBorrarSecuencia.place(y=500)

def borrarVariables():
    mv.limpiarXI()
    print(mv.listaCHI2,mv.listaXI)
    tk.messagebox.showinfo("Variables Elminadas",
                           "Las variables se elimino con exito")

botonBorrarSecuencia=tk.Button(master,text="Borrar variables",command=borrarVariables)
botonBorrarSecuencia.place(y=540)
def VariableSeleccionada(event):

    global label_Me
    global texto_Me
    label_Me.place_forget()
    texto_Me.place_forget()

    global label_Va
    global texto_Va
    label_Va.place_forget()
    texto_Va.place_forget()

    global label_Ta
    global texto_Ta
    label_Ta.place_forget()
    texto_Ta.place_forget()

    global label_Ca
    global texto_Ca
    label_Ca.place_forget()
    texto_Ca.place_forget()


    if varStringVariable.get()=="Box Muller":
        #label_Me.place(x=300,y=90)
        #texto_Me.place(x=300,y=110)
        #label_Va.place(x=300,y=130)
        #texto_Va.place(x=300,y=150)
        label_Ca.place(x=300,y=90)
        texto_Ca.place(x=300,y=110)
        botonVariable.place(x=300,y=130)

        print()
    elif varStringVariable.get()=="Logaritmica Normal":
        label_Ca.place(x=300, y=90)
        texto_Ca.place(x=300, y=110)
        botonVariable.place(x=300, y=130)
        botonVariable.place(x=300, y=210)

        print()
    elif varStringVariable.get()=="Chi cuadrado normal":
        label_Ca.place(x=300, y=90)
        texto_Ca.place(x=300, y=110)
        botonVariable.place(x=300, y=130)
        print()
    elif varStringVariable.get()=="T":
        label_Ca.place(x=300, y=90)
        texto_Ca.place(x=300, y=110)
        botonVariable.place(x=300, y=130)
        print()
    elif varStringVariable.get() == "F":
        label_Ca.place(x=300, y=90)
        texto_Ca.place(x=300, y=110)
        botonVariable.place(x=300, y=130)
        print()
    elif varStringVariable.get() == "Exponencial":
        label_Ta.place(x=300,y=90)
        texto_Ta.place(x=300,y=110)
        label_Ca.place(x=300, y=130)
        texto_Ca.place(x=300, y=150)
        botonVariable.place(x=300, y=170)
        print()
    print()













LabelGrafica=tk.Label(master,text="Eliga como generar su secuencia pseudoAleatoria")

varStringGenerador=tk.StringVar()

listboxAl=ttk.Combobox(master,
                     textvariable=varStringGenerador,
                     height=6)
listboxAl["values"]=["Visual Base","Fortran","Congruencial Multiplicativo","Congruencial Cuadratico"]
listboxAl["state"]="readonly"

LabelGrafica.place(x=0,y=50)
listboxAl.place(x=0,y=70)
listboxAl.config(width = 30)




LabelMetodo=tk.Label(master,text="Eliga la distribucion de variable alaeatoria que desea")

varStringVariable=tk.StringVar()

listboxVa=ttk.Combobox(master,
                     textvariable=varStringVariable,
                     height=6)
listboxVa["values"]=["Box Muller","Logaritmica Normal","Chi cuadrado normal","T","F","Exponencial"]
listboxVa["state"]="readonly"

LabelMetodo.place(x=300,y=50)
listboxVa.place(x=300,y=70)
listboxVa.config(width = 30)





listboxAl.bind("<<ComboboxSelected>>",algoritmoSeleccionado)

listboxVa.bind("<<ComboboxSelected>>",VariableSeleccionada)

tk.mainloop()