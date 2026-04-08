# Importa funções de outros módulos
from data_loader import load_data
from utils.helpers import load_zones
from menu import start_menu


def main():
    # Mensagem inicial
    print("\n  Carregando dados...")

    # Carrega os dados do CSV e cria índices (HashTables)
    events, idx_zone, idx_date, idx_type, idx_zone_date = load_data("data/dataset.csv")

    # Carrega informações adicionais das zonas (arquivo JSON)
    zones, zone_types = load_zones("data/zones.json")

    # Exibe estatísticas básicas
    print(f"  {len(events):,} eventos carregados!")
    print(f"  {len(list(idx_zone.keys()))} zonas indexadas")
    print(f"  {len(list(idx_date.keys()))} dias no dataset")

    # Exibe estatísticas das HashTables (importante para análise de desempenho)
    print(f"\n  [HashTable stats]")
    for name, ht in [("idx_zone", idx_zone), ("idx_date", idx_date)]:
        s = ht.stats()
        print(f"    {name}: load={s['load_factor']}, collisions={s['collisions']}, "
              f"max_chain={s['max_chain']}")

    # Inicia o menu interativo
    start_menu(events, idx_zone, idx_date, idx_type, idx_zone_date, zones, zone_types)


# Garante que o programa só execute ao rodar diretamente
if __name__ == "__main__":
    main()