📊 Motor de Analytics — Dados de Retalho
📌 Descrição

Este projeto consiste em um motor de analytics desenvolvido em Python para análise de dados de eventos em ambientes de varejo (ex.: lojas, shoppings).

O sistema processa um dataset contendo eventos de entrada, saída e permanência de usuários em diferentes zonas, permitindo a execução de múltiplas consultas analíticas com foco em desempenho.

O principal objetivo do projeto é demonstrar, na prática, a aplicação de estruturas de dados e algoritmos clássicos implementados do zero, sem dependência de bibliotecas externas de alto nível.

🧠 Objetivos
Aplicar conceitos fundamentais de Estruturas de Dados e Algoritmos
Construir um sistema analítico eficiente e modular
Comparar desempenho entre diferentes abordagens algorítmicas
Simular cenários reais de análise de fluxo em ambientes físicos
⚙️ Funcionalidades
🔹 Queries de Agregação Temporal
Ocupação por zona em intervalos de tempo
Média de permanência por zona (por hora)
Identificação de picos de ocupação (Sweep Line)
Comparação de métricas entre dois dias
🔹 Queries de Ranking (Top-K)
Zonas mais visitadas
Blocos de 30 minutos com mais eventos
Zonas com maior tempo médio de permanência
🔹 Análise de Fluxo e Padrões
Fluxo entre zonas (matriz de transição)
Detecção de sequências de zonas (KMP)
Identificação de anomalias (baseado em desvio padrão)
🔹 Queries Compostas
Filtros combinados por:
intervalo de tempo
zona
gênero
faixa etária
🔹 Benchmark
Comparação entre:
Bubble Sort
Merge Sort
Métricas:
Tempo de execução
Número de comparações
🏗️ Arquitetura do Projeto
motor_analytics/
│
├── main.py                # Ponto de entrada
├── menu.py                # Interface CLI
│
├── data_loader.py         # Leitura e indexação dos dados
│
├── models/
│   └── event.py           # Modelo de dados Event
│
├── structures/
│   ├── hash_table.py      # HashTable (chaining)
│   └── heap.py            # MinHeap / MaxHeap
│
├── algorithms/
│   ├── sorting.py         # Bubble Sort / Merge Sort
│   └── search.py          # Busca Binária / KMP
│
├── queries/
│   └── aggregation.py     # Implementação das 12 queries
│
├── utils/
│   ├── helpers.py         # I/O, formatação e utilitários
│   ├── parser.py          # Parser de JSON
│   └── timer.py           # Medição de tempo
│
└── data/
    ├── dataset.csv        # Dataset de eventos
    └── zones.json         # Metadados das zonas
📊 Estruturas de Dados
Hash Table (custom)
Resolução de colisões por encadeamento
Métricas: load factor, colisões, tamanho de cadeia
Heap
MinHeap e MaxHeap
Aplicação em consultas Top-K
🔍 Algoritmos Implementados
Ordenação
Bubble Sort — O(n²)
Merge Sort — O(n log n)
Busca
Busca Binária — O(log n)
KMP (Knuth-Morris-Pratt) — O(n + m)
Outros
Sweep Line (picos de ocupação)
Estatística básica (média, desvio padrão)
Top-K com heap — O(n log k)
📥 Entrada de Dados
CSV (dataset.csv)

Contém eventos no formato:

event_id,timestamp,zone_id,event_type,duration,gender,age_range
event_type: entry | exit | linger
timestamp: YYYY-MM-DD HH:MM:SS
duration: em segundos
JSON (zones.json)

Contém metadados das zonas:

{
  "zones": {
    "Z1": {"label": "Entrada", "type": "entrada"},
    "Z2": {"label": "Loja A", "type": "retalho"}
  },
  "zone_types": {
    "entrada": "...",
    "retalho": "..."
  }
}
▶️ Como Executar
Clone o repositório:
git clone <repo_url>
cd motor_analytics
Execute o projeto:
python main.py
Utilize o menu interativo para executar as queries.
📈 Métricas de Desempenho

O sistema fornece:

Tempo de execução das queries
Estatísticas da Hash Table:
Load factor
Número de colisões
Tamanho máximo das cadeias
🧪 Benchmark

Comparação prática entre algoritmos de ordenação:

Algoritmo	Complexidade	Uso
Bubble Sort	O(n²)	Didático
Merge Sort	O(n log n)	Produção
🎯 Principais Aprendizados
Impacto direto das estruturas de dados no desempenho
Importância da indexação para consultas eficientes
Diferença prática entre algoritmos de ordenação
Aplicação de algoritmos clássicos em cenários reais
📌 Possíveis Extensões
Interface gráfica (GUI)
API REST para consultas
Visualização de dados (gráficos)
Uso de banco de dados (SQL/NoSQL)
Paralelização de queries