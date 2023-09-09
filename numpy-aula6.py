import numpy as np
import numpy.random as npr

# Encontrar os valores comuns entre dois vetores

a = npr.randint(0, 10, 5)
b = npr.randint(0, 10, 5)

print(a, b, np.intersect1d(a, b))

print("#"*100)

# Em um vetor com 100 elementos (0-99), inverta os valores de 42 até 66

c = np.arange(100)

c[42:67] = c[42:67] * -1

# c[42:67] *= -1
# c[(c > 41) & (c < 67)] *= -1    # Usando filtros

print(c)

print("#"*100)

# Encontre o elemento de um vetor mais próximo de um dado valor

d = npr.randint(0, 100, 50)
valor = npr.uniform(0, 100)

print(d)

i = np.abs(d - valor).argmin() # Pega o índice do menor valor

print(valor, d[i])