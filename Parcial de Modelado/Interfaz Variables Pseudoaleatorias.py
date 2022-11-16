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



listaTraingulo=[]
master=tk.Tk()
master.geometry("1380x980")




vectorResultadosNumeros=[]


fig = Figure(figsize=(5, 5),
                 dpi=100)
canvas = FigureCanvasTkAgg(fig,
                               master=master)


cantidadTriangulos=0

variable_a=tk.IntVar()
label_k=tk.Label(master,text="Ingresa un valor de K")
texto_k=tk.Entry(master,textvariable =variable_a)

variable_g=tk.IntVar()
label_g=tk.Label(master,text="Ingrese un valor de G")
texto_g=tk.Entry(master,textvariable =variable_g)

variable_x0=tk.IntVar()
label_x0=tk.Label(master,text="ingrese una semilla")
texto_x0=tk.Entry(master,textvariable =variable_x0)

variable_x1=tk.IntVar()
label_x1=tk.Label(master,text="ingrese una 2 semilla")
texto_x1=tk.Entry(master,textvariable =variable_x1)


variable_a=tk.IntVar()
label_a=tk.Label(master,text="Ingrese un valor de A")
texto_a=tk.Entry(master,textvariable =variable_a)

variable_b=tk.IntVar()
label_b=tk.Label(master,text="Ingrese una valor de B")
texto_b=tk.Entry(master,textvariable =variable_b)

variable_c=tk.IntVar()
label_c=tk.Label(master,text="Ingrese una valor de C")
texto_c=tk.Entry(master,textvariable =variable_c)

Variable_A=tk.DoubleVar()
label_A=tk.Label(master,text="Ingrese el punto A del triangulo")
entrada_A=tk.Entry(master,textvariable =Variable_A)

Variable_B=tk.DoubleVar()
label_B=tk.Label(master,text="Ingrese el punto B del triangulo")
entrada_B=tk.Entry(master,textvariable =Variable_B)

Variable_C=tk.DoubleVar()
label_C=tk.Label(master,text="Ingrese el punto C del triangulo")
entrada_C=tk.Entry(master,textvariable =Variable_C)


label_Tamaño_datos=tk.Label(master,text="")
def ListadoVariables():
    tamaño=""
    cont=0
    global label_Tamaño_datos
    for i in vectorResultadosNumeros:
        cont+=1
        tamaño+= "La secuencia: "+str(cont)+ "es de tamaño:  "+str(len(i))+"\n"
        print(i)
    label_Tamaño_datos.config(text=tamaño)




