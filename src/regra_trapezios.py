import sys
import time
import csv
from typing import List

def trapezio_array(valores: List[float], h: float) -> float:
    n: int = len(valores) - 1
    soma: float = valores[0] + valores[-1]
   
    for i in range(1, n):
        soma += valores[i]
   
    integral: float = (h / 2) * soma
   
    return integral

def main() -> None:
    # Pegando argumentos da linha de comando
    args = sys.argv[1:]
    
    if len(args) < 3:
        raise ValueError("Número insuficiente de argumentos. Deve haver pelo menos 3: a, b e valores da função.")
    
    a = float(args[0])
    b = float(args[1])
    valores = [float(x) for x in args[2:]]

    n: int = len(valores) - 1
    h: float = (b - a) / n   

    start_time = time.time()
    
    resultado: float = trapezio_array(valores, h)
    
    elapsed_time = time.time() - start_time
    
    with open("datasets/output/tempo_saida.csv", "a", newline="") as outfile:
        writer = csv.writer(outfile)
        writer.writerow(["Regra do trapezio ", elapsed_time, resultado])   
        
    
    print(f"Resultado da integral (Regra do Trapézio): {resultado}")

if __name__ == "__main__":
    main()
