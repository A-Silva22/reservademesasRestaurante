def dashboard_mesas(total_mesas, mesas_ocupadas):
    """
    Mostra um dashboard simples com informações sobre o total de mesas,
    quantas estão ocupadas e quantas estão livres.

    Args:
    - total_mesas: Número total de mesas disponíveis no restaurante.
    - mesas_ocupadas: Número de mesas que estão atualmente ocupadas.
    """
    mesas_livres = total_mesas - mesas_ocupadas  # Calcula quantas mesas estão livres

    # Mostra o dashboard
    print("=== DASHBOARD DE MESAS ===")
    print(f"Total de mesas: {total_mesas}")
    print(f"Mesas ocupadas: {mesas_ocupadas}")
    print(f"Mesas livres: {mesas_livres}")
    print("==========================")


# Exemplo de uso
dashboard_mesas(total_mesas=20, mesas_ocupadas=8)