def generarSecuencia():
    global label_Tamaño_datos
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
    elif varStringGenerador.get() == "Algoritmo Lineal":
        res = ma.ResolverLieal(float(texto_k.get()), float(texto_c.get()), float(texto_g.get()), float(texto_x0.get()))
        vectorResultadosNumeros.append(res)
        print(res)
    elif varStringGenerador.get()=="Cuadrados medios":

        if len(texto_x0.get())!=4:
            tkinter.messagebox.showinfo("NO se puede realizar la accion",
                                        "Se necesita que la semilla tenga un tamaño fijado de 4 unidades")
        else:

            res = ma.AlgortimoCuadrados(float(texto_x0.get()))
            vectorResultadosNumeros.append(res)
            print(res)
    elif varStringGenerador.get() == "Productos medios":

        if len(texto_x0.get() ) != 4 or len(texto_x1.get())!=4 :
            tkinter.messagebox.showinfo("NO se puede realizar la accion",
                                        "Se necesita que la semilla tenga un tamaño fijado de 4 unidades")
        else:

            res = ma.AlgortimosProductos(float(texto_x0.get()),float(texto_x1.get()))
            vectorResultadosNumeros.append(res)
            print(res)

    elif varStringGenerador.get() == "Mutiplicador constante":

        if len(texto_x0.get()) != 4 or len(texto_x1.get())!=4 :
            tkinter.messagebox.showinfo("NO se puede realizar la accion",
                                        "Se necesita que la semilla tenga un tamaño fijado de 4 unidades")
        else:

            res = ma.AlgortimosConstante(float(texto_x0.get()),float(texto_x1.get()))
            vectorResultadosNumeros.append(res)
            print(res)

    ListadoVariables()
    label_Tamaño_datos.place(x=0, y=310)




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

    global label_x1
    global texto_x1
    label_x1.place_forget()
    texto_x1.place_forget()

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
    elif varStringGenerador.get() == "Algoritmo Lineal":
        label_g.place(x=0, y=90)
        texto_g.place(x=0, y=110)
        label_k.place(x=0, y=130)
        texto_k.place(x=0, y=150)
        label_c.place(x=0, y=170)
        texto_c.place(x=0, y=190)
        label_x0.place(x=0, y=210)
        texto_x0.place(x=0, y=230)
        botonGenerar.place(x=0, y=250)
    elif varStringGenerador.get()=="Cuadrados medios":
        label_x0.place(x=0, y=90)
        texto_x0.place(x=0, y=110)
        botonGenerar.place(x=0, y=130)
    elif varStringGenerador.get()=="Productos medios":
        label_x0.place(x=0, y=90)
        texto_x0.place(x=0, y=110)
        label_x1.place(x=0,y=130)
        texto_x1.place(x=0,y=150)
        botonGenerar.place(x=0, y=170)
    elif varStringGenerador.get()=="Mutiplicador constante":
        label_x0.place(x=0, y=90)
        texto_x0.place(x=0, y=110)
        label_x1.place(x=0, y=130)
        texto_x1.place(x=0, y=150)
        botonGenerar.place(x=0, y=170)




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

variable_alpha=tk.DoubleVar()
label_alpha=tk.Label(master,text="Ingrese un valor de alpha")
texto_alpha=tk.Entry(master,textvariable=variable_alpha)

variable_Beta=tk.DoubleVar()
label_Beta=tk.Label(master,text="Ingrese un valor de beta que quiere")
texto_Beta=tk.Entry(master,textvariable=variable_Beta)

variable_U=tk.DoubleVar()
label_U=tk.Label(master,text="Ingrese un valor de u que quiere")
texto_U=tk.Entry(master,textvariable=variable_U)

Variable_Desviacion=tk.DoubleVar()
label_Desviacion=tk.Label(master,text="Ingrese un valor de u que quiere")
texto_Desviacion=tk.Entry(master,textvariable=Variable_Desviacion)

Variable_Delta=tk.DoubleVar()
label_Delta=tk.Label(master,text="Ingrese un valor de u que quiere")
texto_Delta=tk.Entry(master,textvariable=Variable_Delta)


labelTriangulos=tk.Label(master,text="La cantidad actual de triangulos es: "+str(cantidadTriangulos))

