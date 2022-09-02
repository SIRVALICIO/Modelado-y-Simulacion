import confirmacionDeAleatoriedad


def resolver(a,x,b,c,m):
    xresultante=((a*((x)**2))+(b*x)+c)%m
    return xresultante



a= int(input("Ingrese un valor de a, recomendado un valor par: "))


c= int(input("Ingrese un valor de c, recomendado un valor impar: "))

g=int(input("Ingrese un valor de g, recomendado que sea entero: "))

b=int(input("Ingrese un valor de b: "))

ite=int(input("Ingresar el numero de iteraciones que quiere: "))

x=int(input("Ingrese un valor de Xo que sea impar: "))
m=2**g


semilla=[]
pseudoAle=[]

semilla.append(resolver(a,x,b,c,m))
pseudoAle.append(semilla[-1]/(m-1))

for i in range(0,ite):
    semilla.append(resolver(a,semilla[-1],b,c,m))
    pseudoAle.append(semilla[-1] / (m - 1))

for x in pseudoAle:
    print(x)

confirmacionDeAleatoriedad.media(pseudoAle)
confirmacionDeAleatoriedad.varianza(pseudoAle)
confirmacionDeAleatoriedad.Prueba_corrida_media(pseudoAle)
confirmacionDeAleatoriedad.graficaDeLaNormal(pseudoAle)
