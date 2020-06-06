#Emilio Campuzano Mejia
#A01378948

import pandas as pd


movies = ['Exmachina', 'Yo, Robot', 'Inteligencia Artificial', '2001, odisea', 'Matrix', 'Blade Runner']


def getRatings():
    '''Esta funcion regresa una lista de puntajes que el usuaria debe introducir'''
    ratings = []
    for i in range(6):
        rating=float(input('Cual es la calificacion para la pelicula {0}: '.format(movies[i])))
        ratings.append(rating)
    return ratings


def getViews(lista):
    '''Esta funcion regresa una lista de todas las peliculas que si ha visto el usuario.'''
    views = []
    for i in lista:
      if i > 0:
          views.append(i)
    return views


def getIndNoViews(lista):
    '''Esta funcion regresa una lista de las peliculas que NO ha visto el usuario (no literalmente el 
    nombre,sino la posicion de acuerdo a movies)'''
    noViews = []
    cont = 0
    for i in lista:
        if i == 0:
            noViews.append(cont)
        cont += 1
    return noViews


def getIndViews(lista):
    '''Esta funcion regresa una lista de las peliculas que SI ha visto el usuario (no literalmente el 
    nombre, sino la posicion de acuerdo a movies)'''
    #lista es 
    views = []
    cont = 0
    for i in lista:
        if i != 0:
            views.append(cont)
        cont += 1
    return views


def getNewBase(df, lista):
    '''Esta funcion regresa un data frame reestructurado. Lista es lo que delimita su nueva
    composicion'''
    return df.iloc[:,lista]


def dist(lista1,lista2):
    '''Esta funcion regresa el valor que existe entre 2 puntos, es decir, la distancia 
    euclideana. '''
    x = len(lista1)
    y = len(lista2)
    if x == y:
        cont=0
        for i in range(len(lista1)):
            cont+= (lista1[i]-lista2[i]) **2
        ans = cont**(.5)
        return ans


def putInd(lista):
    '''Esta funcion regresa una lista de listas. En cada sublista se encuentra un valor
    y la posicion de donde se saco ese valor.'''
    indice=[]
    for x in range(len(lista)):
        indice.append([lista[x], x])
    return indice


def kmin(k, lista):
    '''Esta funcion regresa una lista con los menores elementos de 'lista'. Puede regresar varios ya que 
    'k' delimita el numero de elementos que se regresan'''
    lista.sort()
    return lista[:k]


def maxPun(base):
    '''Esta funcion hace una sumatoria por columnas de un dataframe. El nombre de la columna con
    la sumatoria mas alta es lo que devuelve la funcion.'''
    puntuaciones = []
    for i in base:
        x = sum(base[i])
        puntuaciones.append([x, i])
    return max(puntuaciones)[1]


def recomendar(k,base):
    '''Esta funcion devuelve una sugerencia al usuario de cual pelicula deberia ver de acuerdo a su lista de preferencias '''
    #k es un int positivo
    # base es un DataFrame de ratings de peliculas

    ratings = getRatings()#lista de los valores que el usuario puso

    views = getViews(ratings) #lista de solo las peliculas que ha visto

    viewsInd = getIndViews(ratings) # indice de peliculas si vistas
    noViewsInd = getIndNoViews(ratings) # indice de peliculas no vistas

    dataFrameV = getNewBase(base,viewsInd) #base de datos que el usuario ha visto
    dataFrameNV = getNewBase(base, noViewsInd) #base de datos que el usuario no ha visto

    distancia = []
    x = []
    for i in range(len(dataFrameV)):
        d = dataFrameV.iloc[i,:]
        distancia.append(dist(d,views))

    nd = putInd(distancia)
    minimum = kmin(k,nd)

    for j in minimum:
        x.append(j[1])
    
    lastDataFrame = dataFrameNV.iloc[x]
    recomendation = maxPun(lastDataFrame)
    return 'La pelilcula que mas te recomiendo ver es la de: {0}'.format(recomendation)


def main():

    # Lista de pruebas de cada funcion:
    # print('ejercicio 1', getRatings(),'\n')
    # print('ejercio 2', getViews([4, 0, 3.5, 5, 5, 0]),'\n')
    # print('ejercio 3', getIndNoViews([4, 0, 3.5, 5, 5, 0]),'\n')
    # print('ejercio 4', getIndViews([4 , 0, 3.5, 5, 5, 0]),'\n')
    # print('ejercio 5')
    # baseP = [[4.5, 4, 4, 5, 4.5, 5], [3, 4.5, 3.5, 2, 5, 3], [5, 4.5, 4.5, 4.5, 5, 4], [4, 4.5, 4.5, 3, 5, 3.5]]
    # baseP_df = pd.DataFrame(baseP, columns = movies)
    # print(getNewBase(baseP_df,[1,5]),'\n')
    # print('ejercicio 6',dist([0,0,0],[1,1,1]),'\n')
    # print('ejercicio 7',putInd([1,2,3,1,'kk']),'\n')
    # print('ejercicio 8','\n',kmin(3,[4,5,2,7,1,9]),'\n')
    # print('ejercicio 8','\n',kmin(5,[[2,3],[1,3],[5,8],[7,6],[0,4],[7,2],[9,5],[1,2],[4,6]]),'\n')
    # print('ejercio 9')
    # basePp = [[4.5, 4, 4, 5, 4.5, 5], [3, 4.5, 3.5, 2, 5, 3], [5, 4.5, 4.5, 4.5, 5, 4], [4, 4.5, 4.5, 3, 5, 3.5]]
    # basePp_df = pd.DataFrame(basePp, columns = movies)
    # print(maxPun(basePp_df),'\n')
    # print('ejercicio 10')
    # basp = [[3, 4, 3, 4, 4, 2], [3, 5, 3, 4, 5, 4], [3, 4.5, 5, 3, 4, 3], [3.5, 4, 3.5, 4.5, 5, 5], [4.5, 3.5, 4, 4, 4.5, 4],
    #     [3, 4.5, 4, 3, 2.5, 3], [4, 4.5, 3.5, 5, 4, 4], [5, 4.5, 4, 4, 4.5, 4.5], [3.5, 3, 4, 5, 3.5, 4.5],
    #     [3, 5, 1, 4.5, 3.5, 1.5], [3, 5, 3, 4, 5, 3.5], [2.5, 4.5, 3, 3, 3.5, 4.5], [3.5, 5, 2.5, 3, 4.5, 5]]
    # basdf = pd.DataFrame(basp, columns = movies)
    # print(recomendar(2, basdf)) , ratings = [4.5, 0, 4, 4.5, 0, 5]
    # print(recomendar(2, baseP_p_df)), ratings =[3, 0, 5, 3, 0, 4]
    # print(recomendar(3, baseP_p_df)),ratings = [5, 0, 0, 0, 4, 2]
    # print(recomendar(5, baseP_p_df)),ratings = [0, 3, 4, 4, 0, 0]
    # print(recomendar(7, baseP_p_df)), ratings =[4, 5, 5, 0, 5, 0]
    
    
    
    
    # insertar aqui la base de datos 
    
    #Asegurarse de que la base de datos solo tenga la informacion que necesitamos analizar
    #Si contiene al mas asegurarse de borrar lo que no se utiliza
    
    
    base_de_datos = pd.read_csv("Ciencia Ficción.csv") #agregar el nombre del archivo
    a = base_de_datos.drop('Estudiante', axis = 1)
    b = a.drop('Ciencia Ficción', axis = 1)
    # a y b borran columnas que no se utilizan para el analisis
    print(recomendar(2,b)) # agregar k

main()
