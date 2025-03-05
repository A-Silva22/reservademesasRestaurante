import os
from restaurante import Restaurante, Cliente, Mesa
from validacoes import validar_telefone, validar_numero_pessoas, validar_data, validar_horario
from datetime import datetime

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_menu():
    print("\n=== Sistema de Reservas de Restaurante ===")
    print("1. Fazer reserva")
    print("2. Cancelar reserva")
    print("3. Lista de reservas")
    print("4. Exibir Dashboard")
    print("5. Sair")
    opcao = input("Escolha uma opção: ")
    return opcao

def exibir_dashboard(restaurante, reservas_existentes):
    print("\n=== Dashboard de Ocupação ===")
    # Ocupação atual
    mesas_ocupadas = sum(1 for reserva in reservas_existentes if reserva['data'] >= datetime.now().date())
    mesas_totais = len(restaurante.mesas)
    print(f"Ocupação atual: {mesas_ocupadas}/{mesas_totais} mesas ocupadas.")
    
    # Ocupação diária
    hoje = datetime.now().date()
    reservas_hoje = [reserva for reserva in reservas_existentes if reserva['data'] == hoje]
    print(f"Reservas de hoje: {len(reservas_hoje)} reservas.")
    input("\nPressione ENTER para voltar ao menu...")

def main():
    restaurante = Restaurante("Restaurante XPTO")
    
    # Adicionando mesas ao restaurante
    restaurante.adicionar_mesa(Mesa(1, 4))
    restaurante.adicionar_mesa(Mesa(2, 2))
    restaurante.adicionar_mesa(Mesa(3, 6))

    reservas_existentes = []  # Lista de reservas para verificar no horário

    while True:
        limpar_tela()
        opcao = exibir_menu()
        
        if opcao == "1":
            while True:
                limpar_tela()
                print("=== Fazer Reserva ===")
                nome = input("Nome do cliente (ou digite 'voltar' para retornar): ")
                if nome.lower() == 'voltar':
                    break

                telefone = input("Telefone do cliente: ")
                if telefone.lower() == 'voltar':
                    break
                if not validar_telefone(telefone):
                    print("Telefone inválido. Digite um telefone válido com 9 a 12 dígitos.")
                    input("Pressione ENTER para continuar...")
                    continue

                numero_pessoas = input("Número de pessoas: ")
                if numero_pessoas.lower() == 'voltar':
                    break
                if not validar_numero_pessoas(numero_pessoas):
                    print("Número de pessoas inválido. Insira um número entre 1 e 6.")
                    input("Pressione ENTER para continuar...")
                    continue

                data = input("Data (YYYY-MM-DD): ")
                if data.lower() == 'voltar':
                    break
                if not validar_data(data):
                    input("Pressione ENTER para continuar...")
                    continue

                horario = input("Horário (HH:MM): ")
                if horario.lower() == 'voltar':
                    break
                if not validar_horario(horario, reservas_existentes, datetime.strptime(data, "%Y-%m-%d")):
                    print("Horário inválido. Certifique-se de que está no formato HH:MM e que não está reservado.")
                    input("Pressione ENTER para continuar...")
                    continue

                cliente = Cliente(nome, telefone)
                reserva = restaurante.fazer_reserva(cliente, int(numero_pessoas), data, horario)
                if reserva:
                    print("Reserva realizada com sucesso!", reserva)
                    reservas_existentes.append({'data': datetime.strptime(data, "%Y-%m-%d").date(), 'horario': horario})  # Adiciona a reserva na lista
                else:
                    print("Não há mesas disponíveis para esse horário.")
                input("Pressione ENTER para continuar...")
        
        elif opcao == "2":
            while True:
                limpar_tela()
                print("=== Cancelar Reserva ===")
                nome_cliente = input("Nome do cliente (ou digite 'voltar' para retornar): ")
                if nome_cliente.lower() == 'voltar':
                    break
                data = input("Data (YYYY-MM-DD): ")
                if data.lower() == 'voltar':
                    break
                horario = input("Horário (HH:MM): ")
                if horario.lower() == 'voltar':
                    break
                if restaurante.cancelar_reserva(nome_cliente, data, horario):
                    print("Reserva cancelada com sucesso!")
                    reservas_existentes = [reserva for reserva in reservas_existentes if not (reserva['data'].strftime("%Y-%m-%d") == data and reserva['horario'] == horario)]  # Remove da lista de reservas
                else:
                    print("Reserva não encontrada.")
                input("Pressione ENTER para continuar...")
        
        elif opcao == "3":
            limpar_tela()
            print("\n=== Lista de Reservas ===")
            print(restaurante.listar_reservas())
            input("\nPressione ENTER para voltar ao menu...")
        
        elif opcao == "4":
            exibir_dashboard(restaurante, reservas_existentes)
        
        elif opcao == "5":
            print("A Encerrar...")
            break
        
        else:
            print("Opção inválida! Tente novamente.")
            input("Pressione ENTER para continuar...")

if __name__ == "__main__":
    main()