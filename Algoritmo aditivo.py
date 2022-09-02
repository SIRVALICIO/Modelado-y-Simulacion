import confirmacionDeAleatoriedad


def algoritmo(x1,x2,m):
    resultante=(x1+x2)%m
    return resultante


numeros=[]
resultados=[]
imax=int(input("Ingrese cuantos numeros piensa ingresar: "))

for i in range(0,(imax)):

    numeros.append(int(input("Ingrese un numero entero: ")))


m=int(input("Ingrese un valor de m: "))
iter=int(input("Ingrese cuantas iteraciones quiere: "))
cont=0
for j in range(0,iter):

    numeros.append(algoritmo(numeros[-1],numeros[cont],m))
    resultados.append(numeros[-1]/(m-1))
    cont+=1

for j in resultados:
    print(j)


confirmacionDeAleatoriedad.media(resultados)
confirmacionDeAleatoriedad.varianza(resultados)
confirmacionDeAleatoriedad.Prueba_corrida_media(resultados)
confirmacionDeAleatoriedad.graficaDeLaNormal(resultados)
