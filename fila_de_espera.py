fila_espera = []  # Lista para armazenar os nomes na fila de espera

def adicionar_na_fila(nome_cliente):
    """
    Adiciona um cliente à fila de espera.
    """
    fila_espera.append(nome_cliente)
    print(f"{nome_cliente} foi adicionado à fila de espera.")

def chamar_proximo():
    """
    Remove e chama o próximo cliente da fila de espera.
    """
    if len(fila_espera) > 0:
        proximo = fila_espera.pop(0)
        print(f"O próximo cliente é {proximo}.")
    else:
        print("A fila de espera está vazia.")

def listar_fila():
    """
    Lista todos os clientes na fila de espera.
    """
    if len(fila_espera) > 0:
        print("Fila de espera:")
        for idx, nome in enumerate(fila_espera, start=1):
            print(f"{idx}. {nome}")
    else:
        print("A fila de espera está vazia.")

# Exemplo de uso
adicionar_na_fila("João")
adicionar_na_fila("Maria")
adicionar_na_fila("Ana")

listar_fila()

chamar_proximo()

listar_fila()

chamar_proximo()
chamar_proximo()
chamar_proximo()  # Testar quando a fila está vazia
