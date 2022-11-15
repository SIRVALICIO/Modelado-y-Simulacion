
def VisualBase(x0):
    X0=int(x0)


    resultados_ri=[]
    for i in range (0,1000000):
        #x_1= ( 1140671485 + (12820163+X0))%(2**24)
        x_1 = (1140671485 * (12820163 + X0)) % (2 ** 24)
        ri=(x_1)/((2**24)-1)
        resultados_ri.append(ri)
        X0=x_1


    return resultados_ri

def Fortran(x0):
    X0=int(x0)


    resultados_ri=[]
    for i in range (0,1000000):
        x_1= ( 630360016*(X0+1))%((2**31)-1)
        ri=(x_1)/((2**31)-1)
        resultados_ri.append(ri)
        X0=x_1


    return resultados_ri

def ConguencialMultplicativo(g,k,x0):
    X0 = int(x0)
    g=abs(int(g))
    k=abs(int(k))

    if X0%2==0:
        X0+=1

    m=2**g
    a=5+(8*k)
    resultados_ri = []
    for i in range(0, m):
        x_1 =(a*X0)%m
        ri = (x_1) / (m)
        resultados_ri.append(ri)
        X0 = x_1
    return resultados_ri

def CongruencialCuadratico(g,a,b,c,x0):
    X0 = int(x0)
    g = abs(int(g))
    a=int(a)
    b=int(b)
    c=int(c)
    if a % 2 != 0:
        a += 1
    if c%2!=1:
        c+=1

    #if (b-1)%4!=1:
        #while (b-1)%4!=1:
            #b+=1


    m = 2 ** g
    print(a,b,c,X0,g)
    resultados_ri = []
    for i in range(0, m):
        x_1 = ( (a*(X0**2) )+ (b*X0) +(c)) % m

        ri = (x_1) / (m)
        resultados_ri.append(ri)
        X0 = x_1
    return resultados_ri

def AlgoritmoLineal(a,x,c,m):
    xresultante=((a*x)+c)%m
    return xresultante

def ResolverLieal(k,c,g,x):



    m=int(2**g)
    a=1+(4*k)

    semilla=[]
    pseudoAle=[]

    semilla.append(AlgoritmoLineal(a,x,c,m))
    pseudoAle.append(semilla[-1]/(m-1))

    for i in range(0,m):
        semilla.append(AlgoritmoLineal(a, semilla[-1], c, m))
        pseudoAle.append(semilla[-1] / (m - 1))

    return pseudoAle