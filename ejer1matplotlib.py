import matplotlib.pyplot as plt 
import numpy as np

x=range(-4,5)
np_x=np.array(x)
y=[]
for i in np_x:
  y.append(i**2-4)


x2=range(-4,5)
np_x2=np.array(x2)
y2=[]
for j in np_x2:
  y2.append(-j**2+4)



plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.title("Ejercicio 1")
plt.text(-2,0,"inter")
plt.text(2,0,"inter")
plt.plot(np_x,y,c="green")
plt.plot(np_x2,y2,c="red")
plt.xticks([-4,-2,0,2,4])
plt.yticks([-12,-8,-4,0,4,8,12])
plt.grid(True)
plt.show()
