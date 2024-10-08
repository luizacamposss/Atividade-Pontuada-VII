import os

os.system("cls|| clear")

# Função sem retorno.
def logoSenai():
    os.system("cls || clear")
    print("\033[35m=== SENAI === \033[m")

# Calculando imc 
def calculo_imc(b:float, a:float):
    imc_list = []    
    for i,peso in enumerate(b):
        imc = peso / (a[i]*a[i])
        imc_list.append(imc)
    return imc_list


# Resultados do IMC
def resultado_imc(a):
    lista_grau_imc = []
    for imc in a:
        if imc < 18.5:
            lista_grau_imc.append("Você está abaixo do peso.") 
        elif imc <= 18.5 and imc < 25:
            lista_grau_imc.append("Você está com um peso normal.") 
        elif imc <= 25 and imc < 30:
            lista_grau_imc.append("Você está com sobrepeso.") 
        elif imc <= 30 and imc < 35:
            lista_grau_imc.append("Você está com uma obesidade grau I.") 
        elif imc < 35 and imc < 40:
            lista_grau_imc.append("Você está com uma obesidade grau II.") 
        elif imc > 40:
            lista_grau_imc.append("Você está com uma obesidade grau III (mórbida).")
    return lista_grau_imc

# Definindo listas vazias para armazenar os dados dos usuários
nomes = []
idades = []
alturas = []
pesos = []

# Solicitando os dados dos usuários em um loop
while True:
    logoSenai()
    nome = input("\033[34mDigite o nome do usuário (ou digite 'sair' para encerrar): ")

    if nome.lower() == 'sair':
        break
    

    idade = int(input("Digite a idade do usuário: "))
    altura = float(input("Digite a altura do usuário (em metros): "))
    peso = float(input("Digite o peso do usuário (em quilogramas):  \033[m"))


    # Adicionando os dados às listas
    nomes.append(nome)
    idades.append(idade)
    alturas.append(altura)
    pesos.append(peso)

calculo = calculo_imc(pesos,alturas)
situacao_imc = resultado_imc(calculo)

# Exibindo os dados armazenados
logoSenai()
print("\n\033[35mDados dos usuários: \033[m")
for i,a in enumerate(situacao_imc):
    print("="*40)
    print(f"\033[34mImc: {calculo[i]:.2f}")
    print(f"A sua situação: {a}")
    print("Nome:", nomes[i])
    print("Idade:", idades[i])
    print("Altura:", alturas[i], "metros")
    print("Peso:", pesos[i], "quilogramas \033[m")

