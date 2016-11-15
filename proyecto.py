import random
def listaAleatorios(n):
      lista = [0]  * n
      for i in range(n):
          lista[i] = random.randint()
      return lista
 
print listaAleatorios(37)
