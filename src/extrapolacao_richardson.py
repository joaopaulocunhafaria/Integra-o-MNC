import sys
import time
import csv
from typing import List

# Implementação da Regra de Simpson 1/3 para valores tabulados
def simpson_1_3_array(valores: List[float], h: float) -> float:
    n = len(valores) - 1
    if n % 2 != 0:  # Se n for ímpar, ajustamos para ser par
        n -= 1
        valores = valores[:n+1]

    soma = valores[0] + valores[-1]
    for i in range(1, n):
        soma += 4 * valores[i] if i % 2 == 1 else 2 * valores[i]

    return (h / 3) * soma

# Implementação da Extrapolação de Richardson
def richar(I1: float, I2: float, N1: int, N2: int) -> float:
    p = 4  # Para Simpson 1/3, p = 4
    I_R = I2 + ((N1 ** p * (I2 - I1)) / (N2 ** p - N1 ** p))
    return I_R

def main():
    # Pegando argumentos da linha de comando
    args = sys.argv[1:]

    if len(args) < 4:
        raise ValueError("Número insuficiente de argumentos. Esperado: a, b, valores da função.")

    # Lendo os valores passados pela linha de comando
    a = float(args[0])
    b = float(args[1])
    valores = [float(x) for x in args[2:]]

    N1 = len(valores) - 1  # Número de subintervalos para I1
    N2 = 2 * N1            # Número de subintervalos para I2 (dobro de pontos)
    
    h1 = (b - a) / N1
    h2 = (b - a) / N2

    # Interpolação para obter valores intermediários para N2
    valores_interpolados = []
    for i in range(len(valores) - 1):
        valores_interpolados.append(valores[i])
        valores_interpolados.append((valores[i] + valores[i + 1]) / 2)
    valores_interpolados.append(valores[-1])

    # Cálculo das integrais usando Simpson 1/3
    I1 = simpson_1_3_array(valores, h1)
    I2 = simpson_1_3_array(valores_interpolados, h2)

    # Aplicação da Extrapolação de Richardson
    resultado = richar(I1, I2, N1, N2)
    print(f"Resultado da integral (Extrapolação de Richardson): {resultado}")


if __name__ == "__main__":
    main()
