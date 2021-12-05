# Declaração de variáveis e atribuições
numero = int(input("Digite um numero: "))

# Comando while de repetição
while numero < 100:
    # Se número digitado for menor que 100, imprime o número (converte o numero
    # inteiro em string para imprimir) e soma 1 ao numero até que chegue ao 100
    # e o comando seja encerrado
    print("\t" + str(numero))
    # Soma um ao numero impresso
    numero = numero + 1

print("Laço de repetição encerrado")