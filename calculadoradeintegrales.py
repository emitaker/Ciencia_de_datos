n=int(input("rectangulos: "))
sum=0

for i in range (n):
    area_irect=(1/n)*(i/n)**2
    sum = sum+area_irect
print(sum)
