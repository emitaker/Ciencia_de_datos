#Histogramas junto con diccionarios
import matplotlib.pyplot as plt

z=[2,2,3,5,7,6,5,7,2,4,10,9,9,7,1,1,3,8,10,8,5,2,3,4]

plt.hist(z)
plt.show

#para cambiar el color
plt.hist(z, bins = 5,color='red')
plt.show()

#para ponerlo de manera horizontal
plt.hist(z,color='green',bins=7,orientation='horizontal')
plt.show()

#con ticks
plt.hist(z,color='yellow')
plt.xlabel('Eje x')
plt.ylabel('Cantidad')
plt.title('Histograma de prueba')
plt.xticks([2,4,6,8])
plt.grid(True)
plt.show()
