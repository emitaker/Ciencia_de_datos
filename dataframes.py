import pandas as pd

nombres = ['Poe', 'Lovecraft', 'García Márquez', 'Zafón', 'King', 'Asimov','Quiroga', 'Clarke', 'Tolkien', 'Dick'] 
novelas = ['El Silencio', 'Dagón', 'Cien años de Soledad', 'La sombra del viento', 'Eso', 'Yo Robot','Cuentos de Locura', '2001 una odisea espacial', 'El Señor de los Anillos', 'Ubik'] 
año = [1849, 1937, 2014, "--", "--", 1992, 1937, 2008, 1973, 1982] 
generos = ['terror', 'terror', 'realismo mágico', 'realismo mágico', 'terror', 'ciencia ficción', 'terror', 'ciencia ficción', 'fantasía', 'ciencia ficción'] 
autores = {'nombre': nombres, 'libro': novelas, 'muerte' : año, 'género': generos}

pd_autores = pd.DataFrame(autores)

print(pd_autores,"\n")

pd_autores.index= ['EAP' , 'HPL', 'GM','CRZ','SK','IA','HdQ','ACC','JRR','PKD']
print(pd_autores,"\n")

z=pd_autores.loc[['EAP','JRR','PKD'],['libro','género']]
print(z,"\n")

a=pd_autores.loc[:,['nombre','género']]
print(a,"\n")

b=pd_autores.iloc[[5,3],[3,0]]
print(b,"\n")

c=pd_autores.iloc[[5,3]]
print(c,"\n")

d=pd_autores.iloc[:,[1]]
print(d,"\n")

e=pd_autores.iloc[0:8:2,[1]]
print(e,"\n")

# a partir de aqui poner en la terminal esto
type(pd_autores)

pd_autores
#esto es para las columnas
pd_autores[['libro']]
pd_autores[['libro','género']]

#uso de  (esto es para los renglones)
pd_autores[1:5]
pd_autores[1:2]
pd_autores[['muerte','nombre'][1:2]]