import numpy as np

"""
Numpy funciona con arrays, y esto solo permite un tipo de dato
"""


alturas = [1.57,1.77,1.80,1.85,1.78]
pesos = [65,68,95,104,72]

array_alt=np.array(alturas)
array_w=np.array(pesos)

imc=array_w/(array_alt)**2
print("ejemplo de imc\n",imc,"\n")

#otro ejemplo
arraylol=np.array(range(100))
print("ejemplo de multiplos de 7 hasta 100\n",arraylol[arraylol % 7==0],"\n")

#ejercicio
print("ejercicio 1")
pesos_lb = [112.99, 136.49, 153.03, 142.34, 144.30, 123.30, 141.49, 136.46, 112.37, 120.67]

w=np.array(pesos_lb)
print("pesos(en libras)\n",w*.454,"\n")

alturas_in =[65.78, 71.52, 69.40, 68.22, 67.79, 68.70, 69.80, 70.01, 67.90, 66.78]
h=np.array(alturas_in)
print("alturas(en inches)\n",h*.0254,"\n")
print("El indice de masa corporala es: ",array_w/(array_alt)**2,"\n")

print("ejercicio 2")
over=np.array(array_w/(array_alt)**2)
print(over>21)
 
    