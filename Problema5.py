
listaLetras = ["A","B","C","D",1,2,"E","F","G","H",3,4,"I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",5,6,7,8,9,0]

def formandoMatriz(linha,coluna):
    matriz = []
    cont = 0
    for i in range(0,linha):
        linha2 = []
        for x in range(0,coluna):
            linha2.append(listaLetras[cont])
            cont+=1
        matriz.append(linha2)
    return matriz
def mostrandoMatriz(matriz):
    if len(matriz)==1:
      for i in range(0,len(matriz)):
        for x in range(0,len(matriz[0])):
            print(f'[{matriz[i][x]:^3}]',end='')
        print()
    else:
      for i in range(0,len(matriz)):
          for x in range(0,len(matriz[0])):
              print(f'[{matriz[i][x]:^3}]',end='')
          print()
def retomandoCusto(matriz,letras):
    soma = 0
    if len(matriz)==1:
      for x in range(0,len(matriz[0])):
          for z in letras:
              if matriz[0][x]==z:
                  soma+=(1+x+1)
              else:
                  soma+=0
    else:
      for i in range(0,len(matriz)):
          for x in range(0,len(matriz[0])):
              for z in letras:
                  if matriz[i][x]==z:
                      soma+=(i+1+x+1)
                  else:
                      soma+=0
    return soma    
def main():

  somas = []
  valores =  [1,1,1]
  quantidade = int(valores[0])
  linha = int(valores[1])
  coluna = int(valores[2])
  while quantidade!=0 and linha!=0 and coluna!=0:
    letras1 = []
    palavras = []
    valores = input().split()
    quantidade = int(valores[0])
    linha = int(valores[1])
    coluna = int(valores[2])
    if (linha*coluna)!=36:
      break
    else:
      matriz = formandoMatriz(linha,coluna)
      mostrandoMatriz(matriz)
      for i in range(quantidade):
          palavra = input().upper()
          palavras.append(palavra)
      for i in palavras:
        for x in i:
          letras1.append(x)
        somas.append(retomandoCusto(matriz,letras1))
  for i in somas:
    print(i)
try:
  main()
except Exception:
  print("Informe um valor correto!")
