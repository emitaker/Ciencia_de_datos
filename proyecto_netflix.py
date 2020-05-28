#Emilio Campuzano Mejia
#A01378948
import pandas as pd


movies = 'Exmachina' , 'Yo Robot', 'AI' , '2001' , 'Matrix' , 'Blade Runner'



def getRatings():
    ratings = []
    for i in range(6):
        rating=int(input('Cual es la calificacion para la pelicula {0}: '.format(movies[i])))
        ratings.append(rating)
    return ratings


def getViews(lista):
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






def main():

    print('ejercicio 1 - 6')
    print('ejercicio 1', getRatings())
    print('ejercio 2', getViews([4, 0, 3.5, 5, 5, 0]))
    print('ejercio 3', getIndNoViews([4, 0, 3.5, 5, 5, 0]))
    print('ejercio 4', getIndViews([4 , 0, 3.5, 5, 5, 0]))
    print('ejercio 5')
    baseP = [[4.5, 4, 4, 5, 4.5, 5], [3, 4.5, 3.5, 2, 5, 3], [5, 4.5, 4.5, 4.5, 5, 4], [4, 4.5, 4.5, 3, 5, 3.5]]
    baseP_df = pd.DataFrame(baseP, columns = movies)
    print(getNewBase(baseP_df,[1,5]))

main()