from sklearn import datasets
import pandas as pd
import numpy as np

iris=datasets.load_iris()
iris.keys()


print(type(iris['target']),iris['target'].shape)
print(iris['feature_names'])
print(iris['target_names'])
X=iris['data']
df=pd.DataFrame(X)
df.head()
df=pd.DataFrame(X,columns=iris['feature_names'])
df.head()

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

knn=KNeighborsClassifier(n_neighbors=5)
y=pd.DataFrame(iris['target'])
knn.fit(df,y)
nuevos=np.array([[5.6,2.8,3.9,1.1],[4.77,3.21,1.3,.25]])
print(knn.predict(nuevos))
print(iris['target_names'])
X_train,X_test,y_train,y_test=train_test_split(df,y,test_size=0.2,random_state=123,stratify=y)
knn.fit(X_train,y_train)
print(knn.predict(X_test))
print(len(knn.predict(X_test)))
print(knn.score(X_test,y_test))

X_train,X_test,y_train,y_test=train_test_split(df,y,test_size=0.3,random_state=123,stratify=y)
knn.fit(X_train,y_train)
print(knn.predict(X_test))
print(len(knn.predict(X_test)))
print(knn.score(X_test,y_test))

X_train,X_test,y_train,y_test=train_test_split(df,y,test_size=0.1,random_state=123,stratify=y)
knn.fit(X_train,y_train)
print(knn.predict(X_test))
print(len(knn.predict(X_test)))
print(knn.score(X_test,y_test))

#ejercicio 1
df1=df.drop(0 and 149, axis=0)
y1=y.drop(0 and 149,axis=0)
knn.fit(df1,y1)
new=np.array([[5.7,2.6,3.8,1.3]])
print('ejercicio 1',knn.predict(new))
print('ejercicio 1',knn.score(df1,y1))

#ejercicio 2
Xx_train,Xx_test,yy_train,yy_test=train_test_split(df1,y1,test_size=0.1,stratify=y1)
knn.fit(Xx_train,yy_train)
print('ejercicio 2',knn.predict(Xx_test))
print('ejercicio 2',len(knn.predict(Xx_test)))
print('ejercicio 2',knn.score(Xx_test,yy_test))
