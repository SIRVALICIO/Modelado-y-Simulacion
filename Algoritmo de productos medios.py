import confirmacionDeAleatoriedad
def numeroPseudo(result,result2):

    result=result*result2


    result=str(result)
    while (len(result) >5):
        result=result[1::]

        result=result[:-1:]


    return int(result)

seed=int(input("Ingrese una semilla: "))
seed2= int(input("Ingrese la segunda semilla:"))
ri=int(input("Cuantos numero quiere que se generen con esta semilla?: "))


semillas=[]
resultados=[]
if seed.__sizeof__()<4:
    print("No se pueden generar numeros por que la longitud de la semilla es menor de 4")
else:
    x = numeroPseudo(seed,seed2)
    y = 10 ** len(str(x))
    semillas.append(x)
    resultados.append(float( "{:.4f}".format((x/y))))


    antes=seed2
    ahora=semillas[0]
    for i in range(1,ri):

        x=numeroPseudo(antes,ahora)
        #print(x)
        y=10** len(str(x))
        #print(y)
        resultados.append(x/y)
        semillas.append(x)
        antes=ahora
        ahora=semillas[i]

#print(semillas)
print(resultados)

print("los resultados son: ")
for x in resultados:
    print(x)


confirmacionDeAleatoriedad.media(resultados)
confirmacionDeAleatoriedad.varianza(resultados)
confirmacionDeAleatoriedad.Prueba_corrida_media(resultados)
confirmacionDeAleatoriedad.graficaDeLaNormal(resultados)
