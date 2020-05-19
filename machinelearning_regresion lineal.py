import pandas as pd
from sklearn import datasets
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error

boston=datasets.load_boston()

print('boston',type(boston),'\n')

print('boston keys',boston.keys(),'\n') #esto es para poder ver las llaves

print('boston.data & target',type(boston.data),type(boston.target),'\n')

print('boston data shape',boston.data.shape,'\n')

print(boston.DESCR,'\n') #muestra un resumen de la base de datos

x=boston.data
y=boston.target
print(x[:5])
df = pd.DataFrame(x, columns = boston.feature_names)
df.head()
print('x',type(x),'\n')
print('df',type(df),'\n')
print('y',type(y),'\n')


x_rooms = x[:,5]
df_rooms = df[['RM']]
print('x_rooms',type(x_rooms),'\n')
print('df_rooms',type(df_rooms),'\n')


print('x rooms shape',x_rooms.shape,'\n')
print('df rooms shape',df_rooms.shape,'\n')
print('y shape',y.shape,'\n')

plt.scatter(x_rooms, y)
plt.title('panda numpy')
plt.scatter(df_rooms,y)
plt.xlabel('numero de cuartos')
plt.ylabel('costo en miles de dolares')
plt.show()



from sklearn.linear_model import LinearRegression


reg = LinearRegression()


x_rooms= x_rooms.reshape(-1,1)
y=y.reshape(-1,1)
print('x rooms shape',x_rooms.shape,'\n')
print('y shape',y.shape,'\n')

reg.fit(x_rooms,y)
reg.fit(df_rooms,y)

prediction_space = np.linspace(min(x_rooms),max(x_rooms))
print('len predic space',len(prediction_space))

y_pred=reg.predict(prediction_space)

plt.scatter(df_rooms,y)
plt.title('Sklearn linear regression')
plt.xlabel('numero de cuartos')
plt.ylabel('costo en miles de dolares')
plt.plot(prediction_space,y_pred,color='black',linewidth=3)
plt.show()



from sklearn.model_selection import train_test_split


X_train,X_test,y_train,y_test = train_test_split(x_rooms ,y ,test_size=0.10 ,random_state=42)

print(X_train.shape)
print(x_rooms.shape)

reg1 = LinearRegression()

reg1.fit(X_train,y_train)

y_pred1= reg.predict(X_test)

plt.scatter(X_train,y_train)
plt.title('Sklearn test')
plt.xlabel('numero de cuartos')
plt.ylabel('costo en miles de dolares')
plt.plot(X_test, y_pred1, color ='black', lineWidth = 3)
plt.show()

print(np.sqrt(mean_squared_error(y_test,y_pred1)),'\n')





#ejercicio 1


print('ejercicio 1 \n')
print('La que mas se parece a RM es LSTAT \n')





#ejercicio 2

print('ejercicio 2 \n')


from sklearn.linear_model import LinearRegression

reg2= LinearRegression()

x_ = x[:,12]
df_ = df[['LSTAT']]

x_= x_.reshape(-1,1)
y=y.reshape(-1,1)


reg2.fit(x_, y)

prediction_space2 = np.linspace(min(x_), max(x_))

y_pred2=reg2.predict(prediction_space2)

plt.scatter(df_,y)
plt.title('Sklearn linear regression')
plt.xlabel('% lower status of the population')
plt.ylabel('costo en miles de dolares')
plt.plot(prediction_space2,y_pred2,color='black',linewidth=3)
plt.show()



#ejercicio3

print('ejercicio 3 \n')

print(reg2.predict([[10]]))
print(reg2.predict([[8]]))
print(reg2.predict([[2]]),'\n')


#ejercicio 4

print('ejercicio 4 \n')


from sklearn.model_selection import train_test_split


X_train,X_test,y_train,y_test = train_test_split(x_ , y ,test_size=0.20 ,random_state=11)
reg_2 = LinearRegression()
reg_2.fit(X_train,y_train)
y_pred_2=reg_2.predict(X_test)
plt.scatter(X_train,y_train)
plt.plot(X_test,y_pred_2,color = 'black', lineWidth = 3)
plt.xlabel('% of lower status of the population')
plt.ylabel('costo en miles de dolares')
plt.show()

print(np.sqrt((mean_squared_error(y_test,y_pred_2))))
