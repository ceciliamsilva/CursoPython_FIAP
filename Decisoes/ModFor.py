# Declaração de variáveis e atribuições
tabuada = int(input("Digite um número para exibir a tabuada: "))

print("Tabuada do número ", tabuada)

# Comando for de repetição
for valor in range(1, 11, 1):
    # Repete o print abaixo iniciando o valor em 1, acrescentando 1, enquanto o incremento for menor 11
    print(str(tabuada) + " x " + str(valor) + " = " + str((tabuada * valor)))