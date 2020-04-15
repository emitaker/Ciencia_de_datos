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

main()
