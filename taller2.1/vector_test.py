from vector import Vector

# Crear vectores de prueba
v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6])
v3 = Vector([2, 0, -1])

print("=== CREACIÓN DE VECTORES ===")
print(f"Vector v1: {v1}")
print(f"Vector v2: {v2}")
print(f"Vector v3: {v3}")

print("\n=== ACCESO A COMPONENTES ===")
print(f"Primera componente de v1: {v1[0]}")
print(f"Segunda componente de v2: {v2[1]}")
print(f"Tercera componente de v3: {v3[2]}")

print("\n=== OPERACIONES BÁSICAS ===")
# Suma de vectores
suma = v1 + v2
print(f"v1 + v2 = {suma}")

# Resta de vectores
resta = v2 - v1
print(f"v2 - v1 = {resta}")

# Multiplicación por escalar
escalar = v1 * 3
print(f"v1 * 3 = {escalar}")

# División por escalar
division = v2 / 2
print(f"v2 / 2 = {division}")

print("\n=== PROPIEDADES DEL VECTOR ===")
# Magnitud
print(f"Magnitud de v1: {v1.magnitude}")
print(f"Magnitud de v2: {v2.magnitude}")
print(f"Magnitud de v3: {v3.magnitude}")

# Vector unitario
unitario_v1 = v1.unit_vector
print(f"Vector unitario de v1: {unitario_v1}")
print(f"Magnitud del vector unitario: {unitario_v1.magnitude:.3f}")

print("\n=== PRODUCTO PUNTO ===")
producto_punto = v1.dot(v2)
print(f"v1 · v2 = {producto_punto}")

producto_punto_v3 = v1.dot(v3)
print(f"v1 · v3 = {producto_punto_v3}")

print("\n=== PRODUCTO CRUZ (VECTORES 3D) ===")
producto_cruz = v1.cross(v2)
print(f"v1 × v2 = {producto_cruz}")

# Verificar que el producto cruz es perpendicular
print(f"(v1 × v2) · v1 = {producto_cruz.dot(v1)} (debe ser ≈ 0)")
print(f"(v1 × v2) · v2 = {producto_cruz.dot(v2)} (debe ser ≈ 0)")

print("\n=== ÁNGULO ENTRE VECTORES ===")
import math

angulo_v1_v2 = v1.angle_with(v2)
print(f"Ángulo entre v1 y v2: {angulo_v1_v2:.3f} radianes ({math.degrees(angulo_v1_v2):.1f} grados)")

angulo_v1_v3 = v1.angle_with(v3)
print(f"Ángulo entre v1 y v3: {angulo_v1_v3:.3f} radianes ({math.degrees(angulo_v1_v3):.1f} grados)")

print("\n=== VECTORES ORTOGONALES ===")
# Crear vectores ortogonales
v_ortogonal1 = Vector([1, 0, 0])
v_ortogonal2 = Vector([0, 1, 0])

print(f"Vector ortogonal 1: {v_ortogonal1}")
print(f"Vector ortogonal 2: {v_ortogonal2}")
print(f"Producto punto: {v_ortogonal1.dot(v_ortogonal2)} (debe ser 0)")
angulo_ortogonal = v_ortogonal1.angle_with(v_ortogonal2)
print(f"Ángulo: {angulo_ortogonal:.3f} radianes ({math.degrees(angulo_ortogonal):.1f} grados)")

print("\n=== VECTORES PARALELOS ===")
v_paralelo1 = Vector([2, 4, 6])
v_paralelo2 = Vector([1, 2, 3])

print(f"Vector paralelo 1: {v_paralelo1}")
print(f"Vector paralelo 2: {v_paralelo2}")
producto_cruz_paralelo = v_paralelo1.cross(v_paralelo2)
print(f"Producto cruz: {producto_cruz_paralelo} (debe ser vector nulo)")
angulo_paralelo = v_paralelo1.angle_with(v_paralelo2)
print(f"Ángulo: {angulo_paralelo:.3f} radianes ({math.degrees(angulo_paralelo):.1f} grados)")

print("\n=== MODIFICACIÓN DE COMPONENTES ===")
v_modificable = Vector([1, 1, 1])
print(f"Vector original: {v_modificable}")

v_modificable[1] = 5
print(f"Después de modificar segunda componente: {v_modificable}")

print("\n=== COMPARACIÓN DE VECTORES ===")
v_igual1 = Vector([1, 2, 3])
v_igual2 = Vector([1, 2, 3])
v_diferente = Vector([3, 2, 1])

print(f"v_igual1 == v_igual2: {v_igual1 == v_igual2}")
print(f"v_igual1 == v_diferente: {v_igual1 == v_diferente}")
print(f"v_igual1 != v_diferente: {v_igual1 != v_diferente}")

print("\n=== CASOS ESPECIALES ===")
# Vector cero
vector_cero = Vector([0, 0, 0])
print(f"Vector cero: {vector_cero}")
print(f"Magnitud del vector cero: {vector_cero.magnitude}")

# Vector en 2D
vector_2d = Vector([3, 4])
print(f"Vector 2D: {vector_2d}")
print(f"Magnitud: {vector_2d.magnitude}")
print(f"Vector unitario: {vector_2d.unit_vector}")
