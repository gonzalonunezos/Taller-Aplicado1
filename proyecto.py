import random
def listaAleatorios(n):
      lista = [0]  * n
      for i in range(6):
          lista[i] = random.randint(1,36)
      return lista
def listaordenada(lista):
      listaAleatorios.sort()
      
print listaAleatorios()
