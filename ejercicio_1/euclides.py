#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys


class Euclides:
    def __init__(self):
        self.clear = lambda: os.system("cls" if os.name in ("nt", "dos") else "clear")
        self.str_resto = ""
        self.str_divisor = ""
        self.mcd = 0
        self.mcm = 0
        self.coprimos = False

    def division(self, a: int, b: int):
        "Realiza el algoritmo de la division"
        dividendo = max(a, b)
        divisor = min(a, b)
        self.mcm = a * b
        self.mcd = divisor
        resto = 1
        while resto > 0:
            cociente = dividendo // divisor
            resto = dividendo % divisor
            if resto != 0:
                self.str_resto += (
                    f"{resto} = {dividendo} + {divisor}({(-1) * cociente})\n"
                )
                self.mcd = resto
            self.str_divisor += f"{dividendo} = {divisor}({cociente}) + {resto}\n"
            dividendo = divisor
            divisor = resto
        self.mcm //= self.mcd
        if self.mcd == 1:
            self.coprimos = True


if __name__ == "__main__":
    obj = Euclides()
    obj.clear()

    try:
        n1 = int(input("Ingrese dividendo:\n"))
        n2 = int(input("Ingrese divisor:\n"))
        assert isinstance(n1, int) and isinstance(n2, int)
    except AssertionError:
        print(f"Por favor ingrese los valores nuevamente")
    except:
        print(f"Unexpected error: {sys.exc_info()[0]}")
    else:
        obj.division(n1, n2)
        print(f"Algoritmo de la División:")
        print(f"{obj.str_divisor}")
        print(f"Ordenando los restos:")
        print(f"{obj.str_resto}")
        print(f"Maximo Comun Divisor: {obj.mcd}")
        print(f"Minimo Comun Multiplo: {obj.mcm}")
        print(f"Coprimos o Primos Relativos: {obj.coprimos}")
