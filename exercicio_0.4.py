# las entradas de datos
v1 = int(input("Digite o primeiro valor: "))
v2 = int(input("Digite o segundo valor: "))

#La repetición numerica
while v2==0:
    print(" Por favor informe o valor novamente.")
    v2 = int(input("Digite o segundo valor: "))

# la divisíon numerica
rf = v1/v2

#la impresión de datos
print(f"Seu resultado final foi de:{rf}")