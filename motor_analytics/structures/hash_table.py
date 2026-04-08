# ============================================================
#  HashTable — implementada do zero
#  Colisões resolvidas por encadeamento (chaining)
# ============================================================

class HashTable:
    def __init__(self, size=2048):
        # Tamanho da tabela (quantidade de "baldes")
        self.size = size

        # Cria lista de listas (cada posição é um bucket)
        self.table = [[] for _ in range(size)]

        # Quantidade de chaves armazenadas
        self.num_keys = 0

        # Contador de colisões (útil para análise de desempenho)
        self.collisions = 0

    # ── função hash (djb2) ───────────────────────────────────
    def _hash(self, key):
        # Valor inicial padrão do algoritmo djb2
        h = 5381

        # Percorre cada caractere da chave
        for c in str(key):
            # h * 33 XOR código do caractere
            h = ((h << 5) + h) ^ ord(c)

        # Garante que o índice esteja dentro do tamanho da tabela
        return h % self.size

    # ── inserir / atualizar ──────────────────────────────────
    def insert(self, key, value):
        idx = self._hash(key)        # calcula posição
        bucket = self.table[idx]     # pega o bucket correspondente

        # Verifica se a chave já existe
        for i, (k, _) in enumerate(bucket):
            if k == key:
                # Atualiza o valor existente
                bucket[i] = (key, value)
                return

        # Se já existe algo no bucket → colisão
        if bucket:
            self.collisions += 1

        # Adiciona novo par (key, value)
        bucket.append((key, value))
        self.num_keys += 1

    # ── buscar valor ─────────────────────────────────────────
    def get(self, key):
        idx = self._hash(key)

        # Percorre o bucket procurando a chave
        for k, v in self.table[idx]:
            if k == key:
                return v

        # Se não encontrar, retorna None
        return None

    # ── verificar existência ─────────────────────────────────
    def contains(self, key):
        return self.get(key) is not None

    # ── remover chave ────────────────────────────────────────
    def delete(self, key):
        idx = self._hash(key)
        bucket = self.table[idx]

        # Procura a chave dentro do bucket
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket.pop(i)   # remove o item
                self.num_keys -= 1
                return True

        return False  # não encontrou

    # ── iterar sobre todos os elementos ──────────────────────
    def items(self):
        # Percorre todos os buckets
        for bucket in self.table:
            for k, v in bucket:
                yield k, v   # generator (não cria lista)

    def keys(self):
        # Retorna apenas as chaves
        for k, _ in self.items():
            yield k

    def values(self):
        # Retorna apenas os valores
        for _, v in self.items():
            yield v

    # ── métricas (importante para análise) ───────────────────
    def load_factor(self):
        # Taxa de ocupação da tabela
        return self.num_keys / self.size

    def stats(self):
        # Quantos buckets estão sendo usados
        used = sum(1 for b in self.table if b)

        # Maior tamanho de lista dentro de um bucket
        maxlen = max((len(b) for b in self.table), default=0)

        return {
            "size": self.size,
            "keys": self.num_keys,
            "collisions": self.collisions,
            "load_factor": round(self.load_factor(), 4),
            "buckets_used": used,
            "max_chain": maxlen,
        }

    # ── representação para debug ─────────────────────────────
    def __repr__(self):
        s = self.stats()
        return (f"HashTable(size={s['size']}, keys={s['keys']}, "
                f"load={s['load_factor']}, collisions={s['collisions']})")