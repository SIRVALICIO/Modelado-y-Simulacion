import confirmacionDeAleatoriedad


def resolver(a,x,m):
    xresultante=((a*x))%m
    return xresultante



k= int(input("Ingrese un valor de k, recomendado un valor entro: "))

g=int(input("Ingrese un valor de g, recomendado que sea entero: "))
x=int(input("Ingrese un valor de Xo que sea impar: "))
ite=int(input("Ingresar el numero de iteraciones que quiere: "))
m=2**g
a=5+(8*k)

semilla=[]
pseudoAle=[]

semilla.append(resolver(a,x,m))
pseudoAle.append(semilla[-1]/(m-1))

for i in range(0,ite):
    semilla.append(resolver(a, semilla[-1],  m))
    pseudoAle.append(semilla[-1] / (m - 1))

for x in pseudoAle:
    print(x)

confirmacionDeAleatoriedad.media(pseudoAle)
confirmacionDeAleatoriedad.varianza(pseudoAle)
confirmacionDeAleatoriedad.Prueba_corrida_media(pseudoAle)
confirmacionDeAleatoriedad.graficaDeLaNormal(pseudoAle)
