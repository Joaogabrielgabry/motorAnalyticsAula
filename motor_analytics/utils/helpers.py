import time
import json

# ── Timer ────────────────────────────────────────────────────
def measure_time(func, *args, **kwargs):
    # Marca o tempo inicial
    t0 = time.time()

    # Executa a função passada como parâmetro
    result = func(*args, **kwargs)

    # Calcula o tempo decorrido
    elapsed = time.time() - t0

    # Exibe o tempo formatado (ms se < 1 segundo, senão segundos)
    if elapsed < 1:
        print(f"\n  ⏱  Tempo de execução: {elapsed*1000:.2f} ms")
    else:
        print(f"\n  ⏱  Tempo de execução: {elapsed:.4f} s")

    # Retorna o resultado da função executada
    return result


# ── Parser de zones.json ─────────────────────────────────────
def load_zones(file_path):
    # Abre o arquivo JSON
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)  # Converte JSON em dicionário Python

    # Retorna as zonas e, se existir, os tipos de zona
    # .get evita erro caso "zone_types" não exista
    return data["zones"], data.get("zone_types", {})


# ── Formatação de tabela no terminal ─────────────────────────
def print_table(headers, rows, col_width=None):
    # Se não houver dados, exibe mensagem
    if not rows:
        print("  (sem resultados)")
        return

    # Se largura das colunas não for informada, calcula automaticamente
    if col_width is None:
        widths = [len(h) for h in headers]  # começa pelo tamanho dos cabeçalhos

        # Ajusta largura com base nos dados
        for row in rows:
            for i, cell in enumerate(row):
                widths[i] = max(widths[i], len(str(cell)))

        col_width = widths

    # Monta linha separadora da tabela
    sep = "+-" + "-+-".join("-" * w for w in col_width) + "-+"

    # Monta cabeçalho formatado
    hdr = "| " + " | ".join(str(h).ljust(w) for h, w in zip(headers, col_width)) + " |"

    # Imprime tabela
    print(sep)
    print(hdr)
    print(sep)

    # Imprime cada linha de dados
    for row in rows:
        line = "| " + " | ".join(str(c).ljust(w) for c, w in zip(row, col_width)) + " |"
        print(line)

    print(sep)


# ── Input helpers ─────────────────────────────────────────────
def ask(prompt, default=None):
    # Mostra prompt com valor padrão (se existir)
    val = input(f"  {prompt}" + (f" [{default}]" if default else "") + ": ").strip()

    # Se usuário não digitar nada, retorna o padrão
    return val if val else default


def ask_int(prompt, default=None):
    # Loop até o usuário digitar um número válido
    while True:
        val = ask(prompt, default=str(default) if default is not None else None)

        try:
            return int(val)  # tenta converter para inteiro
        except (TypeError, ValueError):
            print("  ⚠  Por favor insira um número inteiro.")


def ask_date(prompt, default=None):
    """Pede uma data no formato YYYY-MM-DD."""
    while True:
        val = ask(prompt + " (YYYY-MM-DD)", default=default)

        # Validação simples de formato
        if val and len(val) == 10 and val[4] == "-" and val[7] == "-":
            return val

        print("  ⚠  Formato inválido. Use YYYY-MM-DD.")


def ask_datetime(prompt, default=None):
    """Pede data+hora no formato YYYY-MM-DD HH:MM:SS."""
    while True:
        val = ask(prompt + " (YYYY-MM-DD HH:MM:SS)", default=default)

        # Validação básica pelo tamanho da string
        if val and len(val) == 19:
            return val

        print("  ⚠  Formato inválido. Use YYYY-MM-DD HH:MM:SS.")