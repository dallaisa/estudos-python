'''
def duas_linhas(largura):
   matriz = []


   for i in range(2): #range(2) é a lista [0,1]
       minha_linha = []
       for i in range(largura):
           minha_linha.append('.')
       matriz.append(minha_linha)


   return matriz
resultado = duas_linhas(4)
print(resultado)
'''

'''
def duas_linhas(largura):
    matriz =[]

    for i in range(2):
        minha_lista= []
        for i in range(largura):
            minha_lista.append('.')
            matriz.append(minha_lista)
        return matriz
resultado = duas_linhas(3)
print(resultado)
'''
'''
def sete_linhas(largura):
    matriz = []

    for i in range(7):
        minha_linha = []
        for j in range(largura):
            minha_linha.append('.')
        matriz.append(minha_linha)

    return matriz
# Criar uma matriz com 7 linhas e largura 4
resultado = sete_linhas(4)

# Imprimir o resultado
print("Resultado de sete_linhas(4):")
for linha in resultado:
    print(linha)
'''
def mostra_listas(lista_de_listas):
    string_grande = ""
    for lista in lista_de_listas:
        string = ""
        for letra in lista:
            string += letra
        string_grande += string
        string_grande += '\n'
    return string_grande

listas = [['b', 'a', 'n', 'a', 'n', 'a']]

print(mostra_listas(listas))


'''
def mostra_listas(lista_de_listas):
    string_grande = ""
    for lista in lista_de_listas:
        for letra in lista:
            string_grande += letra  
    return string_grande

# Testando a função com uma lista de listas de caracteres
listas = [['b', 'a', 'n', 'a', 'n', 'a']]
print(mostra_listas(listas))  
'''