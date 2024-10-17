# Matriz de assentos (0 = disponível, 1 = ocupado)
cinema = [
    [0, 0, 1, 0],
    [0, 1, 0, 0],
    [1, 0, 0, 0]
]

# Função para exibir os assentos
def exibir_assentos(cinema):
    for fila in cinema:
        print(fila)

# Função para reservar um assento
def reservar_assento(cinema, fila, assento):
    if cinema[fila][assento] == 0:
        cinema[fila][assento] = 1
        print("Reserva realizada com sucesso!")
    else:
        print("Assento já ocupado.")

# Exibindo os assentos iniciais
print("Assentos no cinema:")
exibir_assentos(cinema)

# Realizando uma reserva
reservar_assento(cinema, 1, 2)

# Exibindo os assentos após a reserva
print("\nAssentos atualizados:")
exibir_assentos(cinema)