cal = "s"
while cal == "s":
    n1 = float(input("Digite a sua primeira nota Avaliativa :"))
    while n1 < 0 or n1 > 10:
        n1 = float(input("Nota inválida\nDigite novamente:"))

    n2 = float(input("Digite a sua segunda nota Avaliativa :"))
    while n2 < 0 or n2 > 10:
        n2 = float(input("Nota inválida\nDigite novamente:"))

    media = (n1 + n2) / 2
    print(f"Sua média final foi: {media:.2f}")
    cal = input("Deseja realizar outro cálculo? 'S' para sim, 'N' para não: ")
