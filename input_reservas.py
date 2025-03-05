# criar input para reservas
"""
--Reserva:

    Dados - data,
            titularReserva,
            nPessoas,
            tipoMesa,
            contacto, 
"""



import datetime
now = datetime.datetime.now()
hour = now.hour

if hour < 12:
    print("Bom Dia. ")
elif hour < 18:
    print("Boa Tarde. ")
else:
    print("Boa Noite. ")





reservaNome = input("Por favor coloque o Nome em que a reserva ficará registada: ")
reservaData = input("Por favor selecione o dia da sua reserva: ")
reservaHora = input("Por favor selecione a hora da sua reserva: ")





# criar input para cancelar reservas

import datetime
now = datetime.datetime.now()
hour = now.hour

if hour < 12:
    print("Bom Dia. ")
elif hour < 18:
    print("Boa Tarde. ")
else:
    print("Boa Noite. ")





reservaNome = input("Por favor coloque o Nome em que a reserva ficou registada: ")
reservaData = input("Por favor selecione o dia da sua reserva: ")
reservaHora = input("Por favor selecione a hora da sua reserva: ")

cancelar = input("Confirma o cancelamento da reserva? (SIM/NÃO) " )
                 
if cancelar == "SIM":
    print("Reserva Cancelada. ")
else:
    print("Operação Anulada")
