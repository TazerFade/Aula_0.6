i=0
soma=0
nums = int(input("Informe o número de alunos na sala: "))

while i<nums:
    nt = int(input("Informe sua nota: "))
    soma +=nt
    i+=1
media = soma /nums
print(f" A média final da turma foi :{media}")