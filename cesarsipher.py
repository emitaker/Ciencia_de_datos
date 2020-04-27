#Emilio Campuzano Mejia A01378948
import matplotlib.pyplot as plt

"""
Programa que desencripta el método de cesar

Lista que se ocupo para comparar los datos
A 	12,53%
B 	1,42%
C 	4,68%
D 	5,86%
E 	13,68%
F 	0,69%
G 	1,01%
H 	0,70%
I 	6,25%
J 	0,44%
K 	0,02%
L 	4,97%
M 	3,15%
N 	6,71%
O 	8,68%
P 	2,51%
Q 	0,88%
R 	6,87%
S 	7,98%
T 	4,63%
U 	3,93%
V 	0,90%
W 	0,01%
X 	0,22%
Y 	0,90%
Z 	0,52%

"""

abecedario='abcdefghijklmnopqrstuvwxyz'
porcentajeLetras=[12.53, 1.42, 4.68, 5.86, 13.68, 0.69, 1.01, 0.70, 6.25, 0.44, 0.02, 4.97, 3.15, 6.71, 8.68, 2.51, 0.88, 6.87, 7.98, 4.63, 3.93, 0.90, 0.01, 0.22, 0.90, 0.52]

def let2int(letra):
    return abecedario.index(letra)

def int2let(numero):
    return abecedario[numero%26]

def shift(n,c):
    return int2let(let2int(c)+n)

def encode(n,frase):
    frase=frase.lower()
    y=''
    for x in frase:
        if x in abecedario:
            y+=(shift(n, x))
        elif x == ' ':
            y+=' '
    return y

def getKey(frase):
    frasee=frase.lower()
    rep=0
    for x in frasee:
        if x in abecedario:
            n=frasee.count(x)
        if n > rep:
            rep=n
            letra=x
    key=abecedario.index(letra)
    return(key)

def crack1(fraEncr):
    x=getKey(fraEncr)
    key= x-abecedario.index('e')
    return encode(-key,fraEncr)

def crack2(fraEncr, letra):
    x=getKey(fraEncr)
    key= x - abecedario.index(letra)
    return encode(-key,fraEncr)

def frq_table(texto):

    lowercase = texto.lower()
    texto = texto.lower()
    stats = [0] * len(abecedario)
    length = 0
    for t in texto:
        if t in abecedario:
            stats[let2int(t)] += 1
            length += 1
    for p in abecedario:
        stats[let2int(p)] = (stats[let2int(p)] * 100) / length
    return stats

def chsqr(lista1, lista2):
    #lista 1 es la esperada
    #lista 2 es la observada
    length = len(lista1)
    e = [0] * length
    for i in range(length):
        if(lista1[i] != 0):
            e[i] = (lista2[i] - lista1[i]) ** 2
            e[i] = e[i] / lista1[i]
        else:
            e[i] = 0
    return sum(e) # |R

def crack(frase):
    deks = []
    for l in abecedario:
        deks.append(crack2(frase, l))
    expected_frq = porcentajeLetras
    lowest = deks[0]
    for d in deks:
        if chsqr(expected_frq, frq_table(d)) < chsqr(expected_frq, frq_table(lowest)):
            lowest = d
    return lowest

def main():
    print("primer funcion(let2int): ",let2int("d"),'\n')
    print('segunda funcion (int2let), prueba rara: ',int2let(54),'\n')
    print('segunda funcion (int2let), prueba rara neg: ',int2let(-484),'\n')
    print('segunda funcion (int2let), prueba normal: ',int2let(4),'\n')
    print('tercera funcion (shift)', shift(4, 'a'),'\n')
    print('cuarta funcion (encode)',encode(554,'PoRK No T GUSto bb cHAle'),'\n')
    print('quinta funcion (getkey)', getKey('asdffffaafffffffffsfsaaaae'),'\n')
    print('sexta funcion (crack 1)', crack1('bcqbc cqc bgy, lm fc nmbgbm bchyp bc nclqyp cl rg.'),'\n')
    print('sexta funcion (crack 1)', crack1('nbcxb yujlnanb erxunwcxb, crnwnw orwjunb erxunwcxb'),'\n')
    print('sexta funcion (crack 1)', crack1('h nu ldnaex wdwlj nvyanwmrx nu ednux. jdw brpdn yxbjmx nw nu kdbcx mn yjujb, bxkan nu mrwcnu mn vr ydnacj. h h bdb xsxb crnwnw uj jyjarnwlrj mn uxb mn dw mnvxwrx zdn nbcj mdavrnwmx... h vr juvj, mn nbj bxvkaj, wx yxmaj urkajabn ¡wdwlj vjb!'),'\n')
    print('sexta funcion (crack 1)', crack1('e iwxi tews, egefeviqsw legmirhs ps uyi tsheqsw, rs ps uyi eqeqsw'),'\n')
    print('septima funcion (crack 2)', crack2('e iwxi tews, egefeviqsw legmirhs ps uyi tsheqsw, rs ps uyi eqeqsw','a'),'\n')

    print('ejercicio 9',frq_table('hola, aa'),'\n')

    print('ejercicio 10',chsqr(porcentajeLetras, frq_table("hola, aa")),'\n')

    frase1='bcqbc cqc bgy, lm fc nmbgbm bchyp bc nclqyp cl rg.'
    print('ejecicio 11',crack(frase1),'\n')
    f1=frq_table(crack(frase1))
    plt.hist(f1,bins=27)
    plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27],abecedario)
    plt.show()

    frase2='nbcxb yujlnanb erxunwcxb, crnwnw orwjunb erxunwcxb'
    print('ejecicio 11',crack(frase2),'\n')
    f2=frq_table(crack(frase2))
    plt.hist(f2,bins=27)
    plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27],abecedario)
    plt.show()

    frase3='h nu ldnaex wdwlj nvyanwmrx nu ednux. jdw brpdn yxbjmx nw nu kdbcx mn yjujb, bxkan nu mrwcnu mn vr ydnacj. h h bdb xsxb crnwnw uj jyjarnwlrj mn uxb mn dw mnvxwrx zdn nbcj mdavrnwmx... h vr juvj, mn nbj bxvkaj, wx yxmaj urkajabn ¡wdwlj vjb!'
    print('ejecicio 11',crack(frase3),'\n')
    f3=frq_table(crack(frase3))
    plt.hist(f3,bins=27)
    plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27],abecedario)
    plt.show()


    frase4='e iwxi tews, egefeviqsw legmirhs ps uyi tsheqsw, rs ps uyi eqeqsw'
    print('ejecicio 11',crack(frase4),'\n')
    f4=frq_table(crack(frase4))
    plt.hist(f4,bins=27)
    plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27],abecedario)
    plt.show()


    frase5='gewxmke, ibleywxs, ip tswxi xswgs c wigs. c ewikyve, mrjeywxs, uyi le zmwxs psw iwtigxvsw.'
    print('ejecicio 11',crack(frase5),'\n')
    f5=frq_table(crack(frase5))
    plt.hist(f5,bins=27)
    plt.xticks([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27],abecedario)
    plt.show()


main()
