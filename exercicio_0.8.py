num = int(input("Informe um número: "))
for x in range(1,num+1):
    for y in range(1,x+1,1):
        print(x,end=" ")
    print()