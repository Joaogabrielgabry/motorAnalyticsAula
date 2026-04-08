# ============================================================
#  Algoritmos de Ordenação — implementados do zero
#  1. Bubble Sort  (O(n²))
#  2. Merge Sort   (O(n log n))
# ============================================================


# ── 1. BUBBLE SORT ──────────────────────────────────────────
def bubble_sort(arr, key=None, reverse=False):
    """
    Ordena lista usando Bubble Sort.

    - Simples, porém lento (O(n²))
    - Retorna (lista_ordenada, nº_comparações)
    """

    arr = list(arr)  # cópia da lista
    n = len(arr)
    cmp = 0          # contador de comparações

    get = key if key else lambda x: x

    # Percorre a lista várias vezes
    for i in range(n):
        swapped = False

        # Compara elementos vizinhos
        for j in range(0, n - i - 1):
            cmp += 1

            a = get(arr[j])
            b = get(arr[j + 1])

            # Troca se estiver fora de ordem
            if (a > b) if not reverse else (a < b):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # Se não houve troca, já está ordenado
        if not swapped:
            break

    return arr, cmp


# ── 2. MERGE SORT ───────────────────────────────────────────
def merge_sort(arr, key=None, reverse=False):
    """
    Ordenação eficiente (divide e conquista)

    Complexidade: O(n log n)
    """

    arr = list(arr)
    cmp_count = [0]  # lista para mutabilidade

    get = key if key else lambda x: x

    # ── Função de merge ──
    def merge(left, right):
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            cmp_count[0] += 1

            a = get(left[i])
            b = get(right[j])

            if (a <= b) if not reverse else (a >= b):
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        # Junta o resto
        result.extend(left[i:])
        result.extend(right[j:])

        return result

    # ── Recursão ──
    def _sort(lst):
        if len(lst) <= 1:
            return lst

        mid = len(lst) // 2

        left = _sort(lst[:mid])
        right = _sort(lst[mid:])

        return merge(left, right)

    sorted_arr = _sort(arr)

    return sorted_arr, cmp_count[0]


# ── BENCHMARK ───────────────────────────────────────────────
def benchmark_sorts(arr, key=None, reverse=False):
    """
    Compara Bubble Sort vs Merge Sort

    Mede:
    - Tempo
    - Número de comparações
    """

    import time

    # ── Bubble ──
    t0 = time.time()
    _, cmp_b = bubble_sort(arr, key=key, reverse=reverse)
    t_bubble = time.time() - t0

    # ── Merge ──
    t0 = time.time()
    _, cmp_m = merge_sort(arr, key=key, reverse=reverse)
    t_merge = time.time() - t0

    return {
        "n": len(arr),
        "bubble": {
            "time_s": round(t_bubble, 6),
            "comparisons": cmp_b
        },
        "merge": {
            "time_s": round(t_merge, 6),
            "comparisons": cmp_m
        },
    }