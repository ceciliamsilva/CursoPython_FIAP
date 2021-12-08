# Criando um Inventário

# Declaração de variável do tipo lista
inventario = []

# Inicializa variável resposta com valor "S" para que ocorra o primeiro preenchimento da lista
resposta = "S"

# Enquanto resposta for S, a variável inventário do tipo lista vai armazenando os dados digitados
while resposta == "S":
    inventario.append(input("Equipamento: "))
    inventario.append(float(input("Valor: ")))
    inventario.append(int(input("Numero Serial: ")))
    inventario.append(input("Departamento: "))
    resposta = input("Digite \"S\" para continuar: ").upper() # A contrabarra precedendo as "" indica que as "" serão impressas

# Imprime todos os dados da lista inventario
for i in inventario:
    print(i)

