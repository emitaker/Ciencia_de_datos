from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

digits=datasets.load_digits()


print(digits.keys())
print(digits['DESCR'],'\n')
print(digits.target_names,'\n')


#ejercicio 1
print('Ejercio 1','\n')
print(type(digits.target))
print(digits.target.shape)
print(digits.target[0:20],'\n')

#ejercicio 2
print('Ejercio 2','\n')
print(type(digits.data))
print(digits.data.shape,'\n')
print(digits.data[0],'\n')
print('\n\n\n')
print(digits.data[0:3],'\n')


#ejercicio 3
print('Ejercio 3','\n')
print(type(digits.images))
print(digits['images'].shape,'\n')
print(digits.images[0],'\n')
print(len(digits.images[0]))
print(type(digits.images[0]))
print(digits.images[0].shape,'\n')

print(digits.images[0],'\n')
plt.imshow(digits.images[0],cmap=plt.cm.gray_r)
plt.show

#ejercicio 4
x=digits.data
y=digits.target

clasificador=KNeighborsClassifier(n_neighbors=7)
clasificador.fit(x,y)

#ejercicio 5
print('Ejercio 5','\n')
X_train,X_test,y_train,y_test=train_test_split(x,y,test_size=0.15,random_state=31,stratify=y)
clasificador.fit(X_train,y_train)
print(clasificador.predict(X_test))
print(clasificador.score(X_test,y_test),'\n')

#ejercicio 6
print('Ejercio 6','\n')
print(clasificador.predict([X_test[0]]),'\n')


#ejercicio 7
print('Ejercio 7','\n')
print(X_test[0])
ar=np.reshape(X_test[0],(8,8))
print(y_test[7])
plt.imshow(ar,cmap=plt.cm.gray_r)
plt.show




