from Consultas_Funcoes.ModFuncoes import *

minhaLista = []
print("\nPreenchendo Inventario")
preencherInventario(minhaLista)
print("\nExibindo")
exibirInventario(minhaLista)

print("\nPesquisando")
localizarPorNome(minhaLista)
print("\nAlterando")
depreciarPorNome(minhaLista, 10)

print("\nExcluindo")
print(excluirPorSerial(minhaLista))

print("\nResumindo")
resumirValores(minhaLista)

