import pandas as pd
import numpy as np

calificaciones=pd.read_csv("Calificaciones.csv")
calificaciones=pd.read_csv("Calificaciones.csv",index_col=0)
c=calificaciones.drop('E6',axis=0)
d=c.drop('Unnamed: 5',axis=1)

#parte 1
print("parte 1")
c=calificaciones.drop('E6',axis=0)
q1= c[['Quiz 1']]
print(q1,'\n')
q2= c[['Quiz 2']]
print(q2,'\n')
q3= c[['Quiz 3']]
print(q3,'\n')
q4= c[['Quiz 4']]
print(q4,'\n')
final= c[['Final']]
print(final,'\n')

#parte 2
print("parte 2")
print(np.mean(q1))

print(np.mean(q2))

print(np.mean(q3))

print(np.mean(q4))

print(np.mean(final),'\n')

#parte 3
print("parte 3")
e=d.iloc[8:19,[0,1,2,3,4]]
final_2=e[['Final']]
print(np.mean(final_2))