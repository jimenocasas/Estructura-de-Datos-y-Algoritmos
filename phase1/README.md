# Lista Enlazada Mejorada en Python (SList2)

Este proyecto consiste en la extensión de una lista enlazada simple (`SList`) mediante la creación de una clase derivada llamada `SList2`, que implementa métodos avanzados sobre listas enlazadas. Fue desarrollado como parte de un trabajo práctico de la asignatura de **Estructura de Datos y Algoritmos**.

## Contenido del Proyecto

El archivo principal contiene la definición de la clase `SList2`, que hereda de `SList` e incorpora los siguientes métodos adicionales:

### Métodos implementados

#### 1. `del_largest_seq()`
Elimina la **última** secuencia más larga de elementos consecutivos e idénticos de la lista.  
Modifica la lista original. Si hay múltiples secuencias con la misma longitud máxima, elimina solo la última.

#### 2. `fix_loop()`
Detecta si la lista contiene un **bucle interno** (por ejemplo, si un nodo apunta hacia uno anterior) y lo elimina.  
Devuelve `True` si se detecta y elimina el bucle, `False` si no hay ninguno.

#### 3. `left_right_shift(left, n)`
Realiza un desplazamiento de nodos:
- Si `left` es `True`, mueve los **n primeros** nodos al final de la lista.
- Si `left` es `False`, mueve los **n últimos** nodos al principio.

No realiza ninguna acción si `n` es igual o mayor al tamaño de la lista.

## Dependencias

Este proyecto requiere el archivo `slistH.py` que contiene la implementación base de `SList` y `SNode`.

## Ejecución

Puedes ejecutar el archivo directamente en Python para ver ejemplos de uso de los métodos:

```bash
python phase1.py
