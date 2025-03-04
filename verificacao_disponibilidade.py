#lógica de verificação de disponibilidade de mesas no Restaurante

class Mesa:
    def __init__(self, numero, capacidade):
        self.numero = numero
        self.capacidade = capacidade
        self.esta_reservada = False

    def reservar(self):
        self.esta_reservada = True

    def liberar(self):
        self.esta_reservada = False

    def __str__(self):
        return f"Mesa {self.numero} - Capacidade: {self.capacidade} - Reservada: {'Sim' if self.esta_reservada else 'Não'}"


class Cliente:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

    def __str__(self):
        return f"Cliente: {self.nome}, Telefone: {self.telefone}"


class Reserva:
    def __init__(self, cliente, mesa, data, horario):
        self.cliente = cliente
        self.mesa = mesa
        self.data = data
        self.horario = horario

    def __str__(self):
        return f"Reserva para {self.cliente.nome} na {self.mesa} em {self.data} às {self.horario}"

class Restaurante:
    def __init__(self, nome):
        self.nome = nome
        self.mesas = []
        self.reservas = []

    def adicionar_mesa(self, mesa):
        self.mesas.append(mesa)

    def verificar_disponibilidade(self, numero_pessoas, data, horario):
        disponiveis = []
        for mesa in self.mesas:
            if mesa.capacidade >= numero_pessoas and not self.esta_reservada(mesa, data, horario):
                disponiveis.append(mesa)
        return disponiveis

    def esta_reservada(self, mesa, data, horario):
        for reserva in self.reservas:
            if reserva.mesa == mesa and reserva.data == data and reserva.horario == horario:
                return True
        return False

    def fazer_reserva(self, cliente, numero_pessoas, data, horario):
        mesas_disponiveis = self.verificar_disponibilidade(numero_pessoas, data, horario)
        if mesas_disponiveis:
            mesa_reservada = mesas_disponiveis[0]
            reserva = Reserva(cliente, mesa_reservada, data, horario)
            self.reservas.append(reserva)
            mesa_reservada.reservar()
            return reserva
        else:
            return None

    def __str__(self):
        return f"Restaurante: {self.nome}, Mesas: {[str(mesa) for mesa in self.mesas]}"


#Exemplo de uso

# Criação do restaurante
restaurante = Restaurante("Restaurante XPTO")

# Adição de mesas ao restaurante
restaurante.adicionar_mesa(Mesa(1, 4))
restaurante.adicionar_mesa(Mesa(2, 2))
restaurante.adicionar_mesa(Mesa(3, 6))

# Criação de um cliente
cliente = Cliente("Alberta", "1234-5678")

# Tentativa de fazer uma reserva
reserva = restaurante.fazer_reserva(cliente, 2, "2025-03-04", "19:00")

if reserva:
    print("Reserva realizada com sucesso!")
    print(reserva)
else:
    print("Não há mesas disponíveis para o número de pessoas desejado.")