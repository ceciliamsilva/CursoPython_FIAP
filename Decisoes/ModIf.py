# Declaração de variáveis e atribuições
nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))

# Comando de decisão sobre a variável criada
if idade >= 65:
    # Se a idade digitada for maior ou igual a 65 informa que tem atendimento prioritário
    print(nome + " possui atendimento prioritário.")
else:
    # Se a idade digitada for menor que 65 informa que não tem atendimento prioritário
    print(nome + " não possui atendimento prioritário.")