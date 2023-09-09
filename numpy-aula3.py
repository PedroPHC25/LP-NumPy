import numpy as np
import math
import numpy.random as npr

# Broadcasting

lista_a = [1, 2, 3]
lista_b= [4, 5, 6]

a1d_a = np.array([1, 2, 3, 4])
a1d_b = np.array([0, 1, 2, 3])

# Operações básicas

# print(lista_a * lista_b)
print(a1d_a * a1d_b)

print(lista_a * 3)
print(a1d_a * 3)

# print(lista_a + 3)
print(a1d_a + 3)

# print(lista_a - 3)
print(a1d_a - 3)

# print(lista_a ** 3)
print(a1d_a ** 3)

# print(lista_a / 3)
print(a1d_a / 3)

"""
print(a1d_a / 0)
print(a1d_b / 0)

print(a1d_a / a1d_b)
"""

print("#"*100)


# Produtos entre ndarrays

a1d_a = a1d_a.reshape(1, 4)
a1d_b = a1d_b.reshape(4, 1)

# print(a1d_a)
# print(a1d_b)

print(a1d_a * a1d_b)

print("#"*100)


ndarray = np.array([1, 2, 3, 4, 5, 6])

indices = ndarray > 3

print(indices)

indices = (ndarray % 2 == 0)

print(indices)

print("#"*100)


indices = ndarray > 3

print(ndarray[indices])

indices = (ndarray % 2 == 0)

print(ndarray[indices])

print("#"*100)


ndarray = np.arange(9).reshape(3, 3)
indices = np.array([[False, True, False], [True, False, True], [True, True, True]])

print(ndarray)
print(indices)

print(ndarray[indices])

print("#"*100)


# Medidas estatísticas

# Breaking Bad
notas = np.array([87, 72, 95, 93, 70, 100])

# Média
print("Média: ", np.average(notas))

# Mediana
print("Mediana: ", np.median(notas))

# Desvio padrão
print("Desvio padrão: ", np.std(notas))

# Mínimo e máximo
print("Mínimo e máximo: ", np.amin(notas), np.amax(notas))

# Percentil
print("Percentil (70): ", np.percentile(notas, 70))

# Pico a pico
print("Pico a pico: ", np.ptp(notas))

print("#"*100)


# Exercício: Elaborar um programa que trata de uma matriz 2xn composta por:
    # 1 - Uma coleção de valores estimados
    # 2 - Uma coleção de valores observados
    
    # Elaborem 4 funções:
        # 1 - Exibir o erro médio absoluto
        # 2 - Exibir o erro médio quadrático
        # 3 - Exibir os dados gerais da coleção (estatísticos)
        # 4 - Exibir o histograma da coleção
        
        
# numpy.histogram

x = np.array([[3, 1, 4, 1, 5], [9, 2, 6, 5, 3]])

# print(np.mean(np.abs(x[0,] - x[1,])))

# print(np.mean(np.square(x[0,] - x[1,])))

# np.histogram(x, 10)


def mean_absolute_error(array):
    print(np.mean(np.abs(array[0,] - array[1,])))
    
mean_absolute_error(x)

def mean_squared_error(array):
    print(np.mean(np.square))
    
def general_data(array):
    print(f"Médias: {array[0,].mean()} e {array[1,].mean()}\n\
Medianas: {np.median(array[0,])} e {np.median(array[1,])}\n\
Desvios padrão:")
          
          
general_data(x)

































