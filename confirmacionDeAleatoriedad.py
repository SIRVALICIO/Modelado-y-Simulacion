import scipy.stats
import pandas as pd
import matplotlib.pyplot as plot
from scipy import stats
def media(lista):
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
    print("Prueba media\n")
    n=len(lista)


    media= 1/n * sum(lista)
    print("La media es: ",media)

    li= 1/2 - (scipy.stats.norm.ppf (1-0.025)*(1/(12*((n)**(1/2)))))
    ls=1/2 + (scipy.stats.norm.ppf (1-0.025)*(1/(12*((n)**(1/2)))))
    print("El limite inferio es: ",li, " y el limite superior es: ",ls,"\n")

    if( media>=li and media<=ls):
        print("La secuencia es pseduoaletaoria debido a que la media: ",media, " se encuentra entre los limites\n")
    else:
        print("La secuencia no es pseudo aleatoria debido a que la media no se encuentra entre los limitres impuestos\n")


sec="ab"

#print(scipy.stats.chi2.ppf(1-0.025,39)) #con la funcion de chi caudarado se debe tener en cuenta que para el limitre superior no se pone 1-alpha si no solamente alpha por como funciona la funcion, lo mismo con le limite inferior, se debe poner es 1-añpha en vez de solo alpha
#print(scipy.stats.norm.ppf (1-0.025)) con esta funcion encutnras el valor de la tabla de distribucion normal que necesitaas
def varianza(lista):
        print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
        print("Prueba varianza\n")
        n = len(lista)

        media = 1 / n * sum(lista)

        total=0
        for i in lista:
            total+= (i-media)**2

        var=total/(n-1)

        livar=(scipy.stats.chi2.ppf(1-0.025,n-1))/(12*(n-1))
        lsvar=(scipy.stats.chi2.ppf(0.025,n-1))/(12*(n-1))
        print("La varianza es de: ",var,"\n")
        print("El limite inferior es: ",livar," Y el limite superior es: ",lsvar,"\n")

        if (var >= livar and var <= lsvar):
            print("La secuencia es pseduoaletaoria debido a que la varianza: ", var, " se encuentra entre los limites\n")
        else:
            print("La secuencia no es pseudo aleatoria debido a que la media no se encuentra entre los limitres impuestos\n")

def Prueba_corrida_media(lista):
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
    print("\nPrueba de corridas arriba y abajo de la media ")
    n= len(lista)
    media = 1 / n * sum(lista)
    arribaMedia=0
    abajoMediao=0

    secuenccia=""
    corridas=0

    for i in lista:
        if secuenccia=="":
            if i<media:
                abajoMediao+=1
                secuenccia+="-"
            elif i>media:
                arribaMedia+=1
                secuenccia+="+"
            corridas+=1
        else:
            if i < media:
                abajoMediao += 1
                secuenccia += "-"
            elif i > media:
                arribaMedia += 1
                secuenccia += "+"
            if secuenccia[-2]!=secuenccia[-1]:
                corridas+=1
    print(secuenccia)
    print("Datos arriba de la media: ",arribaMedia)
    print("Datos debaho de la media: ",abajoMediao)
    print("Numero de corridas",corridas)

    u=((2*arribaMedia*abajoMediao)/(arribaMedia+abajoMediao))+1
    alpha= (2*arribaMedia*abajoMediao*((2*arribaMedia*abajoMediao)-n))/((n**2)*(n-1))
    z=(corridas-u)/((alpha)**(1/2))
    if abs(z)<scipy.stats.norm.ppf (1-0.025):
        print("La secuencia es pesudo aleatoria debido a que el valor de z teorico: ",abs(z), " Es menor al valor esperado del error de: ",scipy.stats.norm.ppf (1-0.025))
    else:
        print("NO es una  secuencia pseudoaletoria debido a que el error de: ",scipy.stats.norm.ppf (1-0.025)," a sido excedido")

def graficaDeLaNormal(lista):
    print(
        "*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
    print("\nPrueba visual por medio por el diagrama de la normal, como esta prueba es visual depende del usuario identiciar si es o no pseudoalatorio ")


    df=pd.DataFrame({ "numerosAleatorios":lista})
    print(df)
    fig = plot.figure()
    ax = fig.add_subplot(111)
    res = stats.probplot(df["numerosAleatorios"], dist=stats.norm, sparams=(6,), plot=ax)
    plot.show()