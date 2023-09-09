import numpy as np
import numpy.random as npr

# Operações em ndarrays


print("#"*100)


a1D_1 = np.arange(10)
print(a1D_1, end = "\n\n")

# a1D_1 = a1D_1.reshape(3,2) ERRO!
a1D_1 = a1D_1.reshape(5,2)
print(a1D_1, end = "\n\n")

a1D_1 = a1D_1.transpose()
print(a1D_1, end = "\n\n")


print("#"*100)


a1D_2 = np.arange(20)
print(a1D_2, end = "\n\n")

a1D_2 = a1D_2.reshape(10,2)
print(a1D_2, end = "\n\n")

a1D_3 = np.vstack((a1D_2, a1D_2))
print(a1D_3, end = "\n\n")

a1D_3 = np.hstack((a1D_2, a1D_2))
print(a1D_3, end = "\n\n")

print(f"Dados sobre a1D_3:\n\tDimensão: {a1D_3.ndim}\n\t\
Forma: {a1D_3.shape}\n\n")


print("#"*100, end = "\n\n")


a1D = np.arange(10)

print(a1D)

# Shallow copy

a1D_copy = a1D
print(a1D_copy)

"""
a = 10
print(a)

b = a
print(b)

b = 7
print(a)
print(b)
"""

a1D_copy[0] = 42
print(a1D)
print(a1D_copy)

print(id(a1D))
print(id(a1D_copy))

# Deep copy

a1D = np.arange(10)

a1D_copy = a1D.copy()
print(a1D_copy)

a1D_copy[0] = 42
print(a1D)
print(a1D_copy)

print(id(a1D))
print(id(a1D_copy))

print("#"*100, end = "\n\n")

# Retornos de funções: shallow x deep

print(a1D)

outro_vetor = a1D.reshape(5,2)

print(outro_vetor)

print(id(a1D))
print(id(outro_vetor))

a1D[0] = 42

# outro_vetor[0,0] = 42

print(a1D)
print(outro_vetor)

print(id(a1D))
print(id(outro_vetor))


print("#"*100, end = "\n\n")


# Exercícios


ex1 = np.zeros(42)
print(ex1)

ex2 = np.ones(42)
print(ex2)

ex3 = np.identity(5)
print(ex3)
ex3 = np.eye(5)
print(ex3)

ex4 = np.arange(7, 43)
print(ex4)

ex5 = np.arange(8, 43, 2)
print(ex5)

ex6 = npr.random()
print(ex6)
ex6 = npr.rand(1)
print(ex6)

ex7 = npr.normal(0, 1, 10)
print(ex7)
ex7 = npr.randn(10)
print(ex7)

ex8 = np.full(10, 42)
print(ex8)
ex8 = np.ones(10) * 42
print(ex8)

ex9 = np.arange(1,10).reshape(3,3)
print(ex9)

































