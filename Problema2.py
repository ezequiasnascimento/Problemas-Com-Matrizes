from Problema1 import preencher_matrizes


def mutiplicar_matrizes(a, b):
    Linha_a = len(a)
    Coluna_a = len(a[0])
    Linha_b = len(b)
    Coluna_b = len(b[0])
    Matriz_r = []
    for linha in range(Linha_a):
        Matriz_r.append([])
        for coluna in range(Coluna_b):
            Matriz_r[linha].append(0)
            for x in range(Coluna_a):
                Matriz_r[linha][coluna] += a[linha][x] * b[x][coluna]
    return Matriz_r


print("Mutiplicação de matrizes")
print("Digite a ordem da primeira matriz")
print("Linhas:")
Linhas_M1 = int(input())
print("Colunas:")
Colunas_M1 = int(input())
print("Digite a ordem da segunda matriz")
print("Linhas:")
Linhas_M2 = int(input())
print("Colunas:")
Colunas_M2 = int(input())
if Linhas_M1 == Colunas_M2:
    print("digite os elementos da primeira matriz(com espaço)")
    M1 = preencher_matrizes(Linhas_M1,Colunas_M1)
    print("digite os elementos da segunda matriz(com espaço)")
    M2 = preencher_matrizes(Linhas_M2, Colunas_M2)
    print("O resultado foi: ")
    for x in mutiplicar_matrizes(M1, M2):
        print(x)