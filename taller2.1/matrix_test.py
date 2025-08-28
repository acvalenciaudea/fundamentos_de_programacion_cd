from matrix import Matrix

# Crear matrices de prueba
m1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
m2 = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
m3 = Matrix([[1, 0], [0, 1]])  # Matriz identidad 2x2
m4 = Matrix([[2, 1], [1, 3]])  # Matriz simétrica

print("=== CREACIÓN DE MATRICES ===")
print(f"Matriz m1: {m1}")
print(f"Matriz m2: {m2}")
print(f"Matriz m3 (identidad): {m3}")
print(f"Matriz m4 (simétrica): {m4}")

print("\n=== PROPIEDADES DE MATRICES ===")
print(f"Filas de m1: {m1.num_rows}")
print(f"Columnas de m1: {m1.num_columns}")
print(f"m1 es cuadrada: {m1.is_square()}")
print(f"m3 es cuadrada: {m3.is_square()}")
print(f"m4 es simétrica: {m4.is_symmetric()}")

print("\n=== ACCESO A ELEMENTOS ===")
print(f"Elemento (0,0) de m1: {m1[0, 0]}")
print(f"Elemento (1,2) de m1: {m1[1, 2]}")
print(f"Primera fila de m1: {m1[0]}")

print("\n=== OPERACIONES BÁSICAS ===")
# Suma de matrices
suma = m1 + m2
print(f"m1 + m2 = {suma}")

# Resta de matrices
resta = m1 - m2
print(f"m1 - m2 = {resta}")

print("\n=== TRANSPOSICIÓN ===")
print(f"Transpuesta de m1: {m1.T}")
print(f"Transpuesta de m4: {m4.T}")

print("\n=== MULTIPLICACIÓN DE MATRICES ===")
# Crear matrices compatibles para multiplicación
m5 = Matrix([[1, 2], [3, 4], [5, 6]])  # 3x2
m6 = Matrix([[1, 0, 1], [2, 1, 0]])    # 2x3

print("\n=== OBTENER FILAS Y COLUMNAS ===")
fila_1 = m1.get_row(1)
columna_2 = m1.get_column(2)
print(f"Segunda fila de m1: {fila_1}")
print(f"Tercera columna de m1: {columna_2}")

print("\n=== DETERMINANTE ===")
# Matriz 2x2 para calcular determinante
det_matrix = Matrix([[3, 4], [2, 1]])
print(f"Matriz para determinante: {det_matrix}")
print(f"Determinante: {det_matrix.determinant}")

# Matriz 3x3
det_matrix_3x3 = Matrix([[1, 2, 3], [0, 1, 4], [5, 6, 0]])
print(f"Matriz 3x3: {det_matrix_3x3}")
print(f"Determinante 3x3: {det_matrix_3x3.determinant}")

print("\n=== COMPARACIÓN DE MATRICES ===")
m_igual1 = Matrix([[1, 2], [3, 4]])
m_igual2 = Matrix([[1, 2], [3, 4]])
m_diferente = Matrix([[4, 3], [2, 1]])

print(f"m_igual1 == m_igual2: {m_igual1 == m_igual2}")
print(f"m_igual1 == m_diferente: {m_igual1 == m_diferente}")

print("\n=== CASOS ESPECIALES ===")
# Matriz identidad
identidad = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
print(f"Matriz identidad: {identidad}")
print(f"Es simétrica: {identidad.is_symmetric()}")

# Matriz rectangular
rectangular = Matrix([[1, 2, 3, 4], [5, 6, 7, 8]])
print(f"Matriz rectangular: {rectangular}")
print(f"Dimensiones: {rectangular.num_rows}x{rectangular.num_columns}")
print(f"Es cuadrada: {rectangular.is_square()}")

