# ============================================================
#  MinHeap / MaxHeap — implementadas do zero
# ============================================================

class MinHeap:
    """Fila de prioridade mínima (menor valor no topo)."""

    def __init__(self):
        # Lista que representa o heap (árvore binária implícita)
        self.data = []

    # ── tamanho ──────────────────────────────────────────────
    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self.data) == 0

    def peek(self):
        # Retorna o menor elemento (raiz)
        if self.is_empty():
            return None
        return self.data[0]

    # ── inserir ──────────────────────────────────────────────
    def insert(self, value):
        # Adiciona no final
        self.data.append(value)

        # Corrige posição subindo na árvore
        self._heapify_up(len(self.data) - 1)

    # ── remover menor ────────────────────────────────────────
    def extract_min(self):
        if self.is_empty():
            return None

        # Caso só tenha 1 elemento
        if len(self.data) == 1:
            return self.data.pop()

        # Guarda raiz (menor)
        root = self.data[0]

        # Move último elemento para raiz
        self.data[0] = self.data.pop()

        # Corrige descendo
        self._heapify_down(0)

        return root

    # ── índices auxiliares ───────────────────────────────────
    @staticmethod
    def _parent(i): return (i - 1) // 2

    @staticmethod
    def _left(i): return 2 * i + 1

    @staticmethod
    def _right(i): return 2 * i + 2

    # ── sobe na árvore ───────────────────────────────────────
    def _heapify_up(self, i):
        while i > 0:
            p = self._parent(i)

            # Se filho menor que pai → troca
            if self.data[i] < self.data[p]:
                self.data[i], self.data[p] = self.data[p], self.data[i]
                i = p
            else:
                break

    # ── desce na árvore ──────────────────────────────────────
    def _heapify_down(self, i):
        n = len(self.data)

        while True:
            smallest = i
            l, r = self._left(i), self._right(i)

            # Verifica filho esquerdo
            if l < n and self.data[l] < self.data[smallest]:
                smallest = l

            # Verifica filho direito
            if r < n and self.data[r] < self.data[smallest]:
                smallest = r

            # Se não precisa trocar → fim
            if smallest == i:
                break

            # Troca com o menor filho
            self.data[i], self.data[smallest] = self.data[smallest], self.data[i]
            i = smallest

    # ── construir heap em O(n) ───────────────────────────────
    def build(self, lst):
        self.data = list(lst)

        # Começa do meio e desce
        for i in range(len(self.data) // 2 - 1, -1, -1):
            self._heapify_down(i)

    def __repr__(self):
        return f"MinHeap({self.data[:10]}{'...' if len(self.data)>10 else ''})"


# ── MaxHeap (reutiliza MinHeap) ─────────────────────────────
class MaxHeap:
    """
    Fila de prioridade máxima.
    Usa MinHeap invertendo valores (negativos).
    """

    def __init__(self):
        self._h = MinHeap()

    def __len__(self):
        return len(self._h)

    def is_empty(self):
        return self._h.is_empty()

    def peek(self):
        top = self._h.peek()
        if top is None:
            return None

        neg, val = top
        return (-neg, val)

    def insert(self, priority, value):
        # Insere com prioridade negativa
        self._h.insert((-priority, value))

    def extract_max(self):
        item = self._h.extract_min()
        if item is None:
            return None

        neg, val = item
        return (-neg, val)

    def build(self, pairs):
        # Converte para negativo
        self._h.build([(-p, v) for p, v in pairs])

    def __repr__(self):
        return f"MaxHeap(size={len(self)})"


# ── Top-K usando MinHeap ────────────────────────────────────
def top_k(pairs, k):
    """
    Retorna os K maiores elementos de (prioridade, valor)
    Complexidade: O(n log k)
    """

    heap = MinHeap()

    for priority, value in pairs:
        # Se heap ainda não tem K elementos
        if len(heap) < k:
            heap.insert((priority, value))

        # Se valor atual é maior que o menor do heap
        elif priority > heap.peek()[0]:
            heap.extract_min()
            heap.insert((priority, value))

    # Extrai tudo (em ordem crescente)
    result = []
    while not heap.is_empty():
        result.append(heap.extract_min())

    # Inverte → maior primeiro
    result.reverse()

    return result