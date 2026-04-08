import json

def load_zones(file_path):
    # Abre o arquivo JSON
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)  # Converte JSON para dicionário

    # Retorna diretamente os dados
    # Aqui NÃO usa .get(), então se não existir "zone_types", dá erro
    return data["zones"], data["zone_types"]