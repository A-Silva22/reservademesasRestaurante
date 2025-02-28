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

