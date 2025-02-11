import sys
import time
import csv
from typing import List

# Nós (t_i) e Pesos (A_i) da Quadratura Gaussiana para n = 5, conforme tabela 5.16
NODES = [
    -0.90617985,  0.90617985,  # t_0 e t_1 (±)
    -0.53846931,  0.53846931,  # t_2 e t_3 (±)
    0.0                          # t_4
]

WEIGHTS = [
    0.23692688, 0.23692688,  # A_0 e A_1
    0.47862868, 0.47862868,  # A_2 e A_3
    0.56888889                # A_4
]

# Implementação da Quadratura Gaussiana com os valores da tabela
def quadratura_gaussiana(a: float, b: float, valores: List[float]) -> float:
    # Mapeamento dos nós para o intervalo [a, b]
    x_mapeado = [(b + a) / 2 + (b - a) / 2 * x for x in NODES]

    # Interpolação linear dos valores da função nos pontos mapeados
    step = (b - a) / (len(valores) - 1)
    f_x_mapeado = []
    for x in x_mapeado:
        i = min(int((x - a) / step), len(valores) - 2)  # Índice do ponto mais próximo
        x1, x2 = a + i * step, a + (i + 1) * step
        y1, y2 = valores[i], valores[i + 1]
        f_x_mapeado.append(y1 + (y2 - y1) * (x - x1) / (x2 - x1))  # Interpolação linear

    # Cálculo da integral pela fórmula da Quadratura Gaussiana
    integral = (b - a) / 2 * sum(w * f for w, f in zip(WEIGHTS, f_x_mapeado))
    return integral

def main():
    # Pegando argumentos da linha de comando
    args = sys.argv[1:]

    if len(args) < 3:
        raise ValueError("Número insuficiente de argumentos. Esperado: a, b, valores da função.")

    # Lendo os valores passados pela linha de comando
    a = float(args[0])
    b = float(args[1])
    valores = [float(x) for x in args[2:]]

    resultado = quadratura_gaussiana(a, b, valores)

    print(f"Resultado da integral (Quadratura Gaussiana, 5 pontos da Tabela 5.16): {resultado}")

if __name__ == "__main__":
    main()
