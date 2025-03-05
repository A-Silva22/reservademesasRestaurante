from datetime import datetime

reservas = []  # Lista para armazenar as reservas

def adicionar_reserva(nome_cliente, horario):
    """
    Adiciona uma nova reserva se não houver conflitos.

    Args:
    - nome_cliente: Nome do cliente.
    - horario: Horário da reserva (formato 'YYYY-MM-DD HH:MM').
    """
    for reserva in reservas:
        if reserva['horario'] == horario:
            print(f"Conflito detectado! Já existe uma reserva para {horario}.")
            return

    reservas.append({'nome': nome_cliente, 'horario': horario})
    print(f"Reserva confirmada para {nome_cliente} no horário {horario}.")

def listar_reservas():
    """
    Lista todas as reservas existentes.
    """
    if not reservas:
        print("Nenhuma reserva registrada.")
    else:
        print("Reservas confirmadas:")
        for reserva in reservas:
            print(f"- {reserva['nome']}: {reserva['horario']}")

# Exemplo de uso
adicionar_reserva("João", "2025-03-05 20:00")
adicionar_reserva("Maria", "2025-03-05 20:00")  # Conflito esperado
adicionar_reserva("Ana", "2025-03-05 21:00")

listar_reservas()

