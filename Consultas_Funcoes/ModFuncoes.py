# Módulo de criação de funcoes para utilizar no gerenciamento do inventário

# Define função para preenchimento dos dados do Inventario
def preencherInventario(lista):

    # Inicializa variável resposta com valor "S" para que ocorra o primeiro preenchimento da lista
    resp = "S"
    # Enquanto resposta for S, a variável equipamento do tipo lista vai armazenando os dados digitados
    while resp == "S":
        equipamento = [input("Equipamento: "),
                       float(input("Valor: ")),
                       int(input("Numero Serial: ")),
                       input("Departamento: ")]
        # Parâmetro da função vai receber dados da lista equipamento
        lista.append(equipamento)
        resp = input("Digite \"S\" para continuar: ").upper()

# Define função para exibição dos dados do Inventario
def exibirInventario(lista):
    # Varre toda a lista
    for i in lista:
        print("Nome: ", i[0])
        print("Valor: ", i[1])
        print("Serial: ", i[2])
        print("Departamento: ", i[3])

# Define função para consultar item do Inventario por nome
def localizarPorNome(lista):
    # Declaração de variável que vai receber o dado a ser buscado na lista
    busca = input("\nDigite o nome do equipamento que deseja buscar: ")
    # Varre toda a lista
    for i in lista:
        # Se valor digitado for igual a posição da lista, imprime os dados do equipamento
        if busca == i[0]:
            print("Valor: ", i[1])
            print("Serial: ", i[2])
            print("Departamento: ", i[3])

# Define função para depreciar item do Inventario por nome
def depreciarPorNome(lista, porcent):
    # Declaração de variável que vai receber o dado (por equipamento) a ser modificado na lista
    depreciacao = input("\nDigite o nome do equipamento que deseja alterar: ")
    porcent = int(input("\nDigite o percentual a depreciar: "))
    for i in lista:
        if depreciacao == i[0]:
            print("Valor anterior: ", i[1])
            i[1] = i[1] * (1 - porcent/100)
            print("Valor atualizado: ", i[1])

# Define função para excluir item do Inventario por numero serial
def excluirPorSerial(lista):
    # Declaração de variável que vai receber o dado (por numero de serie) a ser removido da lista
    # É importante converter para int porque na lista equipamentos o serial foi criado como int
    serial = int(input("\nDigite o número de série do equipamento que deseja excluir: "))

    for i in lista:
        if serial == i[2]:
            lista.remove(i)

# Define função para exibir resumo dos valores do inventário
def resumirValores(lista):

    # Declaração de variável tipo lista que armazena o valor de cada equipamento
    valores = []

    # Percorre todos os itens da lista inventario
    for i in lista:
        # Para cada posição de "valor" (index 2) da lista inventario, armazena o dado na nova lista valores
        valores.append(i[1])

    # Se a lista valores estiver populada, executa as funções maior valor, menor valor e sumarização dos valores
    if len(valores) > 0:
        print("\nValor do equipamento mais caro: ", max(valores))
        print("Valor do equipamento mais barato: ", min(valores))
        print("Valor total dos equipamentos: ", sum(valores))
