from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import  train_test_split
import random as rd
import numpy as np

knn=KNeighborsClassifier(n_neighbors=10)

#algortimos permitidos para machine learning: numpy array, pandas dataframe

rd.seed(777)
colores=[]
puntos=[]
for k in range(500):
    puntos.append([rd.randint(1,100), rd.randint(1,100),rd.randint(1,100)])
    colores.append(rd.choice(['amarillo','azul','rojo']))
np_col=np.array(colores)
np_pun=np.array(puntos)

knn.fit(np_pun, np_col)

print(np_pun.shape,np_col.shape)

new=np.array([[11,80,77]])
prediccion=knn.predict(new)

print(prediccion)

X_train,X_test,y_train,y_test=train_test_split(np_pun,np_col,test_size=0.2, random_state=23,stratify=np_col)
knn1=KNeighborsClassifier(n_neighbors=5)
knn1.fit(X_train, y_train)
predicciones=knn1.predict(X_test)
print(predicciones)
print(knn1.score(X_test, y_test))