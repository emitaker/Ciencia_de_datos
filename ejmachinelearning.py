def dist(list1,list2):
    cont=0
    for x in range(len(list1)):
        cont+=(list1[x]-list2[x])**2
    ans= cont**(.5)
    return ans

def getCoor(lista):
    return lista[:-1]

def putInd(lista):
    indice=[]
    for x in lista:
         indice.append([x, lista.index(x)])
    return indice

def getNearColors(lista1,lista2):
    pass

def main():
    print(dist([0,0,0],[1,1,1]),'\n')
    print(getCoor([1,2,3,'cafe']),'\n')
    print(putInd([1,2,3,1,'kk']),'\n')
    print(getNearColors(1,1))
main()
