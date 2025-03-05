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
        status = "Reservada" if self.esta_reservada else "Disponível"
        return f"Mesa {self.numero} - Capacidade: {self.capacidade} - {status}"


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
        return f"Reserva: {self.cliente.nome} - {self.mesa} - {self.data} às {self.horario}"


class Restaurante:
    def __init__(self, nome):
        self.nome = nome
        self.mesas = []
        self.reservas = []

    def adicionar_mesa(self, mesa):
        self.mesas.append(mesa)

    def verificar_disponibilidade(self, numero_pessoas, data, horario):
        return [mesa for mesa in self.mesas if mesa.capacidade >= numero_pessoas and not self.esta_reservada(mesa, data, horario)]

    def esta_reservada(self, mesa, data, horario):
        return any(reserva.mesa == mesa and reserva.data == data and reserva.horario == horario for reserva in self.reservas)

    def fazer_reserva(self, cliente, numero_pessoas, data, horario):
        mesas_disponiveis = self.verificar_disponibilidade(numero_pessoas, data, horario)
        if mesas_disponiveis:
            mesa_reservada = mesas_disponiveis[0]
            reserva = Reserva(cliente, mesa_reservada, data, horario)
            self.reservas.append(reserva)
            mesa_reservada.reservar()
            return reserva
        return None

    def cancelar_reserva(self, nome_cliente, data, horario):
        for reserva in self.reservas:
            if reserva.cliente.nome == nome_cliente and reserva.data == data and reserva.horario == horario:
                reserva.mesa.liberar()
                self.reservas.remove(reserva)
                return True
        return False

    def listar_reservas(self):
        return "\n".join(str(reserva) for reserva in self.reservas) if self.reservas else "Nenhuma reserva encontrada."

    def __str__(self):
        return f"Restaurante: {self.nome}, Mesas: {[str(mesa) for mesa in self.mesas]}"
