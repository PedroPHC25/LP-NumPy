import numpy as np
import time


### Loop for

inicio_tempo_loop = time.time()

vetor_loop = list(range(1, 11))
print(type(vetor_loop))

for number in range(len(vetor_loop)):
    vetor_loop[number] = vetor_loop[number] ** 2
    
# print(vetor_loop)

fim_tempo_loop = time.time()

print("Tempo de um loop: ", fim_tempo_loop - inicio_tempo_loop)


### NumPy

inicio_tempo_vetorizacao = time.time()

vetor_numpy = np.array(range(1, 11))

print(type(vetor_numpy))

vetor_numpy = vetor_numpy ** 2

fim_tempo_vetorizacao = time.time()

print("Tempo de um loop: ", fim_tempo_vetorizacao - inicio_tempo_vetorizacao)

print("#"*100)


# Vetorização para eliminar a necessidade de loops quando se trabalha com arrays

def calcular_quadrado(numero):
    return numero ** 2

funcao_vetorizada = np.vectorize(calcular_quadrado)

# print(calcular_quadrado(vetor_loop))
print(calcular_quadrado(vetor_numpy))

print(funcao_vetorizada(vetor_loop))
print(funcao_vetorizada(vetor_numpy))

print(type(calcular_quadrado))
print(type(funcao_vetorizada))


print("#"*100)


# Em uma matriz 5x5, qual é o índice do elemento 10?

print(np.unravel_index(10, (5,5)))

# Em uma matriz 5x5x5, qual é o índice do elemento 10?

print(np.unravel_index(42, (5,5,5)))


chess_board = np.zeros((8,8))
print(chess_board)

chess_board[1::2,::2] = 1
chess_board[::2,1::2] = 1
print(chess_board)





































