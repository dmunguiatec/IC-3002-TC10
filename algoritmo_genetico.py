from typing import List

from dominio_tsp import DominioTSP

def optimizar(dominio: DominioTSP, tam_pobl: int, porc_elite: float, prob_mut: float, reps: int) -> List[int]:
    """Algoritmo genético para optimización estocástica.

    Entradas:
    dominio (Dominio)
        Un objeto que modela el dominio del problema que se quiere aproximar.

    tam_pobl (int)
        Tamaño de la población.

    porc_elite (float)
        Porcentaje de la población que se tomará como elite.

    prob_mut (float)
        Probabilidad de mutación, debe estar en el rango [0, 1]

    reps (int)
        Número de iteraciones a ejecutar.

    Salidas:
        (T) Estructura de datos según el dominio, que representa una
        aproximación a la mejor solución al problema.
    """

    raise NotImplementedError()
