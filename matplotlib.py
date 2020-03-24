import matplotlib.pyplot as plt 

x=[1,2,3,4,5]
y=[10,20,30,40,50]

#es para que se vea como puntos
plt.scatter(x,y)
plt.show()

#es para que se vea como grafica
plt.plot(x,y)
plt.show()

#ejemplo 1
años = [1950, 1955, 1960, 1965, 1970, 1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020, 2025, 2030, 2035, 2040, 2045, 2050]
pob = [2.525, 2.758,3.018, 3.322, 3.682, 4.061, 4.440, 4.853, 5.310, 5.735, 6.127, 6.520, 6.930, 7.349, 7.795, 8.184, 8.549, 8.888, 9.199, 9.482, 9.735]
plt.plot(años,pob)
plt.xlabel("Años")
plt.ylabel("Poblacion miles de millones")
plt.title("Poblacion Mundial")
plt.show()

#ticks lol

plt.plot(años,pob)
plt.xlabel("Años")
plt.ylabel("Poblacion miles de millones")
plt.title("Poblacion Mundial")
plt.yticks([2,4,6,8,8,10])
plt.show()

#yticks con m
plt.plot(años,pob)
plt.xlabel("Años")
plt.ylabel("Poblacion")
plt.title("Poblacion Mundial")
plt.yticks([2,4,6,8,8,10],["2mM","4mM","6mM","8mM","10mM"])
plt.show()


#ejemplos de cambio de grosor y parametros en las graficas con scatter
import numpy as np
x=[1,2,3,4,5]
y=[10,20,30,40,50]
np_y=np.array(y)
#s es del tamaño de los puntos
#c color de los puntos
#alpha la opacidad de los puntos
plt.scatter(x,np_y,alpha=.4,s=20,c="black")


#ejemplo de cambio de puntos
x=range(10)
y=[16,1,32,64,128,4,2,256,8,512]
tamaño=[100,200,30,40,1200,60,70,800,90,100]
color=["red","red","blue","black","yellow","yellow","green","green"]
plt.scatter(x,y,s=tamaño,c=color,alpha= 0.6
plt.text(4,128,"punto 5")
plt.text(7,256,"punto 7")
plt.show()

#ejemplo grafica exponencial
x=range(70)
np_x=np.array(x)
np_x=np_x*.1
y=[]
for i in np_x:
    y.append(2**i)
plt.plot(np_x,y,c="black")
plt.grid(True)
plt.show()

