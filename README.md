# 10805_ProjetoFinal
 
 2 Projeto 2: Sistema de Reservas para Restaurante

 Objetivo:
 Desenvolver um sistema que permita gerenciar reservas de mesas em um restaurante.
 1

Funcionalidades:

 • Registar e cancelar reservas
 • Gerenciar disponibilidade de mesas (diferentes tamanhos/tipos)
 • Verificar disponibilidade por data e horario
 • Sistema de fila de espera
 • Registo de preferencias de clientes frequentes
 • Dashboard simples com ocupacao atual e diaria

 Conceitos a utilizar:

 • Classes para Mesa, Reserva, Cliente e Restaurante
 • Estruturas para representar a capacidade e layout do restaurante
 • Metodos para verificar disponibilidade(Dentro de classe)
 • Funcoes para otimizar alocacao de mesas(Pode ser fora de classe)
 • Logica para gerenciar conflitos de horario










Classes:

Mesa: 

    Dados - nMesa(numero da mesa), 
            tipoMesa(VIP ou normal)
            lugares(quantidade de pessoas que se podem sentar na mesa),
    



Reserva:

    Dados - data,
            titularReserva,
            nPessoas,
            tipoMesa,
            contacto,


Cliente:

    Dados - nome,
            contacto,
            frequente(true or false)

Restaurante:

    Dados - nome,
            contacto,
            capacidade,
            morada,
            NIF,
            horario




• Registar e cancelar reservas - Lista de reservas: adicionar, editar e remover para gerir as reservas.

Reservas = {data: "",
            titularReserva: "",
            nPessoas: 19,
            tipoMesa: "",
            contacto: ""}

Funções: adicionarReserva, removerReserva, editarReserva


 • Gerenciar disponibilidade de mesas (diferentes tamanhos/tipos) - Se a mesa estiver ocupada, não deixa reservar a mesa (verificar lugares e tipo de mesa)
 • Verificar disponibilidade por data e horario - Se esta data já estiver ocupada, não deixa reservar

 Funções: verificaMesa


 • Sistema de fila de espera: Se o restaurante estiver cheio, pergunta se quer ficar à espera e guarda numa lista.

 Funções: verificaCapacidade

 • Registo de preferencias de clientes frequentes: Regista o que os clientes frequentes mais gostam de consumir.

 Funções: registaPreferencia


• Dashboard simples com ocupacao atual e diaria: Interface que mostra a taxa de ocupacao atual e dados como numero total de clientes diários, reservas, etc.

• Menu para escolhar o que quer visualizar: Interface de escolha onde o utilizador escolhe o que pretende ver ex: 1- Dashboard 2- Clientes 3-Reservas etc.

