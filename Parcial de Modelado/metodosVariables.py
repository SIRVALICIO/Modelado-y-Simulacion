import numpy as np
import math

def limpiarXI():
    listaXI.clear()
    listaCHI2.clear()

listaXI=[]
listaCHI2=[]

def boxMuller(lista,media ,varianza, cantidad):
    vectorXi=[]

    r1=lista[0]
    r2=lista[1]

    for i in range (0,cantidad):
            #print("r2 ",r1[i])
            #print("r2 ",r2[i])
            z1= math.sqrt(-2*np.log10(r1[i]))
            z2=math.cos(2*np.pi *r2[i])
            #print("Numerador ",z1)
            #print("denominador ",z2)
            zi= z1*z2
            Xi=10+ (2*zi)
            vectorXi.append(Xi)
    listaXI.append(vectorXi)
    vectorXi.sort()
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
        total= (total / len(listaCHI2)) ** (1 / 2)
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
def gamma(lista,cantidad,alpha,beta):
    r1 = lista[0]
    r2 = lista[1]

    a= 1/math.sqrt((2*alpha)-1)
    b=alpha - np.log10(4)
    q= alpha+(1/alpha)
    teta=4.5
    d= 1 + np.log10(teta)
    listaGamma=[]
    for i in range(0, cantidad):
        vi= a * np.log10(r1[i]/(1-r2[i]))
        zi= (r1[i]**2)*r2[i]
        yi=  alpha * (np.e**vi)
        wi=b+ (q*vi) - yi
        if (wi+d)-(teta*zi)> 0:
            listaGamma.append(beta*yi)
        elif wi>=np.log10(zi):
            listaGamma.append(beta * yi)
    return listaGamma