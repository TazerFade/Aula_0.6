senha="123456"
n=1
resposta ="Execesso de tentativas, login bloqueado."
user = input(" Digite o nome do usuário: ")
while n<=3:
    s2 = int(input("Informe sua senha: "))
    if s2==senha:
        resposta=" login realizado com sucesso"
        break
    n+=1
print(resposta)