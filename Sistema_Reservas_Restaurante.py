# Exemplo de lista de reservas

reservas = [
    {"id": 1, "nome": "Reserva 1", "ativa": True},
    {"id": 2, "nome": "Reserva 2", "ativa": False},
    {"id": 3, "nome": "Reserva 3", "ativa": True},
    {"id": 4, "nome": "Reserva 1", "ativa": False},
]

def listar_reservas_ativas(reservas):
    reservas_ativas = [reserva for reserva in reservas if reserva["ativa"]]
    return reservas_ativas

# Exemplo de uso da função
reservas_ativas = listar_reservas_ativas(reservas)
for reserva in reservas_ativas:
    print(f"ID: {reserva['id']}, Nome: {reserva['nome']}")

# Exemplo de lista de mesas
mesas = [
    {"id": 1, "ocupada": True},
    {"id": 2, "ocupada": False},
    {"id": 3, "ocupada": True},
    {"id": 4, "ocupada": False},
    {"id": 5, "ocupada": True},
]

def mostrar_dashboard(mesas):
    total_mesas = len(mesas)
    mesas_ocupadas = len([mesa for mesa in mesas if mesa["ocupada"]])
    mesas_livres = total_mesas - mesas_ocupadas

    print("Dashboard:")
    print(f"Total de mesas : {total_mesas}")
    print(f"Mesas ocupadas: {mesas_ocupadas}")
    print(f"Mesas livres: {mesas_livres}")

# Exemplo do uso da função
mostrar_dashboard(mesas)
