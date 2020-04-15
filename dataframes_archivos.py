import pandas as pd

a=calificaciones=pd.read_csv("Calificaciones.csv")
print(a,'\n')
b=calificaciones=pd.read_csv("Calificaciones.csv",index_col=0)
print(b,'\n')
c=calificaciones.drop('E6',axis=0)
print(c,'\n')
d=c.drop('Unnamed: 5',axis=1)
print(d)
