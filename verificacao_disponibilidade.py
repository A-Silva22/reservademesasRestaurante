#lógica de verificação de disponibilidade de mesas no Restaurante

def esta_reservada(reservas, mesa, data, horario):
    return any(reserva.mesa == mesa and reserva.data == data and reserva.horario == horario for reserva in reservas)