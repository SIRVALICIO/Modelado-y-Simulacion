import numpy as np
import math

listaXI=[]
listaCHI2=[]

def boxMuller(lista,media ,varianza, cantidad):
    vectorXi=[]

    r1=lista[0]
    r2=lista[1]

    for i in range (0,cantidad):
            zi= ((-2*np.log(r1[i]))**(1/2)) * math.cos((2*np.pi)*r2[i])
            Xi=media+ (varianza*zi)
            vectorXi.append(Xi)
    listaXI.append(vectorXi)
    return  vectorXi
def logaritmica(cantidad):
    Xi=listaXI[0]
    vectorXiLn=[]
    for i in range(0,cantidad):
        XiLN=np.e **Xi[i]
        vectorXiLn.append(XiLN)
    return  vectorXiLn

def chi2(cantidad):
    vectorCHI2=[]
    for i in range(0,cantidad):
        total = 0
        for j in listaXI:
            total+= j[i]**2
        print(total)
        vectorCHI2.append(total)
    listaCHI2.append(vectorCHI2)
    return vectorCHI2

def t(cantidad):
    vectorT=[]
    Xi=listaXI[0]
    for i in range(0,cantidad):
        total = 0
        for j in listaXI:
            total+= j[i]
        print(total)
        total= (total/listaCHI2.count())**(1/2)
        res=Xi[i]/total
        vectorT.append(res)
    return vectorT

def f(cantidad):
    CHI21=listaCHI2[0]
    CHI22=listaCHI2[1]
    vectorF=[]
    for i in range(0,cantidad):
        res=CHI21[i]/CHI22[i]
        vectorF.append(res)
    return vectorF

def exponencual(cantidad,tasa):
    vectorF=[]
    XI=listaXI[0]
    for i in range(0,cantidad):
        resul= (-1/tasa ) * np.log10(XI[i])
        vectorF.append(resul)
    return vectorF