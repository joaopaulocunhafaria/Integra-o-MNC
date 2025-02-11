import sys
import time
import csv
from typing import List

def simpson3_8_array(valores: List[float], h: float) -> float:
    n: int = len(valores) - 1
    while n % 3 != 0: 
        n -= 1
        valores = valores[:n+1]


    soma: float = valores[0] + valores[-1]
    for i in range(1, n):
        if i % 3 == 0:
            soma += 2 * valores[i]
        else:
            soma += 3 * valores[i]

    integral: float = (3 * h / 8) * soma
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

    resultado: float = simpson3_8_array(valores, h)

    print(f"Resultado da integral (Simpson 3/8): {resultado}")

if __name__ == "__main__":
    main()
