n1 = int(input("Digite a sua primeira nota Avaliativa :"))
while n1<0 or n1>10:
    n1 = float(input("Nota inválida\nDigite novamente:"))

n2 = int(input("Digite a sua segunda nota Avaliativa :"))
while n2<0 or n2>10:
    n2 = float(input("Nota inválida\n Digite novamente:"))

media=(n1+n2)/2
print(f"Sua média final foi: {media}")