def generarVariable():
    global listaTraingulo
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
            plot.hist(resul)
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
            plot.hist(resul,80)
            canvas.draw()
            canvas.get_tk_widget().place(x=600)
        else:
            tkinter.messagebox.showinfo("No se puede realizar la accion","Se necesita minimo que genere 3 secuencias de variables de distribucion normal para hacer este proceso")
    elif varStringVariable.get()=="T":
        if(len(mv.listaXI)>=1 and len(mv.listaCHI2)>1):
            resul=mv.t(variable_Ca.get())
            print(resul)
            plot = fig.add_subplot(111)
            plot.hist(resul,80)
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
            plot.hist(resul,80)
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
            plot.hist(resul,80)
            canvas.draw()
            canvas.get_tk_widget().place(x=600)
        else:
            tkinter.messagebox.showinfo("No se puede realizar la accion",
                                    "Se necesita minimo que genera una vez unas variables de distribucion normal para hacer el proceso")

    elif varStringVariable.get()=="Gamma":
        if (len(vectorResultadosNumeros) >= 2):
            resul=mv.gamma(vectorResultadosNumeros,variable_Ca.get(),variable_alpha.get(),variable_Beta.get())
            print(resul)
            plot = fig.add_subplot(111)
            plot.hist(resul,100)
            canvas.draw()
            canvas.get_tk_widget().place(x=600)
        print(variable_Beta.get())
        print(variable_alpha.get())
    elif varStringVariable.get() == "Composicion":

            resul = mv.composicion(listaTraingulo ,vectorResultadosNumeros[0],vectorResultadosNumeros[1],variable_Ca.get())
            print(resul)
            plot = fig.add_subplot(111)
            plot.hist(resul, 100)
            canvas.draw()
            canvas.get_tk_widget().place(x=600)
    elif varStringVariable.get() == "Transformada Directa":

        resul = mv.metodoDirecto(vectorResultadosNumeros[0],vectorResultadosNumeros[1],variable_Ca.get(),variable_U.get(),Variable_Desviacion.get())
        print(resul)
        plot = fig.add_subplot(111)
        plot.hist(resul, 100)
        canvas.draw()
        canvas.get_tk_widget().place(x=600)
        canvas.get_tk_widget().place(x=600)
    elif varStringVariable.get() == "Transformada Inversa":

        resul = mv.metodoTransformadaInversa(vectorResultadosNumeros[0],variable_Ca.get(),Variable_Delta.get())
        print(resul)
        plot = fig.add_subplot(111)
        plot.hist(resul, 100)
        canvas.draw()
        canvas.get_tk_widget().place(x=600)
    elif varStringVariable.get()=="Aceptacion y rechazo":
        resul = mv.metodoAceptacionYrechazo(vectorResultadosNumeros[0],vectorResultadosNumeros[1], variable_Ca.get())
        print(resul)
        plot = fig.add_subplot(111)
        plot.scatter(resul[0], resul[1])
        canvas.draw()
        canvas.get_tk_widget().place(x=600)
    print()

botonVariable=tk.Button(master,text="Generar secuencia",command=generarVariable)

def AgregarTriangulo():
    global listaTraingulo
    global Variable_A
    global Variable_B
    global Variable_C
    global labelTriangulos
    global cantidadTriangulos
    if len(listaTraingulo)==5:
        print("No se puede mi loco")
        tkinter.messagebox.showinfo("NO se puede realizar la accion",
                                    "El limite de triangulos es de 5, por lo cual no se le permitira ingresar mas triangulos")
    else:
        listaTraingulo.append([Variable_A.get(),Variable_B.get(),Variable_C.get()])
        print(listaTraingulo)
        cantidadTriangulos+=1
        labelTriangulos.config(text="La cantidad actual de triangulos es: "+str(cantidadTriangulos))
        labelTriangulos.place(x=300,y=230)
    Variable_A.set(0)
    Variable_B.set(0)
    Variable_C.set(0)




botonAgregarTriangulo=tk.Button(master,text="Añadir Triangulo",command=AgregarTriangulo)



def borrarSecuencia():
    ListadoVariables()
    global  vectorResultadosNumeros

    vectorResultadosNumeros.clear()
    print(vectorResultadosNumeros)

    tk.messagebox.showinfo("Secuenvia Elminada",
                                "La secuencia se elimino con exito")

botonBorrarSecuencia=tk.Button(master,text="Borrar secuencias existentes",command=borrarSecuencia)
botonBorrarSecuencia.place(y=900)

def borrarVariables():
    mv.limpiarXI()
    print(mv.listaCHI2,mv.listaXI)
    tk.messagebox.showinfo("Variables Elminadas",
                           "Las variables se elimino con exito")

