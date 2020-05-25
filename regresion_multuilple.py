import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import numpy as np

boston = datasets.load_boston()

X=pd.DataFrame(boston.data, columns=boston.feature_names)
y=pd.DataFrame(boston.target)
X.head()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.15, random_state=17)
print(X_train.shape,'\n')
regresor = LinearRegression()
regresor.fit(X_train, y_train)
print(regresor.score(X_test, y_test),'\n')

from sklearn.model_selection import cross_val_score

X_rooms = X[['RM']]
regresor1 = LinearRegression()
cv_results = cross_val_score(regresor1, X_rooms, y, cv=20)
print(cv_results,'\n')
print(np.mean(cv_results),'\n')


regresor2 = LinearRegression()
cv_results2 = cross_val_score(regresor2, X, y, cv=20)
print(cv_results2,'\n')
print(np.mean(cv_results2),'\n')


#ejercicio 1

'''Aqui se muestran los 5 primeros datos de la base de datos de diabetes'''

print('ejercicio 1','\n')

nombre_base_datos = datasets.load_diabetes()

# print(nombre_base_datos.DESCR,'\n')

X2 = pd.DataFrame(nombre_base_datos.data, columns = nombre_base_datos.feature_names)
y2 = pd.DataFrame(nombre_base_datos.target)
X2.head()

print(X2[:5])

#ejercicio 2

'''Aqui se muestran una regresion multiple con 4 caracteristicas'''

print('ejercicio 2','\n')

X2_1 = X2.iloc[:,[0, 1, 2, 3]]
X2_1.head()
regresor3= LinearRegression()

X2_train, X2_test, y2_train, y2_test = train_test_split(X2_1, y2, test_size=0.10, random_state=101)
regresor3.fit(X2_train , y2_train)
print(regresor3.score(X2_test, y2_test),'\n')

#ejercicio 3

print('ejercicio 3','\n')
for i in [3, 5, 10]:
    cv_results3 = cross_val_score(regresor3, X2_1, y2, cv = i)
    print(cv_results3)
    print(np.mean(cv_results3))
    print('\n')