# ============================================================
#  Algoritmos de Pesquisa — implementados do zero
#  1. Busca Binária  (O(log n))
#  2. KMP — Knuth-Morris-Pratt  (O(n + m))
# ============================================================


# ── 1. BUSCA BINÁRIA ─────────────────────────────────────────
def binary_search(arr, target, key=None):
    """
    Pesquisa binária em lista ORDENADA.
    
    - arr: lista ordenada
    - target: valor procurado
    - key: função para extrair valor (ex: lambda e: e.date)

    Retorna o índice do elemento encontrado ou -1.
    """

    # Define função de acesso ao valor
    get = key if key else lambda x: x

    # Ponteiros inicial e final
    left = 0
    right = len(arr) - 1

    # Enquanto houver intervalo de busca
    while left <= right:
        mid = (left + right) // 2   # meio
        val = get(arr[mid])         # valor no meio

        if val == target:
            return mid              # encontrou
        elif val < target:
            left = mid + 1          # busca na direita
        else:
            right = mid - 1         # busca na esquerda

    return -1                       # não encontrado


# ── BUSCA BINÁRIA POR INTERVALO ─────────────────────────────
def binary_search_range(arr, lo, hi, key=None):
    """
    Retorna todos os elementos cujo valor está no intervalo [lo, hi].

    Complexidade: O(log n + k)
    (log n para encontrar posição + k elementos retornados)
    """

    get = key if key else lambda x: x

    # ── encontra início do intervalo ──
    left, right = 0, len(arr)

    while left < right:
        mid = (left + right) // 2

        if get(arr[mid]) < lo:
            left = mid + 1
        else:
            right = mid

    start = left

    # ── encontra fim do intervalo ──
    left, right = 0, len(arr)

    while left < right:
        mid = (left + right) // 2

        if get(arr[mid]) <= hi:
            left = mid + 1
        else:
            right = mid

    end = left

    # Retorna fatia da lista
    return arr[start:end]


# ── 2. KMP (Knuth-Morris-Pratt) ─────────────────────────────

def _build_failure(pattern):
    """
    Cria tabela de falhas (prefix function).

    Essa tabela diz:
    "Se der erro, pra onde voltar no padrão?"
    """

    m = len(pattern)

    # Lista de falhas (mesmo tamanho do padrão)
    fail = [0] * m

    j = 0  # tamanho do prefixo atual

    for i in range(1, m):
        # Enquanto não bate, volta na tabela
        while j > 0 and pattern[i] != pattern[j]:
            j = fail[j - 1]

        # Se bate, aumenta prefixo
        if pattern[i] == pattern[j]:
            j += 1

        fail[i] = j

    return fail


def kmp_search(text, pattern):
    """
    Busca todas as ocorrências de pattern em text.

    - text: lista (ou string)
    - pattern: sequência procurada

    Retorna lista com índices onde o padrão começa.
    """

    n, m = len(text), len(pattern)

    # Casos inválidos
    if m == 0 or n < m:
        return []

    # Pré-processamento do padrão
    fail = _build_failure(pattern)

    result = []
    j = 0  # posição no padrão

    # Percorre o texto
    for i in range(n):

        # Enquanto não bate, volta usando tabela
        while j > 0 and text[i] != pattern[j]:
            j = fail[j - 1]

        # Se bate, avança
        if text[i] == pattern[j]:
            j += 1

        # Se completou o padrão
        if j == m:
            result.append(i - m + 1)

            # Continua buscando
            j = fail[j - 1]

    return result


def kmp_count(text, pattern):
    """Conta quantas vezes o padrão aparece."""
    return len(kmp_search(text, pattern))