import math
    
def descodifica(entradaCodificada):
    
  qtdColuna=math.sqrt(len(entradaCodificada))
  matriz=[]
  lista=[]
  for digito in entradaCodificada:
    if len(lista)==qtdColuna:
      matriz.append(lista)
      lista=[]
    lista.append(digito)
  matriz.append(lista)
  palavra=""
  for i in range(len(matriz)):
    for j in range(len(matriz[i])):
      try:
        letra=matriz[j][i]
      except:
        return "INVALIDO"
      palavra+=letra
  return (palavra)

palavrasDecodificadas = []
quantidade=int(input())
for i in range(quantidade):
  entrada=input()
  palavrasDecodificadas.append((descodifica(entrada)))

for i in palavrasDecodificadas:
    print(i)
