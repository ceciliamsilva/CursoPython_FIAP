# Criando um Inventário com listas dentro de listas

# Declaração de variável do tipo lista
inventario = []

# Inicializa variável resposta com valor "S" para que ocorra o primeiro preenchimento da lista
resposta = "S"

# Enquanto resposta for S, cria uma variável equipamento do tipo lista, que vai ser incluída na lista inventario
while resposta == "S":

    equipamento = [
        input("Equipamento: "),
        float(input("Valor: ")),
        int(input("Numero Serial: ")),
        input("Departamento: ")
                ]

    # Adiciona na lista invetario os itens da lista equipamento
    inventario.append(equipamento)

    resposta = input("\nDigite \"S\" para continuar: ").upper() # A contrabarra precedendo as "" indica que as "" serão impressas

# Imprime cada item da lista inventario contendo cada dado da lista equipamento, composta de 4 posições
for i in inventario:
    print("\nEquipamento: ", i[0])
    print("Valor: ", i[1])
    print("Serial: ", i[2])
    print("Departamento: ", i[3])

# Declaração de variável que vai receber o dado a ser buscado na lista
busca = input("\nDigite o nome do equipamento que deseja buscar: ")

for i in inventario:
    if busca == i[0]:
        print("Valor: ", i[1])
        print("Serial: ", i[2])
        print("Departamento: ", i[3])

# Declaração de variável que vai receber o dado (por equipamento) a ser modificado na lista
depreciacao = input("\nDigite o nome do equipamento que deseja alterar: ")

for i in inventario:
    if depreciacao == i[0]:
        print("Valor anterior: ", i[1])
        i[1] = i[1] * 0.9
        print("Valor atualizado: ", i[1])

# Declaração de variável que vai receber o dado (por numero de serie) a ser removido da lista
# É importante converter para int porque na lista equipamentos o serial foi criado como int
serial = int(input("\nDigite o número de série do equipamento que deseja excluir: "))

for i in inventario:
    if serial == i[2]:
        inventario.remove(i)

# Imprime novamente cada item da lista inventario, atualizada, contendo cada dado da lista equipamento, composta de 4 posições
for i in inventario:
    print("\nEquipamento: ", i[0])
    print("Valor: ", i[1])
    print("Serial: ", i[2])
    print("Departamento: ", i[3])

# Faz um resumo dos valores dos equipamentos do inventário utilizando funções max, min e sum

# Declaração de variável tipo lista que armazena o valor de cada equipamento
valores = []

# Percorre todos os itens da lista inventario
for i in inventario:
    # Para cada posição de "valor" (index 2) da lista inventario, armazena o dado na nova lista valores
    valores.append(i[1])

# Se a lista valores estiver populada, executa as funções maior valor, menor valor e sumarização dos valores
if len(valores) > 0:
    print("\nValor do equipamento mais caro: ", max(valores))
    print("Valor do equipamento mais barato: ", min(valores))
    print("Valor total dos equipamentos: ", sum(valores))
