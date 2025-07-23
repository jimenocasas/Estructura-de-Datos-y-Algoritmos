#  Estructura de Datos y Algoritmos

Un repositorio completo que implementa estructuras de datos avanzadas y algoritmos eficientes en Python, desarrollado como parte de la asignatura **Estructura de Datos y Algoritmos**.

## Descripción del Proyecto

Este proyecto está dividido en **dos fases principales**, cada una enfocada en diferentes aspectos fundamentales de las estructuras de datos:

### **Phase 1: Listas Enlazadas Avanzadas** 
Extensión y mejora de listas enlazadas simples con funcionalidades avanzadas.

### **Phase 2: Árboles Binarios de Búsqueda** 
Implementación de operaciones complejas sobre árboles binarios de búsqueda y estructuras relacionadas.

---

## Estructura del Repositorio

```
Estructura-de-Datos-y-Algoritmos/
├── phase1/                     # Listas Enlazadas Avanzadas
│   ├── phase1.py              # Implementación principal (SList2)
│   ├── phase1_unittest.py     # Casos de prueba unitarios
│   ├── slistH.py              # Clase base SList y SNode
│   └── README.md              # Documentación específica
│
├── phase2/                     # Árboles Binarios de Búsqueda
│   ├── phase2.py              # Implementación BST2 y operaciones
│   ├── test_unittest.py       # Casos de prueba unitarios
│   ├── bst.py                 # Árbol binario de búsqueda base
│   ├── bintree.py             # Implementación de árbol binario
│   ├── dlist.py               # Lista doblemente enlazada
│   └── README.md              # Documentación específica
│
└── README.md                   # Este archivo
```

---

## Phase 1: Listas Enlazadas Avanzadas

### Características Principales

La clase `SList2` extiende la funcionalidad de listas enlazadas simples con:

#### **Métodos Implementados**

| Método | Descripción | Complejidad |
|--------|-------------|-------------|
| `del_largest_seq()` | Elimina la secuencia más larga de elementos idénticos consecutivos | O(n) |
| `fix_loop()` | Detecta y elimina bucles internos en la lista | O(n²) |
| `left_right_shift(left, n)` | Desplaza n nodos al inicio o final según el parámetro left | O(n) |

#### **Casos de Uso**
- **Limpieza de datos**: Eliminación de secuencias redundantes
- **Detección de ciclos**: Validación de integridad estructural
- **Manipulación eficiente**: Rotación de elementos sin recrear la lista

---

## Phase 2: Árboles Binarios de Búsqueda

### Características Principales

La clase `BST2` implementa operaciones avanzadas sobre árboles binarios:

#### **Métodos Implementados**

| Método | Descripción | Complejidad |
|--------|-------------|-------------|
| `find_dist_k(n, k)` | Encuentra todos los nodos a distancia k del nodo n | O(n) |
| `create_tree(tree1, tree2, op)` | Operaciones entre árboles: merge, intersection, difference | O(n + m) |

#### **Operaciones entre Árboles**
- **Merge**: Unión de dos árboles sin duplicados
- **Intersection**: Elementos comunes entre dos árboles  
- **Difference**: Elementos del primer árbol que no están en el segundo

#### **Estructuras Auxiliares**
- **Lista doblemente enlazada** (`DList`): Para operaciones eficientes O(1)
- **Nodos binarios** (`BinaryNode`): Implementación robusta de nodos
- **Árbol binario base** (`BinaryTree`): Funcionalidades de traversal y visualización

---

## Instalación y Uso

### Prerrequisitos
- Python 3.6 o superior
- No requiere dependencias externas

### Ejecución

#### Phase 1 - Listas Enlazadas
```bash
# Ejecutar ejemplos
cd phase1
python phase1.py

# Ejecutar tests
python phase1_unittest.py
```

#### Phase 2 - Árboles BST  
```bash
# Ejecutar ejemplos
cd phase2
python phase2.py

# Ejecutar tests
python test_unittest.py
```

---

## Testing

Ambas fases incluyen **suites de pruebas unitarias** exhaustivas:

- **Phase 1**: 15+ casos de prueba cubriendo escenarios edge y casos normales
- **Phase 2**: 20+ casos de prueba para operaciones entre árboles

```bash
# Ejecutar todos los tests
python -m unittest discover -s phase1 -p "*unittest.py"
python -m unittest discover -s phase2 -p "*unittest.py"
```

---

## Análisis de Complejidad

### Phase 1 - Listas Enlazadas
| Operación | Tiempo | Espacio | Observaciones |
|-----------|--------|---------|---------------|
| del_largest_seq | O(n) | O(1) | Recorrido único optimizado |
| fix_loop | O(n²) | O(1) | Detección de ciclos sin espacio extra |
| left_right_shift | O(n) | O(1) | Manipulación de punteros in-place |

### Phase 2 - Árboles BST
| Operación | Tiempo | Espacio | Observaciones |
|-----------|--------|---------|---------------|
| find_dist_k | O(n) | O(h) | Donde h es la altura del árbol |
| merge | O(n + m) | O(n + m) | n, m = tamaños de los árboles |
| intersection | O(n × m) | O(min(n,m)) | Optimizable con hash sets |
| difference | O(n × m) | O(n) | Búsquedas en árbol objetivo |

---

## Características Destacadas

- **Código limpio y documentado**: Comentarios detallados y estructura clara
- **Testing exhaustivo**: Casos edge y validación completa
- **Optimización de memoria**: Algoritmos in-place cuando es posible
- **Visualización**: Métodos de debug y representación visual de estructuras
- **Robustez**: Manejo de errores y validaciones de entrada

---

## Autor

**Miguel Jimeno Casas**
- GitHub: [@jimenocasas](https://github.com/jimenocasas)
- Proyecto: Estructura de Datos y Algoritmos - Universidad

---
