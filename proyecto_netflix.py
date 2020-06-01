#Emilio Campuzano Mejia
#A01378948
import pandas as pd


movies = 'Exmachina' , 'Yo Robot', 'AI' , '2001' , 'Matrix' , 'Blade Runner'



def getRatings():
    '''Esta funcion regresa una lista de puntajes que el usuaria debe introducir'''
    ratings = []
    for i in range(6):
        rating=float(input('Cual es la calificacion para la pelicula {0}: '.format(movies[i])))
        ratings.append(rating)
    return ratings


def getViews(lista):
    '''Esta funcion regresa una lista de todas las peliculas que si ha visto el usuario'''
    views = []
    for i in lista:
      if i > 0:
          views.append(i)
    return views


def getIndNoViews(lista):
    noViews = []
    cont = 0
    for i in lista:
        if i == 0:
            noViews.append(cont)
        cont += 1
    return noViews


def getIndViews(lista):
    views = []
    cont = 0
    for i in lista:
        if i != 0:
            views.append(cont)
        cont += 1
    return views


def getNewBase(df, lista):
    x = df
    newList = []
    for i in lista:
        if type(i) == int:
            newList.append(i)
    return x.iloc[:,newList]


def dist(lista1,lista2):
    x = len(lista1)
    y = len(lista2)
    if x == y:
        cont=0
        for i in range(len(lista1)):
            cont+= (lista1[i]-lista2[i]) **2
        ans = cont**(.5)
        return ans

def putInd(lista):
    indice=[]
    for x in lista:
      indice.append([x, lista.index(x)])
    return indice


def kmin(k, lista):
    lista.sort()
    return lista[:k]


def maxPun(base):
    puntuaciones = []
    for i in base:
        x = sum(base[i])
        puntuaciones.append([x, i])
    return max(puntuaciones)[1]


def recomendar(k,base):
    '''Esta funcion devuelve una sugerencia al usuario de cual pelicula deberia ver de acuerdo a su lista de preferencias '''
    #k es un int positivo
    # base es un DataFrame de ratings de peliculas
    ratings = getRatings()
    views = getViews(ratings)
    noViews = getIndNoViews(ratings)

    x=[]
    distancia=[]
    for i in base:
        a = getCoor(i)
        distancia.append(dist(punto,a))
    nd=putInd(distancia)
    min_=kmin(k,nd)
    for j in min_:
        x.append(j[1])

    color=getNearColors(base,x)

    result=[]
    for i in lista2:
        result.append(lista1[i][-1])

    return mode(color)




def main():

    print('ejercicio 1 - 9')
    print('ejercicio 1', getRatings(),'\n')
    print('ejercio 2', getViews([4, 0, 3.5, 5, 5, 0]),'\n')
    print('ejercio 3', getIndNoViews([4, 0, 3.5, 5, 5, 0]),'\n')
    print('ejercio 4', getIndViews([4 , 0, 3.5, 5, 5, 0]),'\n')
    print('ejercio 5')
    baseP = [[4.5, 4, 4, 5, 4.5, 5], [3, 4.5, 3.5, 2, 5, 3], [5, 4.5, 4.5, 4.5, 5, 4], [4, 4.5, 4.5, 3, 5, 3.5]]
    baseP_df = pd.DataFrame(baseP, columns = movies)
    print(getNewBase(baseP_df,[1,5]),'\n')
    print('ejercicio 6',dist([0,0,0],[1,1,1]),'\n')
    print('ejercicio 7',putInd([1,2,3,1,'kk']),'\n')
    print('ejercicio 8','\n',kmin(3,[4,5,2,7,1,9]),'\n')
    print('ejercicio 8','\n',kmin(5,[[2,3],[1,3],[5,8],[7,6],[0,4],[7,2],[9,5],[1,2],[4,6]]),'\n')
    print('ejercio 9')
    basePp = [[4.5, 4, 4, 5, 4.5, 5], [3, 4.5, 3.5, 2, 5, 3], [5, 4.5, 4.5, 4.5, 5, 4], [4, 4.5, 4.5, 3, 5, 3.5]]
    basePp_df = pd.DataFrame(basePp, columns = movies)
    print(maxPun(basePp_df),'\n')


main()
