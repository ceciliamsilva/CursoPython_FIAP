# Declaração de variáveis e atribuições
nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))
doenca_infectocontag = input("Suspeita de doença infectocontagiosa?").upper()

# Comando de decisão sobre as variáveis criada
if idade >= 65:
    # Se a idade digitada for maior ou igual a 65 informa que tem atendimento prioritário
    print(nome + " possui atendimento prioritário.")
elif doenca_infectocontag == "SIM":
    # Comando elif de decisão encadeada. Se idade menor que 65 e suspeita de doenca infectocontagiosa, direcionada para sala
    print(nome + " deve ser direcionado para sala reservada.")
else:
    # Se a idade digitada for menor que 65 informa que não tem atendimento prioritário
    print(nome + " não possui atendimento prioritário.")