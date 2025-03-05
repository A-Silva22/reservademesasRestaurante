import re
from datetime import datetime

def validar_telefone(telefone):
    # Validação de telefone, permitindo tanto o formato simples quanto com DDD e código do país.
    return bool(re.match(r"^\d{9,12}$", telefone))

def validar_numero_pessoas(numero_pessoas):
    try:
        numero_pessoas = int(numero_pessoas)
        return 1 <= numero_pessoas <= 6  # Permitindo números razoáveis entre 1 e 6
    except ValueError:
        return False

def validar_data(data):
    try:
        data_reserva = datetime.strptime(data, "%Y-%m-%d")
        data_atual = datetime.now()

        # Verifica se a data fornecida é no passado
        if data_reserva < data_atual:
            print("Data inválida.")
            return False
        return True
    except ValueError:
        print("Data inválida. Certifique-se de que está no formato YYYY-MM-DD.")
        return False

def validar_horario(horario, reservas_existentes, data_reserva):
    try:
        partes = horario.split(":")
        if len(partes) != 2:
            return False
        hora, minuto = map(int, partes)

        if hora < 0 or hora > 23 or minuto < 0 or minuto > 59:
            return False

        horario_atual = datetime.now()
        horario_reserva = datetime(data_reserva.year, data_reserva.month, data_reserva.day, hora, minuto)

        if horario_reserva < horario_atual:
            print("Horário inválido. Não é possível fazer reservas para horários passados.")
            return False

        for reserva in reservas_existentes:
            if reserva['data'] == data_reserva and reserva['horario'] == horario:
                print("Esse horário já está reservado. Escolha outro.")
                return False

        return True
    except ValueError:
        print("Horário inválido. Certifique-se de que está no formato HH:MM.")
        return False