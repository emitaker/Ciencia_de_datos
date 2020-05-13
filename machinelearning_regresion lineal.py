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
#print(x[:5])
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
plt.scatter(df_rooms,y)
plt.xlabel('numero de cuartos')
plt.ylabel('costo en miles de dolares')
plt.show


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
plt.xlabel('numero de cuartos')
plt.ylabel('costo en miles de dolares')
plt.plot(prediction_space,y_pred,color='black',linewidth=3)
plt.show

np.sqrt(mean_squared_error(x_rooms,y))