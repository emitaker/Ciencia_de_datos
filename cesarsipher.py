abecedario='abcdefghijklmnopqrstuvwxyz'

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
    pass

def crack1(fraEncr):
    pass

def crack2(fraEncr, letra):
    pass

def main():
    print("primer funcion(let2int): ",let2int("d"))
    print('segunda funcion (int2let), prueba rara: ',int2let(54))
    print('segunda funcion (int2let), prueba rara neg: ',int2let(-484))
    print('segunda funcion (int2let), prueba normal: ',int2let(4))
    print('tercera funcion (shift)', shift(4, 'a'))
    print('cuarta funcion (encode)',encode(554,'PoRK No T GUSto bb cHAle'))

main()