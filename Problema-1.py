def somar(m1, m2):
    matriz_soma = []
    # Supondo que as duas matrizes possuem o mesmo tamanho
    quant_linhas = len(m1) # Conta quantas linhas existem
    quant_colunas = len(m1[0]) # Conta quantos elementos têm em uma linha
    for i in range(quant_linhas):
        # Cria uma nova linha na matriz_soma
        matriz_soma.append([])
        for j in range(quant_colunas):
            # Somando os elementos que possuem o mesmo índice
            soma = m1[i][j] + m2[i][j]
            matriz_soma[i].append(soma)
    return matriz_soma
def preencher_matrizes(linha,coluna):
    matriz=[]
    coluna = int(coluna)
    for x in range(coluna):
        print("Linha ",x+1,": ")
        elementos = input()
        elementos = elementos.split()
        for i in range(len(elementos)):
            elementos[i] = int(elementos[i])
        matriz.append(elementos)
    return matriz

print("Digite a ordem da matriz da primeira matriz")
print("Linhas:")
Linhas_M1 = int(input())
print("Colunas:")
Colunas_M1 = int(input())
print("Digite a ordem da matriz da segunda matriz")
print("Linhas:")
Linhas_M2 = int(input())
print("Colunas:")
Colunas_M2 = int(input())
if Linhas_M1 != Linhas_M2 or Colunas_M1 != Colunas_M2:
    print("A ordem das matrizes são diferente não ha como somar ")
else:
    print("digite os elementos da primeira matriz(com espaço)")
    M1 = preencher_matrizes(Linhas_M1,Colunas_M1)
    print("digite os elementos da segunda matriz(com espaço)")
    M2 = preencher_matrizes(Linhas_M2,Colunas_M2)
    print("O resultado foi: ")
    for x in somar(M1,M2):
        print(x)