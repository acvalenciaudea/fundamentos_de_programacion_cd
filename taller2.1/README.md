# Taller 2.1
# Álgebra Lineal: Vectores y Matrices
# Especialización en Analítica y Ciencia de Datos
# Universidad de Antioquia

Este directorio contiene implementaciones en Python para operaciones básicas de álgebra lineal con vectores y matrices.

## Contenido

- `vector.py` - Implementación de la clase Vector y funciones relacionadas
- `matrix.py` - Implementación de la clase Matrix y funciones relacionadas
- `vector_test.py` - Pruebas unitarias para la clase Vector
- `matrix_test.py` - Pruebas unitarias para la clase Matrix
- `vector_test.ipynb` - Notebook con ejemplos y pruebas de vectores
- `matrix_test.ipynb` - Notebook con ejemplos y pruebas de matrices

## Características

### Clase Vector
La clase `Vector` permite trabajar con vectores de cualquier dimensión e incluye:

#### Operaciones básicas:
- Suma (`+`) y resta (`-`) de vectores
- Multiplicación por escalar (`*`)
- División por escalar (`/`)
- Acceso a componentes por índice (`[]`)

#### Métodos de cálculo:
- `magnitude()` - Calcula la magnitud (norma) del vector
- `unit_vector()` - Retorna el vector unitario
- `dot(other)` - Producto punto con otro vector
- `cross(other)` - Producto cruz (solo para vectores 3D)
- `angle_with(other)` - Ángulo entre dos vectores

#### Funciones standalone:
- `dot_product(v1, v2)` - Producto punto entre dos vectores
- `magnitude(v)` - Magnitud de un vector
- `normalize(v)` - Normalización de un vector
- `cross_product(v1, v2)` - Producto cruz entre dos vectores
- `angle_between(v1, v2)` - Ángulo entre dos vectores

### Clase Matrix
La clase `Matrix` permite trabajar con matrices de cualquier tamaño e incluye:

#### Operaciones básicas:
- Suma (`+`) y resta (`-`) de matrices
- Multiplicación por escalar y por matriz (`*`)
- Acceso a elementos y filas por índice (`[]`)
- Igualdad (`==`) y desigualdad (`!=`)

#### Propiedades:
- `num_rows()` - Número de filas
- `num_columns()` - Número de columnas
- `shape()` - Dimensiones (filas, columnas)
- `T()` - Matriz transpuesta
- `trace()` - Traza de la matriz
- `determinant()` - Determinante
- `inverse()` - Matriz inversa

#### Métodos de verificación:
- `is_square()` - Verifica si es matriz cuadrada
- `is_symmetric()` - Verifica si es matriz simétrica
- `is_diagonal()` - Verifica si es matriz diagonal

#### Acceso a filas y columnas:
- `get_row(index)` - Obtiene una fila como Vector
- `get_column(index)` - Obtiene una columna como Vector

#### Funciones standalone:
- `scale(matrix, scalar)` - Escalado de matriz
- `add(m1, m2)` - Suma de matrices
- `subtract(m1, m2)` - Resta de matrices
- `vector_multiply(matrix, vector)` - Multiplicación matriz-vector
- `matrix_multiply(m1, m2)` - Multiplicación matriz-matriz
- `transpose(matrix)` - Transposición
- `determinant(matrix)` - Determinante
- `inverse(matrix)` - Matriz inversa
- `identity_matrix(size)` - Matriz identidad
- `zeros_matrix(rows, cols)` - Matriz de ceros
- `ones_matrix(rows, cols)` - Matriz de unos

## Uso básico

### Vectores
```python
from vector import Vector

# Crear vectores
v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6])

# Operaciones básicas
suma = v1 + v2          # Vector([5, 7, 9])
producto_escalar = v1 * 2  # Vector([2, 4, 6])

# Cálculos
magnitud = v1.magnitude()
producto_punto = v1.dot(v2)
angulo = v1.angle_with(v2)
```

### Matrices
```python
from matrix import Matrix

# Crear matrices
m1 = Matrix([[1, 2], [3, 4]])
m2 = Matrix([[5, 6], [7, 8]])

# Operaciones básicas
suma = m1 + m2          # Matrix([[6, 8], [10, 12]])
producto = m1 * m2      # Multiplicación de matrices

# Propiedades
transpuesta = m1.T()
determinante = m1.determinant()
inversa = m1.inverse()
```

## Pruebas

Para ejecutar las pruebas:

```bash
# Pruebas de vectores
python vector_test.py

# Pruebas de matrices  
python matrix_test.py
```

También puedes usar los notebooks interactivos:
- `vector_test.ipynb` - Ejemplos y pruebas de vectores
- `matrix_test.ipynb` - Ejemplos y pruebas de matrices

## Requisitos

- Python 3.6+
- Módulo `math` (incluido en Python estándar)
- Módulo `typing` (incluido en Python estándar)