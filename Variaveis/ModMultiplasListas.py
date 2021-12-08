# Criando um Inventário com multiplas listas

# Declaração de variável do tipo lista
equipamentos = []
valores = []
seriais = []
departamentos = []

# Inicializa variável resposta com valor "S" para que ocorra o primeiro preenchimento da lista
resposta = "S"

# Enquanto resposta for S, a variável inventário do tipo lista vai armazenando os dados digitados
while resposta == "S":
    equipamentos.append(input("Equipamento: "))
    valores.append(float(input("Valor: ")))
    seriais.append(int(input("Numero Serial: ")))
    departamentos.append(input("Departamento: "))
    resposta = input("Digite \"S\" para continuar: ").upper() # A contrabarra precedendo as "" indica que as "" serão impressas

# Imprime todos os dados da lista inventario, da primeira posição (0) até o total (len()) de itens da lista
for i in range(0,len(equipamentos)):
    print("\nEquipamento: ", (i + 1))
    print("Nome: ", equipamentos[i])
    print("Valor: ", valores[i])
    print("Serial: ", seriais[i])
    print("Departamento: ", departamentos[i])


