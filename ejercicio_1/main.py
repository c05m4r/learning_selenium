#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from typing import Optional, Tuple
from math import sqrt
from euclides import Euclides


def es_primo(num: int) -> Tuple[bool, Optional[int]]:
    abs_num = abs(num)
    if abs_num <= 1:
        return False, None
    if abs_num == 2:
        return True, None
    if abs_num % 2 == 0:
        return False, 2

    limite = int(sqrt(abs_num)) + 1
    for i in range(3, limite, 2):
        if abs_num % i == 0:
            return False, i
    return True, None


if __name__ == "__main__":
    try:
        numero = int(input("Ingrese un número entero: "))
        assert isinstance(numero, int)
    except AssertionError:
        print(f"Por favor ingrese los valores nuevamente")
    except:
        print(f"Unexpected error: {sys.exc_info()[0]}")
    else:
        es_primo_flag, divisor = es_primo(numero)
        if es_primo_flag:
            print(f"El número {numero} es primo.")
        else:
            obj = Euclides()
            obj.clear()
            obj.division(numero, divisor)
            print(f"El número {numero} NO es primo.")
            print(f"Algoritmo de la División:")
            print(f"{obj.str_divisor}")
            print(f"Ordenando los restos:")
            print(f"{obj.str_resto}")
