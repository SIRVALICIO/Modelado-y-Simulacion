import confirmacionDeAleatoriedad
def numeroPseudo(result):

    result = result ** 2


    result=str(result)
    while (len(result) >5):
        result=result[1::]

        result=result[:-1:]


    return int(result)

seed=int(input("Ingrese una semilla: "))
ri=int(input("Cuantos numero quiere que se generen con esta semilla?: "))


semillas=[]
resultados=[]
if seed.__sizeof__()<4:
    print("No se pueden generar numeros por que la longitud de la semilla es menor de 4")
else:
    x = numeroPseudo(seed)
    y = 10 ** len(str(x))
    semillas.append(x)
    resultados.append( float("{:.4f}".format((x/y))))
    for i in range(1,ri):

        x=numeroPseudo(semillas[i - 1])
        #print(x)
        y=10** len(str(x))
        #print(y)
        resultados.append(x/y)
        semillas.append(x)

#print(semillas)
print(resultados)

print("los resultados son: ")
for x in resultados:
    print()


confirmacionDeAleatoriedad.media(resultados)
confirmacionDeAleatoriedad.varianza(resultados)
confirmacionDeAleatoriedad.Prueba_corrida_media(resultados)
confirmacionDeAleatoriedad.graficaDeLaNormal(resultados)
