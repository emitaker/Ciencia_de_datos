
##### Clase 9: Numpy #####

# En esta clase introduciremos una biblioteca que es de mucha utilidad en en análisis de estructuras de datos en general, y en Ciencia de Datos en particular. Sus ventajas serán claras conforme vayamos analizando sus funciones y tipos específicos.  

# La biblioteca de la que hablamos es 'Numpy' o, 'Numerical Python'. Como ya sabemos, para poder usarla usamos la siguiente instrucción

import numpy as np  


# Uno de los tipos de datos que serán más importantes para nosotros es el tipo 'array', específico de Numpy. Un 'arreglo', es simplemente una colección de datos. Es idéntico a una lista en forma, pero muuuuuuy diferente en funcionalidad.

# Para crear un arreglo en Python, usamos la función 'array' de numpy. Esta función acepta una lista como parámetro y regresa un arreglo con exactamente los mismos elementos de la lista

# lista1 = [1,2,3,4,5]
# arreglo1 = np.array(lista1)
# print(lista1)
# print(arreglo1)  

# Note la diferencia a la hora de imprimir el arreglo y a la hora de simplemente pedir su valor.
# Podemos checar el tipo de ar1

#print(type(arreglo1))

# ¿Cuáles son las ventajas del arreglo sobre la lista? Bueno, dado que el arreglo es un nuevo tipo de dato, todo objeto del tipo array tiene sus propias funciones específicas. Por ejemplo

alturas = [1.57, 1.77, 1.80, 1.85, 1.78]
pesos = [65, 68, 95, 104, 72]

ar_alturas = np.array(alturas)
ar_pesos = np.array(pesos)

#imc_listas = pesos / alturas**2
imc = ar_pesos / ar_alturas**2
#print(imc)


# Es decir, los arreglos están diseñados para soportar operaciones término a término, mientras que las listas no. Aunque es posible calcular el índice de masa corporal usando listas y ciclos for, es obvio que es preferible usar arreglos para mejorar el desempeño del algoritmo.

# Otra de las diferencias entre arreglos y listas es que los arreglos permiten un sólo tipo de de dato

lista2 = [0, True, "rojo"]
arreglo2 = np.array(lista2)

#print(lista2)
#print(arreglo2) 

# (de hecho, una de las razones por las cuales las operaciones con arreglos están tan optimizadas, es porque sólo contienen un tipo de dato)


# Por otro lado, al ser un arreglo un tipo de dato nuevo, éste tiene su propia funcionalidad. Es decir, sus propios métodos específicos, que pueden ser muy diferentes a los de otros tipos de datos

# print(alturas)
# print(pesos)
# print(alturas + pesos)

# print("\n")

# print(ar_alturas)
# print(ar_pesos)
# print(ar_alturas + ar_pesos)  


# Sin embargo, una de las cosas que funcionan exactamente igual es el indexing y el slicing

# print(imc[2:5])
# print(imc)
# print(imc[::-1])
# print(imc[-2])  


# Sin embargo, una de las funcionalidades increíbles propias del arreglo, es que se puede hacer slicing usando un arreglo de booleanos. 

# Por ejemplo, definamos el siguiente arreglo

mes_nac = [11, 11, 7, 2, 5, 11]
ar_mes_nac = np.array(mes_nac)

# Imaginemos que queremos saber quíenes nacieron en la segunda mitad del año. Los primero que debemos hacer es crear un arreglo de booleanos

ar_cond = ar_mes_nac > 6
#print(ar_cond)  


# Luego pasamos este arreglo de booleanos como slicing al arreglo original


# Esta instrucción emparejará los elementos de ambos arreglos 'ar_mes_nac' y 'ar_cond' y creará un nuevo arreglo sólo con los elementos que tengan emparejado un True

#print(ar_mes_nac[ar_cond])


# Analicemos otro ejemplo. Imaginemos que queremos crear un arreglo con los múltiplos de 7 que están entre 0 y 100. ¿Cómo lo haría?, ¿ciclo for? Pretty sure! Pero es más rápido usando arreglos

arreglo3 = np.array(range(100))

print(arreglo3[arreglo3 % 7 == 0])


# Ejercicio 1: A continuación se presentan los pesos en libras de 10 estudiantes de la UCLA (stat.ucla.edu) en una lista. Construya un arreglo con estos datos llamado 'np_pesos_lb'. Luego convierta estos pesos en kilogramos y guarde los resultados en un arreglo llamado 'np_pesos_kg'. Imprima ambos arreglos en pantalla junto con su tipo.

pesos_lb = [112.99,
136.49,
153.03,
142.34,
144.30,
123.30,
141.49,
136.46,
112.37,
120.67]


# Ejercicio 2: A continuación se presentan las alturas en pulgadas de 10 estudidantes de la UCLA. Construya un arreglo llamado 'np_alturas_in' con estos datos, luego convierta estas alturas a metros y guarde los resultados en un arreglo llamado 'np_alturas_m'. Finalmente construya un arreglo llamado 'imc_uni' con los índices de masa corporal de los estudiantes

alturas_in =[65.78,     
71.52,
69.40,
68.22,
67.79,
68.70,
69.80,
70.01,
67.90,
66.78]


# Ejercicio 3: La universidad se preocupa por la salud de sus estudiantes. Así que le pide un registro de los estudiantes con posibles problemas de peso. Construya un arreglo de booleanos llamado 'over' que contenga 'True' si el imc correspondiente es mayor a 21 y 'False' de lo contrario. Usando 'over' filtre los elementos de 'imc_uni' para obtener un nuevo arreglo llamado 'alum_over' que contenga los imc's mayores a 21 e imprímalo en pantalla.

# Ejercicio 4: Por último, sólo para cerciorarnos de que funciona, haga un slicing normal en 'imc', imprimiendo los datos que van del índice 3 al índice 8 incluyéndolo.


# Ejercicio 5: La universidad se acaba de dar cuenta que un índice de masa corporal muy bajo también puede ser un síntoma de problemas alimenticios, por tanto le pide un nuevo registro con los estudiantes que tengan un imc por debajo de 19. Construya un arreglo de booleanos llamado 'under' similar al ejerciccio anterior y úselo para filtrar los elementos de 'imc_uni' por debajo de 19 y guarde los datos en un nuevo arreglo llamado 'alum_under'. Imprímalo en pantalla.True


# Ejercicio 6: Finalmente imprima los imc's de los alumnos sin problemas de imc. Es decir, imprima los imc entre 20 y 23. ¿Tiene algún problema para resolver este ejercicio?. ¿Se le ocurre alguna manera usando operadores lógicos?
















# Soluciones:


np_pesos_lb = np.array(pesos_lb)
np_alturas_in = np.array(alturas_in)

np_pesos_kg = np_pesos_lb * 0.454
np_alturas_m = np_alturas_in * 0.0254

imc = np_pesos_kg / np_alturas_m**2