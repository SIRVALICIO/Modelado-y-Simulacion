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

def composicion(listaABC,R1,R2,tamaño):
    resultados=[]
    ListaProbabilidades=[]
    prabilidad=0
    resul=0

    total=listaABC[-1][-1]-listaABC[0][0]
    print(len(listaABC))
    for i in range (0,len(listaABC)):
        a=listaABC[i][0]
        b=listaABC[i][1]
        c=listaABC[i][2]

        prabilidad+= (b-a)/total
        ListaProbabilidades.append(prabilidad)
        prabilidad+= (c-b)/total
        ListaProbabilidades.append(prabilidad)


    print(ListaProbabilidades)


    if len(ListaProbabilidades)==2:
        for i in range(0, tamaño):
            if R1[i]<=ListaProbabilidades[0]:
                resul= listaABC[0][0]+(math.sqrt(R2[i])*(listaABC[0][1]-listaABC[0][0]))
                ListaProbabilidades.append(resul)
            else:
                resul= listaABC[0][2]-(math.sqrt(1-R2[i])*(listaABC[0][2]-listaABC[0][1]))
                ListaProbabilidades.append(resul)
    elif  len(ListaProbabilidades)==4:
        for i in range(0, tamaño):
            if R1[i]<=ListaProbabilidades[0]:
                resul= listaABC[0][0]+(math.sqrt(R2[i])*(listaABC[0][1]-listaABC[0][0]))
                ListaProbabilidades.append(resul)
            elif R1[i]<=ListaProbabilidades[1]:
                resul= listaABC[0][2]-(math.sqrt(1-R2[i])*(listaABC[0][2]-listaABC[0][1]))
                ListaProbabilidades.append(resul)
            elif R1[i]<=ListaProbabilidades[2]:
                resul= listaABC[1][0]+(math.sqrt(R2[i])*(listaABC[1][1]-listaABC[1][0]))
                ListaProbabilidades.append(resul)
            else:
                resul= listaABC[1][2]-(math.sqrt(1-R2[i])*(listaABC[1][2]-listaABC[1][1]))
                ListaProbabilidades.append(resul)
    elif  len(ListaProbabilidades)==6:
        for i in range(0, tamaño):
            if R1[i]<=ListaProbabilidades[0]:
                resul= listaABC[0][0]+(math.sqrt(R2[i])*(listaABC[0][1]-listaABC[0][0]))
                ListaProbabilidades.append(resul)
            elif R1[i]<=ListaProbabilidades[1]:
                resul= listaABC[0][2]-(math.sqrt(1-R2[i])*(listaABC[0][2]-listaABC[0][1]))
                ListaProbabilidades.append(resul)
            elif R1[i]<=ListaProbabilidades[2]:
                resul= listaABC[1][0]+(math.sqrt(R2[i])*(listaABC[1][1]-listaABC[1][0]))
                ListaProbabilidades.append(resul)
            elif R1[i]<=ListaProbabilidades[3]:
                resul= listaABC[1][2]-(math.sqrt(1-R2[i])*(listaABC[1][2]-listaABC[1][1]))
                ListaProbabilidades.append(resul)
            elif R1[i]<=ListaProbabilidades[4]:
                resul= listaABC[2][0]+(math.sqrt(R2[i])*(listaABC[2][1]-listaABC[2][0]))
                ListaProbabilidades.append(resul)
            else:
                resul= listaABC[2][2]-(math.sqrt(1-R2[i])*(listaABC[2][2]-listaABC[2][1]))
                ListaProbabilidades.append(resul)
    elif  len(ListaProbabilidades)==8:
        for i in range(0, tamaño):
            if R1[i]<=ListaProbabilidades[0]:
                resul= listaABC[0][0]+(math.sqrt(R2[i])*(listaABC[0][1]-listaABC[0][0]))
                ListaProbabilidades.append(resul)
            elif R1[i]<=ListaProbabilidades[1]:
                resul= listaABC[0][2]-(math.sqrt(1-R2[i])*(listaABC[0][2]-listaABC[0][1]))
                ListaProbabilidades.append(resul)
            elif R1[i]<=ListaProbabilidades[2]:
                resul= listaABC[1][0]+(math.sqrt(R2[i])*(listaABC[1][1]-listaABC[1][0]))
                ListaProbabilidades.append(resul)
            elif R1[i]<=ListaProbabilidades[3]:
                resul= listaABC[1][2]-(math.sqrt(1-R2[i])*(listaABC[1][2]-listaABC[1][1]))
                ListaProbabilidades.append(resul)
            elif R1[i]<=ListaProbabilidades[4]:
                resul= listaABC[2][0]+(math.sqrt(R2[i])*(listaABC[2][1]-listaABC[2][0]))
                ListaProbabilidades.append(resul)
            elif R1[i]<=ListaProbabilidades[5] :
                resul= listaABC[2][2]-(math.sqrt(1-R2[i])*(listaABC[2][2]-listaABC[2][1]))
                ListaProbabilidades.append(resul)
            elif R1[i]<=ListaProbabilidades[6]:
                resul= listaABC[3][0]+(math.sqrt(R2[i])*(listaABC[3][1]-listaABC[3][0]))
                ListaProbabilidades.append(resul)
            else:
                resul= listaABC[3][2]-(math.sqrt(1-R2[i])*(listaABC[3][2]-listaABC[3][1]))
                ListaProbabilidades.append(resul)
    else:
        for i in range(0, tamaño):
            if R1[i] <= ListaProbabilidades[0]:
                resul = listaABC[0][0] + (math.sqrt(R2[i]) * (listaABC[0][1] - listaABC[0][0]))
                ListaProbabilidades.append(resul)
            elif R1[i] <= ListaProbabilidades[1]:
                resul = listaABC[0][2] - (math.sqrt(1 - R2[i]) * (listaABC[0][2] - listaABC[0][1]))
                ListaProbabilidades.append(resul)
            elif R1[i] <= ListaProbabilidades[2]:
                resul = listaABC[1][0] + (math.sqrt(R2[i]) * (listaABC[1][1] - listaABC[1][0]))
                ListaProbabilidades.append(resul)
            elif R1[i] <= ListaProbabilidades[3]:
                resul = listaABC[1][2] - (math.sqrt(1 - R2[i]) * (listaABC[1][2] - listaABC[1][1]))
                ListaProbabilidades.append(resul)
            elif R1[i] <= ListaProbabilidades[4]:
                resul = listaABC[2][0] + (math.sqrt(R2[i]) * (listaABC[2][1] - listaABC[2][0]))
                ListaProbabilidades.append(resul)
            elif R1[i] <= ListaProbabilidades[5]:
                resul = listaABC[2][2] - (math.sqrt(1 - R2[i]) * (listaABC[2][2] - listaABC[2][1]))
                ListaProbabilidades.append(resul)
            elif R1[i] <= ListaProbabilidades[6]:
                resul = listaABC[3][0] + (math.sqrt(R2[i]) * (listaABC[3][1] - listaABC[3][0]))
                ListaProbabilidades.append(resul)
            elif R1[i] <= ListaProbabilidades[7]:
                resul = listaABC[3][2] - (math.sqrt(1 - R2[i]) * (listaABC[3][2] - listaABC[3][1]))
                ListaProbabilidades.append(resul)
            elif R1[i] <= ListaProbabilidades[8]:
                resul = listaABC[4][0] + (math.sqrt(R2[i]) * (listaABC[4][1] - listaABC[4][0]))
                ListaProbabilidades.append(resul)
            else:
                resul = listaABC[4][2] - (math.sqrt(1 - R2[i]) * (listaABC[4][2] - listaABC[4][1]))
                ListaProbabilidades.append(resul)
    return ListaProbabilidades

