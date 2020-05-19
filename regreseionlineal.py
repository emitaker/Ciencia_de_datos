

import pandas as pd
from sklearn import datasets
import numpy as np 
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error

# Importamos una base de datos precargada en Scikitlearn y la guardamos con el nombre de 'boston'. Note el tipo de 'boston'.


boston = datasets.load_boston()
type(boston)

# El tipo 'Bunch' es parecido a un diccionario en el sentido de que tiene etiquetas y valores.

print(boston.keys())

#Sin embargo, las etiquetas son más complejas que en un diccionario. Por ejemplo, la etiqueta 'data' tiene TODOS los datos de la base de datos, con excepción de la última columna, que corresponde a la etiquta 'target'. Pues Scikitlearn ya da un formato previo a la estructura de datos teniendo en mente que se analizará con métodos estadísticos.

type(boston.data), type(boston.target)

#Estos tipos de datos son convenientes como ya sabemos.

#También podemos saber con cuántos datos contamos con el atributo 'shape'.

boston.data.shape

#También podemos ver las primeras 5 observaciones de la base de datos.

print(boston.DESCR)

#Aunque la base de datos ya tiene algo de formato previo, para poder usar todas las funcionalidades hasta ahora vistas, tenemos que extraer el contenido de nuestra base de datos y convertirlo en un tipo de dato que podamos manejar con familiaridad.


#X = boston['data']
X = boston.data
y = boston.target
print(X[:5])
df = pd.DataFrame(X, columns = boston.feature_names)
df.head()
print(type(X))
print(type(df))

#Como siempre, hagamos un análisis exploratorio de los datos antes de empezar a hacer ML.

print(boston.DESCR)

#En esta clase realizaremos regresión lineal simple, dejando la regresión múltiple (igual de sencilla) para la siguiente clase. Por tanto, necesitamos analizar un sólo atributo o característica de todas las que arroja la base de datos. Hagámoslo con el número de cuartos RM. Es decir, de todo el DataFrame 'df', extraigamos sólamente la columna 'RM'.

X_rooms = X[:,5]
df_rooms = df[['RM']]
print(type(X_rooms))
print(type(df_rooms))
print(type(y))

#Sin embargo, note cuál es el tamaño de 'df_rooms' declarada de esta manera. Después volveremos a esto para arreglarlo.

print(X_rooms.shape)
print(df_rooms.shape)
print(y.shape)

#Intentemos ver si es viable tratar este problema como un problema de regresión lineal. Recuerde que para hacer esto, necesitamos ver los datos en una gráfica (a menos que sepa lo que es el coeficiente de correlación de Pearson).

plt.scatter(X_rooms,y)
#plt.scatter(df_rooms,y)
plt.xlabel("Número de cuartos")
plt.ylabel("Costo en miles de dólares")
plt.show()

#Con esta gráfica, queda claro que hay una fuerte correlación entre la cantidad de cuartos de una casa y su precio en la ciudad de Boston. Más aún, parece que la relación puede ser modelada de manera lineal.

#Hace unos minutos vimos cuál es el funcionamiento de la Regresión lineal simple, vimos que se trata de obtener una línea recta y = ax + b que mejor se ajuste a los datos observados, mediante un método llamado "mínimos cuadrados" que minimiza el cuadrado de la distancia entre las predicciones de la línea recta, y los datos reales. Bueno, Scikitlearn hace todo esto y más de una manera directa.

#Primero importamos el método de regresión lineal de Scikitlearn y lo instanciamos con el nombre 'reg'

from sklearn.linear_model import LinearRegression
reg = LinearRegression()

#Ahora aplicamos la regresión para que "ajuste" los datos dados

reg.fit(X_rooms, y)
print(X_rooms.shape)
print(y.shape)
help(reg.fit)

#Note lo mencionado anteriormente. Debemos poner los datos en el formato correcto para que Scikitlearn los pueda manipular. En este caso, debemos usar la función 'reshape' para que nuestros arreglos tengan la dimensión correcta.

X_rooms = X_rooms.reshape(-1, 1)
y = y.reshape(-1, 1)
print(X_rooms.shape)
print(y.shape)

#Lo intentamos de nuevo


reg.fit(X_rooms, y)
reg.fit(df_rooms, y)

#Acabamos de realizar nuestra primera regresión lineal con Scikitlearn. Sin embargo, no visualizamos nada. Para poder analizar nuestra regresión, pongámosla a prueba. Lo haremos de dos maneras: una visual y otra usando alguna métrica predefinida.

#Primero definamos un "espacio de prueba" que simplemente será un arreglo de datos que pasaremos a nuestro modelo. Elegimos exactamente el rango de valores que están presentes en nuestros datos experimentales.

prediction_space = np.linspace(min(X_rooms), max(X_rooms))
print(prediction_space)
len(prediction_space)

#Ahora obtenemos los valores que nuestro modelo predice usando el espacio de prueba

y_pred = reg.predict(prediction_space)

#Ahora grafiquemos los resultados obtenidos y comparémoslos con los datos experimentales.

plt.scatter(df_rooms, y)
plt.xlabel("Número de cuartos")
plt.ylabel("Costo en miles de dólares")
plt.plot(prediction_space, y_pred, color = 'black', linewidth = 3)
plt.show()

#Por último, Scikitlearn incluso nos da información sobre qué tan bien se ajusta el modelo lineal a los datos. Para esto, también podemos usar el método 'score' como lo hicimos en kNN.

reg.score(y, y_pred)
reg.predict([[20]])

print(min(X_rooms))
print(help(mean_squared_error))
plt.plot(X,y)

#Amazing!!!