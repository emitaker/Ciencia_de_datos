l = [ 1, 10, 4, 2, 4, 3, 3, 1, 1, 3,1]

# moda
repeticiones = 0
for i in l:
    apariciones = l.count(i)
    if apariciones > repeticiones:
        repeticiones = apariciones

modas = []
for i in l:
    apariciones = l.count(i)
    if apariciones == repeticiones and i not in modas:
        modas.append(i)

print ("moda:", modas)
