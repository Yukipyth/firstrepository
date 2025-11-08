# Exercício - Unir listas
# Crie uma função zipper (como zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

def zipper(lista1, lista2):
  """
  Une duas listas em tuplas, parando no final da lista mais curta.
  Usa a função nativa zip() do Python.
  """
  # A função zip() retorna um "iterador". 
  # Usamos list() para converter esse iterador em uma lista.
  return list(zip(lista1, lista2))

  # intervalo = min(len(lista1), len(lista2))
  # return[(lista1[i], lista2[i]) for i in range(intervalo)]

# --- Exemplo de uso ---
cidades = ['Salvador', 'Ubatuba', 'Belo Horizonte']
estados = ['BA', 'SP', 'MG', 'RJ']

resultado = zipper(cidades, estados)
print(resultado)


