import time

def measure_time(func, *args):
    # Marca o tempo inicial
    start = time.time()

    # Executa a função passada
    result = func(*args)

    # Marca o tempo final
    end = time.time()

    # Calcula e exibe o tempo total em segundos
    print(f"\nTempo de execução: {end - start:.4f} segundos")

    # Retorna o resultado da função
    return result