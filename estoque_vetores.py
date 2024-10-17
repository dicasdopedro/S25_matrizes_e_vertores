# Vetor de estoque de camisetas
estoque = [50, 40, 30]  # [P, M, G]

# Função para exibir o estoque
def exibir_estoque(estoque):
    tamanhos = ['P', 'M', 'G']
    for i in range(len(estoque)):
        print(f"Tamanho {tamanhos[i]}: {estoque[i]} unidades")

# Função para atualizar o estoque
def atualizar_estoque(estoque, indice, quantidade):
    estoque[indice] += quantidade

# Exibindo o estoque inicial
print("Estoque inicial:")
exibir_estoque(estoque)

# Atualizando o estoque do tamanho M
atualizar_estoque(estoque, 1, -5)

# Exibindo o estoque atualizado
print("\nEstoque atualizado:")
exibir_estoque(estoque)