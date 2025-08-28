import math
from typing import List, Union


class Vector:
    """
    Clase para representar y manipular vectores.

    Un vector es una lista de números que puede representar
    puntos en el espacio, direcciones, o cualquier secuencia ordenada de valores.
    """

    components: List[Union[int, float]] = []

    def __init__(self, components: List[Union[int, float]]):
        """
        Inicializa un vector con sus componentes.

        Args:
            components: Lista de números que representan las componentes del vector
        """
        self.components = components

    def __str__(self) -> str:
        """Representación en string del vector."""
        return f"Vector:({self.components})"

    def __repr__(self) -> str:
        """Representación detallada del vector."""
        return f"Vector:({self.components})"

    def __len__(self) -> int:
        """Retorna la dimensión del vector."""
        pass

    def __getitem__(self, index: int) -> Union[int, float]:
        """Permite acceder a los componentes del vector usando índices."""
        return self.components[index]

    def __setitem__(self, index: int, value: Union[int, float]):
        """Permite modificar componentes del vector usando índices."""
        self.components[index] = value

    def __add__(self, other: "Vector") -> "Vector":
        """Suma de vectores usando el operador +."""
        if len(self.components) != len(other.components):
            raise ValueError("Los vectores deben tener la misma dimensión")
        return Vector([x + y for x, y in zip(self.components, other.components)])

    def __sub__(self, other: "Vector") -> "Vector":
        """Resta de vectores usando el operador -."""
        if len(self.components) != len(other.components):
            raise ValueError("Los vectores deben tener la misma dimensión")
        return Vector([x - y for x, y in zip(self.components, other.components)])

    def __mul__(self, scalar: Union[int, float]) -> "Vector":
        """Multiplicación por escalar usando el operador *."""
        return Vector([x * scalar for x in self.components])

    def __rmul__(self, scalar: Union[int, float]) -> "Vector":
        """Multiplicación por escalar (orden invertido)."""
        inverse_components = self.components[::-1]
        return Vector([x * scalar for x in inverse_components])

    def __truediv__(self, scalar: Union[int, float]) -> "Vector":
        """División por escalar usando el operador /."""
        return Vector([x / scalar for x in self.components])

    def __eq__(self, other: "Vector") -> bool:
        """Igualdad entre vectores usando el operador ==."""
        return self.components == other.components

    def __ne__(self, other: "Vector") -> bool:
        """Desigualdad entre vectores usando el operador !=."""
        return self.components != other.components

    @property 
    def magnitude(self) -> float:
        """Calcula y retorna la magnitud (norma) del vector."""
        return math.sqrt(sum(x ** 2 for x in self.components))

    @property
    def unit_vector(self) -> "Vector":
        """Retorna el vector unitario (normalizado)."""
        return Vector([x / self.magnitude for x in self.components])

    def dot(self, other: "Vector") -> float:
        """
        Calcula el producto punto con otro vector.

        Args:
            other: Otro vector para el producto punto

        Returns:
            El producto punto como un número
        """
        return sum(x * y for x, y in zip(self.components, other.components))

    def cross(self, other: "Vector") -> "Vector":
        """
        Calcula el producto cruz con otro vector (solo para vectores 3D).

        Args:
            other: Otro vector para el producto cruz

        Returns:
            Un nuevo vector resultado del producto cruz
        """
        if len(self.components) != 3 or len(other.components) != 3:
            raise ValueError("Los vectores deben tener 3 dimensiones")
        return Vector([
            self.components[1] * other.components[2] - self.components[2] * other.components[1],
            self.components[2] * other.components[0] - self.components[0] * other.components[2],
            self.components[0] * other.components[1] - self.components[1] * other.components[0]
        ])

    def angle_with(self, other: "Vector") -> float:
        """
        Calcula el ángulo entre este vector y otro.

        Args:
            other: Otro vector

        Returns:
            El ángulo en radianes
        """
        # 1. Obtener producto punto
        dot_product = self.dot(other)
        
        # 2. Obtener magnitud del otro vector
        other_magnitude = other.magnitude
        magnitude_product = self.magnitude * other_magnitude
        
        # 3. Calcular el coseno del ángulo
        cos_angle = dot_product / magnitude_product
        
        # 4. Calcular el ángulo en radianes
        return math.acos(cos_angle)


# =============================================================================
# FUNCIONES DE VECTOR
# =============================================================================

def dot_product(v1: Vector, v2: Vector) -> float:
    """
    Calcula el producto punto entre dos vectores.
    
    Args:
        v1: Primer vector
        v2: Segundo vector
        
    Returns:
        El producto punto como un número
    """
    return v1.dot(v2)


def magnitude(v: Vector) -> float:
    """
    Calcula la magnitud (norma) de un vector.
    
    Args:
        v: El vector
        
    Returns:
        La magnitud del vector
    """
    return v.magnitude


def normalize(v: Vector) -> Vector:
    """
    Normaliza un vector (lo convierte en vector unitario).
    
    Args:
        v: El vector a normalizar
        
    Returns:
        Un nuevo vector normalizado
    """
    return v.unit_vector


def cross_product(v1: Vector, v2: Vector) -> Vector:
    """
    Calcula el producto cruz entre dos vectores 3D.
    
    Args:
        v1: Primer vector
        v2: Segundo vector
        
    Returns:
        Un nuevo vector resultado del producto cruz
    """
    return v1.cross(v2)


def angle_between(v1: Vector, v2: Vector) -> float:
    """
    Calcula el ángulo entre dos vectores.
    
    Args:
        v1: Primer vector
        v2: Segundo vector
        
    Returns:
        El ángulo en radianes
    """
    return v1.angle_with(v2)
