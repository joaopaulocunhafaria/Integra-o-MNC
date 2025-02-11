import os
import time
import csv
from typing import List

def ler_entrada(input_filename: str) -> tuple:
    with open(input_filename, "r") as infile:
        line: str = infile.readline().strip()
        parts: List[str] = [x.strip() for x in line.split(",") if x.strip() != '']
        
        if len(parts) < 3:
            raise ValueError("O arquivo de entrada deve conter pelo menos 3 números: 2 para os limites e 1 ou mais para os valores da função.")

        a: float = float(parts[0])
        b: float = float(parts[1])
        valores: List[float] = [float(x) for x in parts[2:]]

    return a, b, valores

def executar_todos_os_metodos(input_filename: str):
    a, b, valores = ler_entrada(input_filename)
    
    # Convertendo os valores para uma string para passar na linha de comando
    valores_str = " ".join(map(str, valores))
    
    metodos = {
        "regra_trapezios": "src/regra_trapezios.py",
        "primeira_simpson": "src/primeira_simpson.py",
        "segunda_simpson": "src/segunda_simpson.py",
        "quadratura_gaussiana": "src/quadratura_gaussiana.py",
        "extrapolacao_richardson": "src/extrapolacao_richardson.py"
    }

    for nome, script in metodos.items():
        print(f"\nExecutando {nome}...")

        # Iniciando a contagem do tempo
        start_time = time.time()
        # Passando os valores como argumentos para cada script
        os.system(f"python {script} {a} {b} {valores_str}")
        # Calculando o tempo de execução
        elapsed_time = time.time() - start_time
        print(f"Tempo de execução: {elapsed_time:.6f} segundos")

        # Escrevendo o tempo de execução no arquivo de saída
        with open(output_filename, "a", newline="") as outfile:
            writer = csv.writer(outfile)
            writer.writerow([nome, elapsed_time])


if __name__ == "__main__":
    # criar um arquivo de saída
    output_filename = "datasets/output/tempo_saida.csv"
    with open(output_filename, "w", newline="") as outfile:
        writer = csv.writer(outfile)
        writer.writerow(["Método", "Tempo de execução (s)"])


    input_filename = "datasets/input/entrada.csv"  # Caminho do arquivo de entrada
    executar_todos_os_metodos(input_filename)
