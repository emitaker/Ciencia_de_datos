def moda(a):
    count=0
    modas = []
    for x in a:
        count_x = a.count(x)
        if count_x > count:
            count = count_x

    #cuando hay mas modas
    for y in a:
        count_y = a.count(y)
        if count_y == count and y not in modas:
            modas.append(y)
    return modas

def main():
    a=[1,2,3,4,5,6,7,8,9,10,1,2,3,1,3]
    print(moda(a))

main()
