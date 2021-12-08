#Declaração de variáveis e atribuições
nome = input("Digite um funcionário: ")
empresa = input("Digite uma instituição: ")
#Cria variável como inteiro
qtd_funcionarios = int(input("Digite a quantidade de funcionários: "))
#Cria variável como float
mediaMensalidade = float(input("Digite a média da mensalidade: "))

#Imprime valor das variáveis nome e empresa concatenados com texto fixo
print(nome + " trabalha na empresa " + empresa + ".")

#Imprime valor da variável qtd_funcionarios concatenado com texto
print("Possui: ", qtd_funcionarios, " funcionários.")

#Imprime valor da variável mediaMensalidade convertido em string, concatenado com texto
print("A media da mensalidade é de: " + str(mediaMensalidade) + ".")

#Verificando o tipo de dado das variáveis criadas:
print("======Verifique os tipos de dados abaixo:======")
print("O tipo de dado da variável [nome] é: ", type(nome))
print("O tipo de dado da variável [empresa] é: ", type(empresa))
print("O tipo de dado da variável [qtd_funcionarios] é: ", type(qtd_funcionarios))
print("O tipo de dado da variável [mediaMensalidade] é: ", type(mediaMensalidade))
