import random as rd

def dist(list1,list2):
    cont=0
    for x in range(len(list1)):
        cont+=(list1[x]-list2[x])**2
    ans= cont**(.5)
    return ans

def getCoor(lista):
    return lista[:-1]

def putInd(lista):
    indice=[]
    for x in lista:
         indice.append([x, lista.index(x)])
    return indice

def getNearColors(lista1,lista2):
    result=[]
    for i in lista2:
        result.append(lista1[i][-1])
    return result

def kmin(k,lista):
    lista.sort()
    return lista[0:k]

def kNN(k,listaPuntos,punto):#lista de puntos coloreados=listaPuntos , punto sin color = punto
    e=[]
    for i in listaPuntos:
        f = getCoor(i)
        e.append(f)
    g = []
    for i in e:
        di = dist(i,punto)
        g.append(di)
    posiciones = putInd(g)
    pos=[]
    for i in range(len(posiciones)):
        h=posiciones[i][0]
        pos.append(h)
        
    kk = Kmin(k,e)
    indices = []
    for i in range(len(kk)):
        ind = pos.index(kk[i])
        indices.append(ind)
    colores = getNearColors(listaPuntos,indices)
    color=mode(colores)
    return color


def main():
    print('ejercicio 1','\n',dist([0,0,0],[1,1,1]),'\n')
    print('ejercicio 2','\n',getCoor([1,2,3,'cafe']),'\n')
    print('ejercicio 3','\n',putInd([1,2,3,1,'kk']),'\n')
    print('ejercicio 4','\n',getNearColors([[1,2,3,'rojo'],[4,5,6,'azul'],[7,8,9,'amarillo']],[0,2]),'\n')
    print('ejercicio 5','\n',kmin(3,[4,5,2,7,1,9]),'\n')
    print('ejercicio 5','\n',kmin(5,[[2,3],[1,3],[5,8],[7,6],[0,4],[7,2],[9,5],[1,2],[4,6]]),'\n')
    rd.seed(777)
    puntos = []
    for k in range(50):
        puntos.append([rd.randint(1,100), rd.randint(1,100), rd.randint(1,100), rd.choice(['amarillo','azul', 'rojo'])])
    print('ejercicio 6','\n',kNN(5,puntos,[20,30,40]),'\n')
    print('ejercicio 6','\n',kNN(5,puntos,[11,53,89]),'\n')
    print('ejercicio 6','\n',kNN(5,puntos,[97,11,54]),'\n')
    rd.seed(777)
    puntos = []
    for k in range(500):
        puntos.append([rd.randint(1,100), rd.randint(1,100), rd.randint(1,100), rd.choice(['amarillo','azul', 'rojo'])])
    print('ejercicio 6','\n',kNN(5,puntos,[11,80,77]),'\n')


main()
