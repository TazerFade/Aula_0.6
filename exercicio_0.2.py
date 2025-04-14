soma=0
x = 0
while x<5:
    nota = int(input("Digite sua nota: "))
    print(f"Meu lindo X ainda é {x}")
    x += 1
    soma += nota
media=soma/5

print(f"Sua média final foi: {media}")