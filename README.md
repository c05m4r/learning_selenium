# Ejercicio integrador

## Punto 1
Escribir un programa que dado el ingreso de un número retorne si el mismo es primo o no.

***

## Punto 2
Escribir una función que dado el ingreso de 3 variables ($a$, $b$, $c$) retorne las raíces resultantes de una ecuación cuadrática.

**Ecuación de segundo grado o Cuadrática**
$$ax^2+bx+c=0$$
La fórmula para encontrar las raíces ($x$) es:
$$x = \frac{-b \pm \sqrt{b^2-4ac}}{2a}$$

***

## Punto 3
Automatizar los siguientes casos de prueba. Luego de que sean automatizados, deben ser subidos a un repositorio git, se debe generar el archivo y debe retornar un reporte HTML con los resultados de la ejecución.

### Sitio: https://www.saucedemo.com/

#### Caso 1
1.  El usuario se loguea al sitio como usuario **standard user**.
2.  Ordenar los elementos por "price (low to high)".
3.  Verificar que los elementos estén ordenados.

#### Caso 2
1.  El usuario se loguea al sitio como usuario **standard user**.
2.  Incorporar al carrito todos los elementos.
3.  Ir al carrito.
4.  Verificar que todos los elementos están en el carrito.
5.  Ir al checkout.
6.  Ingresar nombre y clickear **Continue**.
7.  Verificar que aparece el error "Error: Last Name is required".
8.  Ingresar un apellido y clickear **Continue**.
9.  Verificar que aparece el error "Error: Postal Code is required".

#### Caso 3
1.  El usuario se loguea al sitio como usuario **standard user**.
2.  Agregar un elemento al carrito.
3.  Ir al carrito.
4.  Remover el artículo.
5.  Verificar que el sitio no tiene artículos agregados.
6.  Ir a **Continue Shopping**.
7.  Agregar dos elementos.
8.  Ir al carrito.
9.  Verificar que los elementos existen.
10. Hacer el checkout.
11. Finalizar la compra.
12. Verificar que la compra fue realizada.

***

### Sitio: Poke Api (https://pokeapi.co/api/v2)

#### Caso 1
1.  Hacer un `get` a `berry/1`.
2.  Verificar que el `size` sea **20**.
3.  Verificar que el `soil_dryness` sea **15**.
4.  Verificar que en `firmness`, el `name` sea **soft**.

#### Caso 2
1.  Hacer un `get` a `berry/2`.
2.  Verificar que el `size` sea **mayor al punto anterior**.
3.  Verificar que el `soil_dryness` sea **igual al punto anterior**.
4.  Verificar que en `firmness`, el `name` sea **super-hard**.

#### Caso 3
1.  Hacer un `get` a `https://pokeapi.co/api/v2/pokemon/pikachu/`.
2.  Verificar que su experiencia base es mayor a 10 y menor a 1000.
3.  Verificar que su tipo es “electric”

# FAQ

## ¿Como ejecutar tests?

1. Instalar [UV](https://docs.astral.sh/uv/getting-started/installation/)
2. Resolver dependencias con 

    ```bash
    uv sync
    ```

3. Ejecutar código

    ```bash
    uv run ejercicio_1/main.py
    ```

    ```bash
    uv run ejercicio_2/main.py
    ```

4. Ejecutar pruebas con pytest, ejecutar dentro de carpeta ejercicio_3

    1. Desde la etiqueta por caso de prueba

    ```bash
    uv run pytest --html=report.html
    uv run pytest -m tc1
    uv run pytest -m tc2
    uv run pytest -m tc3
    uv run pytest -m pokeapi_tc1
    uv run pytest -m pokeapi_tc2
    uv run pytest -m pokeapi_tc3
    ```

    2. Desde la etiqueta por sitio

    ```bash
    uv run pytest -m saucedemo
    uv run pytest -m pokeapi
    ```

    3. Desde el archivo

    ```bash
    uv run pytest ejercicio_3/tests/saucedemo/login_standard_user_test.py
    ```

## ¿Cómo ejecutar en modo debug?

```bash
 uv run pytest -m tc1 -v --trace
```

```bash
 uv run pytest ejercicio_3/tests/saucedemo/login_user_test.py -v --trace
```

Luego usar segun corresponda

```
n (next) avanza a la siguiente línea de la función actual
s (step) entra en la siguiente llamada (como n pero detallado)
c (continue) reanuda hasta el próximo breakpoint o el final
l (list) muestra el código alrededor de la posición actual
p expr (print) imprime el valor de una expresión
b archivo.py:línea (breakpoint) define un breakpoint adicional
q (quit) sale del depurador y aborta la ejecución
```

## ¿Cómo configuro un breakpoint?

De este modo al presionar c en el modo depuración se detendrá en el breakpoint para que podamos analizar el comportamiento

```python
import pdb
# codigo de interés
pdb.set_trace()
```

## ¿Cómo ordenar el código usando el linter ruff?

Posicionarse en la carpeta raiz y ejecutar

```python
uvx ruff format
```
