# Criando um Inventário com multiplas listas e pesquisando dados em uma das listas

# Declaração de variável do tipo lista
equipamentos = []
valores = []
seriais = []
departamentos = []

# Inicializa variável resposta com valor "S" para que ocorra o primeiro preenchimento da lista
resposta = "S"

# Enquanto resposta for S, a variável inventário do tipo lista vai armazenando os dados digitados
while resposta == "S":
    equipamentos.append(input("\nEquipamento: "))
    valores.append(float(input("Valor: ")))
    seriais.append(int(input("Numero Serial: ")))
    departamentos.append(input("Departamento: "))
    resposta = input("\nDigite \"S\" para continuar: ").upper() # A contrabarra precedendo as "" indica que as "" serão impressas

# Declaração de variável que vai receber o dado a ser buscado na lista
busca = input("\nDigite o nome do equipamento que deseja buscar: ")

# Varre toda a lista
for i in range(0,len(equipamentos)):
    # Se valor digitado for igual a posição da lista, imprime os dados do equipamento
    if busca == equipamentos[i]:
        print("Valor: ", valores[i])
        print("Serial: ", seriais[i])
        print("Departamento: ", departamentos[i])


