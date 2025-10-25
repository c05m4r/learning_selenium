#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from math import sqrt
from typing import Tuple


def bhaskara(a: float, b: float, c: float) -> Tuple[float, float]:
    if a == 0:
        raise ValueError("El coeficiente 'a' no puede ser cero")

    dte = b ** 2 - 4 * a * c
    if dte < 0:
        raise ValueError("La ecuación no existen soluciones reales")

    dte_raiz = sqrt(dte)
    den = 2 * a
    x1 = (-b + dte_raiz) / den
    x2 = (-b - dte_raiz) / den
    return x1, x2


if __name__ == "__main__":
    try:
        coef_a = float(input("Ingrese el coeficiente a: "))
        coef_b = float(input("Ingrese el coeficiente b: "))
        coef_c = float(input("Ingrese el coeficiente c: "))
        soluciones = bhaskara(coef_a, coef_b, coef_c)
    except ValueError as exc:
        print(f"Error: {exc}")
    except Exception:
        print(f"Unexpected error: {sys.exc_info()[0]}")
    else:
        x1, x2 = soluciones
        if x1 == x2:
            print(f"La ecuación tiene una raíz doble\n\tx = {x1}")
        else:
            print(f"Las raíces son\n\tx1 = {x1}\n\tx2 = {x2}")
