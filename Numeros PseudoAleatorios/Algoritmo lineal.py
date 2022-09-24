import confirmacionDeAleatoriedad


def resolver(a,x,c,m):
    xresultante=((a*x)+c)%m
    return xresultante



k= int(input("Ingrese un valor de k, recomendado un valor entro: "))
c=int(input("Ingrese un valor de c, recomendado que sea un primo relativo a m: "))
g=int(input("Ingrese un valor de g, recomendado que sea entero: "))
x=int(input("Ingrese un valor de Xo: "))
ite=int(input("Ingresar el numero de iteraciones que quiere: "))
m=2**g
a=1+(4*k)

semilla=[]
pseudoAle=[]

semilla.append(resolver(a,x,c,m))
pseudoAle.append(semilla[-1]/(m-1))

for i in range(0,ite):
    semilla.append(resolver(a, semilla[-1], c, m))
    pseudoAle.append(semilla[-1] / (m - 1))

for x in pseudoAle:
    print(x)

confirmacionDeAleatoriedad.media(pseudoAle)
confirmacionDeAleatoriedad.varianza(pseudoAle)
confirmacionDeAleatoriedad.Prueba_corrida_media(pseudoAle)
confirmacionDeAleatoriedad.graficaDeLaNormal(pseudoAle)
