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
class Sistema_Reservas():
    def __init__(self):
        self.clientes = []
        self.mesas = []
        self.reservas = []
        self.restaurantes = []
    pass

    class Mesa():
        def __init__(self, nMesa, capacidade, tipoMesa, reservada = False):
            self.nMesa = nMesa
            self.capacidade = capacidade
            self.tipoMesa = tipoMesa
            self.reservada = reservada
        pass

    class Cliente():
        def __init__(self, nome, contacto, frequente = False):
            self.nome = nome
            self.contacto = contacto
            self.frequente = frequente
        pass

    class Restaurante():
        def __init__(self, nome, mesas, contacto, capacidade, morada, nif, horario):
            self.nome = "Manecas"
            self.mesas = 10
            self.contacto = "912345678"
            self.capacidade = 50
            self.morada = "Av. da Ficticia, 123"
            self.nif = "123456789"
            self.horario = "12:00-15:00, 19:00-23:00"
        pass

    class Reserva():
        def __init__(self, cliente, nMesa, data, hora):
            self.cliente = cliente
            self.nMesa = nMesa
            self.data = data
            self.hora = hora
        pass
