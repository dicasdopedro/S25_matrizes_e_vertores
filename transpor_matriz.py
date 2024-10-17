temperaturas = [
    [22, 25, 28, 32],  # Guarulhos
    [20, 23, 26, 30],  # Campinas
    [18, 22, 25, 29]   # Araraquara
]

# Função para exibir uma matriz
def exibir_matriz(matriz):
    for linha in matriz:
        print(linha)

print("Matriz original:")
exibir_matriz(temperaturas)

# Transpor a matriz
def transpor_matriz(matriz):
    return [[matriz[j][i] for j in range(len(matriz))] for i in range(len(matriz[0]))]

# Exibir a matriz transposta
matriz_transposta = transpor_matriz(temperaturas)
print("\nMatriz transposta:")
exibir_matriz(matriz_transposta)