botonBorrarSecuencia=tk.Button(master,text="Borrar variables",command=borrarVariables)
botonBorrarSecuencia.place(y=920)
def VariableSeleccionada(event):
    global labelTriangulos
    global listaTraingulo

    global cantidadTriangulos

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

    global label_alpha
    global texto_alpha

    label_alpha.place_forget()
    texto_alpha.place_forget()

    global label_Beta
    global texto_Beta

    label_Beta.place_forget()
    texto_Beta.place_forget()


    global label_A
    global entrada_A

    label_A.place_forget()
    entrada_A.place_forget()

    global label_B
    global entrada_B

    label_B.place_forget()
    entrada_B.place_forget()

    global label_C
    global entrada_C

    global label_U
    global texto_U


    global label_Desviacion
    global texto_Desviacion
    global botonAgregarTriangulo
    botonAgregarTriangulo.place_forget()

    label_C.place_forget()
    entrada_C.place_forget()
    global label_Delta
    global texto_Delta

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
    elif varStringVariable.get()=="Gamma":
        label_alpha.place(x=300,y=90)
        texto_alpha.place(x=300,y=110)
        label_Beta.place(x=300,y=130)
        texto_Beta.place(x=300,y=150)
        label_Ca.place(x=300,y=170)
        texto_Ca.place(x=300,y=190)
        botonVariable.place(x=300,y=210)
    elif varStringVariable.get()=="Composicion":
        label_A.place(x=300,y=90)
        entrada_A.place(x=300,y=110)
        label_B.place(x=300, y=130)
        entrada_B.place(x=300, y=150)
        label_C.place(x=300, y=170)
        entrada_C.place(x=300, y=190)
        botonAgregarTriangulo.place(x=300,y=210)
        labelTriangulos.place(x=300,y=230)
        label_Ca.place(x=300, y=250)
        texto_Ca.place(x=300, y=270)
        botonVariable.place(x=300,y=290)
    elif varStringVariable.get()=="Transformada Directa":
        label_U.place(x=300,y=90)
        texto_U.place(x=300,y=110)
        label_Desviacion.place(x=300,y=130)
        texto_Desviacion.place(x=300,y=150)
        label_Ca.place(x=300, y=170)
        texto_Ca.place(x=300, y=190)
        botonVariable.place(x=300,y=210)
    elif varStringVariable.get()=="Transformada Inversa":
        label_Delta.place(x=300,y=90)
        texto_Delta.place(x=300,y=110)
        label_Ca.place(x=300, y=130)
        texto_Ca.place(x=300, y=150)
        botonVariable.place(x=300,y=170)
    elif varStringVariable.get()=="Aceptacion y rechazo":
        label_Ca.place(x=300, y=90)
        texto_Ca.place(x=300, y=110)
        botonVariable.place(x=300, y=130)

    print()













LabelGrafica=tk.Label(master,text="Eliga como generar su secuencia pseudoAleatoria")

varStringGenerador=tk.StringVar()

listboxAl=ttk.Combobox(master,
                     textvariable=varStringGenerador,
                     height=6)
listboxAl["values"]=["Visual Base","Fortran","Congruencial Multiplicativo","Congruencial Cuadratico","Algoritmo Lineal","Cuadrados medios","Productos medios","Mutiplicador constante"]
listboxAl["state"]="readonly"

LabelGrafica.place(x=0,y=50)
listboxAl.place(x=0,y=70)
listboxAl.config(width = 30)




LabelMetodo=tk.Label(master,text="Eliga la distribucion de variable alaeatoria que desea")

varStringVariable=tk.StringVar()

listboxVa=ttk.Combobox(master,
                     textvariable=varStringVariable,
                     height=6)
listboxVa["values"]=["Box Muller","Logaritmica Normal","Chi cuadrado normal","T","F","Exponencial","Gamma","Composicion",
                     "Transformada Directa","Transformada Inversa","Aceptacion y rechazo"]
listboxVa["state"]="readonly"

LabelMetodo.place(x=300,y=50)
listboxVa.place(x=300,y=70)
listboxVa.config(width = 30)





listboxAl.bind("<<ComboboxSelected>>",algoritmoSeleccionado)

listboxVa.bind("<<ComboboxSelected>>",VariableSeleccionada)

tk.mainloop()