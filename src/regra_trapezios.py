import csv
import time
from typing import List

def trapezio_array(valores: List[float], h: float) -> float:
    n: int = len(valores) - 1
    soma: float = valores[0] + valores[-1]
   
    for i in range(1, n):
        soma += valores[i]
   
    integral: float = (h / 2) * soma
   
    return integral

def main() -> None:
    input_filename: str = "dataset/primeira_simpson_input.csv"
    
    with open(input_filename, "r") as infile:
        line: str = infile.readline().strip()
        parts: List[str] = [x.strip() for x in line.split(",") if x.strip() != '']
        if len(parts) < 3:
            raise ValueError("O arquivo de entrada deve conter pelo menos 3 números: 2 para os limites e 1 ou mais para os valores da função.")
        a: float = float(parts[0])
        b: float = float(parts[1])
        valores: List[float] = [float(x) for x in parts[2:]]
    
    n: int = len(valores) - 1
    h: float = (b - a) / n
    
    inicio: float = time.perf_counter()
    resultado: float = trapezio_array(valores, h)
    fim: float = time.perf_counter()
    tempo_exec: float = fim - inicio
    
    print(f"Resultado da integral (Regra do Trapézio): {resultado}")
    print(f"Tempo de execução: {tempo_exec:.6f} segundos")
    
    output_filename: str = "dataset/tempo_saida.csv"
    with open(output_filename, "w", newline="") as outfile:
        writer = csv.writer(outfile)
        writer.writerow(["Tempo de Execução (s)"])
        writer.writerow([tempo_exec])

if __name__ == "__main__":
    main()
