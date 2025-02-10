import csv
import time
from typing import List

def simpson1_3_array(valores: List[float], h: float) -> float:
    n: int = len(valores) - 1
    if n % 2 != 0:
        raise ValueError("O número de subintervalos (len(valores) - 1) deve ser par para a Regra de Simpson 1/3.")

    soma: float = valores[0] + valores[-1]
    for i in range(1, n):
        if i % 2 == 0:
            soma += 2 * valores[i]
        else:
            soma += 4 * valores[i]

    integral: float = (h / 3) * soma
    return integral

def main() -> None:
    input_filename: str = "dataset/input.csv"
    
    with open(input_filename, "r") as infile:
        line: str = infile.readline().strip()
        valores: List[float] = [float(x) for x in line.split(",") if x.strip() != '']
    
    h: float = float(input("Digite o valor de h (passo): "))
    
    inicio: float = time.perf_counter()
    resultado: float = simpson1_3_array(valores, h)
    fim: float = time.perf_counter()
    tempo_exec: float = fim - inicio

    print(f"Resultado da integral (Simpson 1/3): {resultado}")
    print(f"Tempo de execução: {tempo_exec:.6f} segundos")

    output_filename: str = "tempo_saida.csv"
    with open(output_filename, "w", newline="") as outfile:
        writer = csv.writer(outfile)
        writer.writerow(["Tempo de Execução (s)"])
        writer.writerow([tempo_exec])

if __name__ == "__main__":
    main()
