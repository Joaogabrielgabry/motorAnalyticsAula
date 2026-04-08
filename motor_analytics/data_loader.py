from models.event import Event
from structures.hash_table import HashTable

# Dias por mês (não está sendo usado diretamente aqui, mas pode ser útil)
_DAYS_IN_MONTH = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


# Verifica se o ano é bissexto
def _is_leap(y):
    return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)


# Calcula o dia da semana usando fórmula de Zeller
def _weekday(year, month, day):
    """Retorna: 0=segunda ... 6=domingo"""
    if month < 3:
        month += 12
        year -= 1

    k = year % 100
    j = year // 100

    h = (day + (13*(month+1))//5 + k + k//4 + j//4 - 2*j) % 7

    # Ajusta para padrão (segunda=0)
    return (h + 5) % 7


def load_data(file_path):
    """
    Lê o CSV e retorna:
    - lista de eventos
    - várias HashTables para acesso rápido
    """

    events = []

    # Abre o arquivo
    with open(file_path, "r", encoding="utf-8") as f:
        next(f)  # pula cabeçalho

        # Lê linha por linha
        for line in f:
            line = line.strip()

            # Ignora linhas vazias
            if not line:
                continue

            parts = line.split(",")

            # Validação básica
            if len(parts) < 7:
                continue

            # Cria objeto Event
            ev = Event(
                parts[0],  # id
                parts[1],  # timestamp
                parts[2],  # zona
                parts[3],  # tipo
                parts[4],  # duração
                parts[5],  # gênero
                parts[6],  # idade
            )

            # Calcula dia da semana manualmente
            y, m, d = int(ev.date[:4]), int(ev.date[5:7]), int(ev.date[8:10])
            ev.weekday = _weekday(y, m, d)

            # Adiciona à lista principal
            events.append(ev)

    # ================================
    # CRIAÇÃO DOS ÍNDICES (HashTables)
    # ================================

    idx_zone      = HashTable(size=64)
    idx_date      = HashTable(size=256)
    idx_type      = HashTable(size=8)
    idx_zone_date = HashTable(size=512)

    # Preenche os índices
    for ev in events:

        # Indexação por zona
        lst = idx_zone.get(ev.zone_id)
        if lst is None:
            lst = []
            idx_zone.insert(ev.zone_id, lst)
        lst.append(ev)

        # Indexação por data
        lst = idx_date.get(ev.date)
        if lst is None:
            lst = []
            idx_date.insert(ev.date, lst)
        lst.append(ev)

        # Indexação por tipo
        lst = idx_type.get(ev.event_type)
        if lst is None:
            lst = []
            idx_type.insert(ev.event_type, lst)
        lst.append(ev)

        # Indexação por zona + data
        key = f"{ev.zone_id}|{ev.date}"
        lst = idx_zone_date.get(key)
        if lst is None:
            lst = []
            idx_zone_date.insert(key, lst)
        lst.append(ev)

    # Retorna tudo organizado
    return events, idx_zone, idx_date, idx_type, idx_zone_date