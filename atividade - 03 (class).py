import os
from dataclasses import dataclass

os.system("cls|| clear")

@dataclass
class Usuario:
    nome: str
    sobrenome: str
    idade: int
    altura: float
    peso: float 

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

lista_usuarios = []

while True:
    lista_total = []
    usuario = Usuario(
    nome = input("Digite seu nome: "),
    sobrenome = input("Digite seu sobrenome: "),
    idade = int(input("Digite sua idade: ")),
    altura = float(input("Digite sua altura: ")),
    peso = float(input("Digite o seu peso:"))
        )
    lista_total.append(usuario)
    
    opcao = input("Você deseja sair ou deseja adicionar mais uma pessoa?: ")
    if opcao.lower() == "sair":
        break

lista_nome=[]
lista_sobrenome=[]
lista_idade = []
lista_altura = []
lista_peso = []

for pessoa in lista_total:
    lista_nome.append(pessoa.nome)
    lista_sobrenome.append(pessoa.sobrenome)
    lista_idade.append(pessoa.idade)
    lista_altura.append(pessoa.altura)
    lista_peso.append(pessoa.peso)
calculo = calculo_imc(lista_peso,lista_altura)
situacao_imc = resultado_imc(calculo)

# Exibindo os dados armazenados
logoSenai()
print("\n\033[35mDados dos usuários: \033[m")

for i,nome in enumerate(lista_nome):
    print(f"Nome: {nome} {lista_sobrenome[i]}")
    print(f"Idade: {lista_idade[i]}")
    print(f"Altura: {lista_altura[i]}")
    print(f"Peso: {lista_peso[i]}")
    print(f"Imc: {calculo[i]:.2f}")
    print(f"Situação: {situacao_imc[i]}")
    


    

    

