#actividad histogramas 
import matplotlib.pyplot as plt

abecedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ','o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ]
lista=[]

def cuenta(x):
    for i in abecedario:
        n=x.count(i)
        lista.append(n)
    return lista

frase=cuenta('He visto cosas que ustedes los humanos ni siquira podrían imaginar naves de asalto estallar en el cinturon de orion rayos c brillar mas alla de las puertas de tarkhauser todas estas cosas se perderan como lagrimas bajo la lluvia hora de morir')

plt.hist(frase,bins=27,color='green')
plt.title('Frecuencia de letras en español')
plt.xlabel('Letras del abecedario')
plt.ylabel('Porcentaje')
plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27],abecedario)
plt.show()

