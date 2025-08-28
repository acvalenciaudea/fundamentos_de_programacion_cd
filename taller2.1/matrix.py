import math
from typing import List, Union, Tuple, Optional
from vector import Vector


class Matrix:
    """
    Clase para representar y manipular matrices.

    Una matriz es una colección rectangular de números organizados en filas y columnas.
    """

    data: List[List[Union[int, float]]] = []

    def __init__(self, data: List[List[Union[int, float]]]):
        """
        Inicializa una matriz con sus datos.

        Args:
            data: Lista de listas que representa las filas de la matriz
        """
        self.data = data

    def __str__(self) -> str:
        """Representación en string de la matriz."""
        return f"Matrix: {self.data}"

    def __repr__(self) -> str:
        """Representación detallada de la matriz."""
        return f"Matrix: {self.data}"

    def __getitem__(
        self, key: Union[int, Tuple[int, int]]
    ) -> Union[List[Union[int, float]], Union[int, float]]:
        """Permite acceder a filas o elementos específicos de la matriz."""
        if isinstance(key, int):
            return self.data[key]
        elif isinstance(key, tuple):
            row, col = key
            return self.data[row][col]
        else:
            raise ValueError("Key must be an integer or a tuple of two integers")

    def __setitem__(
        self,
        key: Union[int, Tuple[int, int]],
        value: Union[List[Union[int, float]], Union[int, float]],
    ):
        """Permite modificar filas o elementos específicos de la matriz."""
        if isinstance(key, int):
            self.data[key] = value
        elif isinstance(key, tuple):
            row, col = key
            self.data[row][col] = value
        else:
            raise ValueError("Key must be an integer or a tuple of two integers")

    def __add__(self, other: "Matrix") -> "Matrix":
        """Suma de matrices usando el operador +."""
        if self.shape != other.shape:
            raise ValueError("Matrices must have the same shape")
        return Matrix(
            [
                [x + y for x, y in zip(row1, row2)]
                for row1, row2 in zip(self.data, other.data)
            ]
        )

    def __sub__(self, other: "Matrix") -> "Matrix":
        """Resta de matrices usando el operador -."""
        if self.shape != other.shape:
            raise ValueError("Matrices must have the same shape")
        return Matrix(
            [
                [x - y for x, y in zip(row1, row2)]
                for row1, row2 in zip(self.data, other.data)
            ]
        )

    def __mul__(
        self, other: Union["Matrix", "Vector", int, float]
    ) -> Union["Matrix", "Vector"]:
        """Multiplicación de matrices/vectores/escalares usando el operador *."""
        if isinstance(other, Matrix):
            if self.num_columns != other.num_rows:
                raise ValueError(
                    "The number of columns of the first matrix must be equal to the number of rows of the second matrix"
                )
            if self.num_rows != other.num_rows:
                raise ValueError(
                    "The number of rows of the first matrix must be equal to the number of rows of the second matrix"
                )

            result = []
            for i in range(self.num_rows):
                row = []
                for j in range(other.num_columns):
                    row.append(
                        sum(
                            x * y
                            for x, y in zip(
                                self.data[i], [row[j] for row in other.data]
                            )
                        )
                    )
                result.append(row)
            return Matrix(result)
        else:
            raise ValueError("Invalid type for multiplication")

    def __eq__(self, other: "Matrix") -> bool:
        """Igualdad entre matrices usando el operador ==."""
        return self.data == other.data

    def __ne__(self, other: "Matrix") -> bool:
        """Desigualdad entre matrices usando el operador !=."""
        return self.data != other.data

    @property
    def num_rows(self) -> int:
        """Retorna el número de filas de la matriz."""
        return len(self.data)

    @property
    def num_columns(self) -> int:
        """Retorna el número de columnas de la matriz."""
        return len(self.data[0])

    @property
    def shape(self) -> Tuple[int, int]:
        """Retorna las dimensiones de la matriz como (filas, columnas)."""
        return (self.num_rows, self.num_columns)

    @property
    def T(self) -> "Matrix":
        """Retorna la transpuesta de la matriz."""
        return Matrix(
            [
                [self.data[j][i] for j in range(self.num_rows)]
                for i in range(self.num_columns)
            ]
        )

    @property
    def trace(self) -> Union[int, float]:
        """Calcula y retorna la traza de la matriz (suma de elementos diagonales)."""
        if not self.is_square():
            raise ValueError("La matriz debe ser cuadrada para calcular la traza")

        return sum(self.data[i][i] for i in range(self.num_rows))

    @property
    def determinant(self) -> Union[int, float]:
        """Calcula y retorna el determinante de la matriz."""

        def calc_determinant(matriz: "Matrix") -> Union[int, float]:
            if not matriz.is_square():
                raise ValueError(
                    "La matriz debe ser cuadrada para calcular el determinante"
                )

            if matriz.num_rows == 0:
                return 1

            if matriz.num_rows == 1:
                return matriz.data[0][0]

            if matriz.num_rows == 2:
                return (
                    matriz.data[0][0] * matriz.data[1][1]
                    - matriz.data[0][1] * matriz.data[1][0]
                )

            # determinante de una matriz nxn recursivo
            total = 0
            n = matriz.num_rows
            for j in range(n):
                # Crear la submatriz eliminando la fila 0 y la columna j
                submatriz = []
                for i in range(1, n):  # Omitir la primera fila
                    fila_sub = []
                    for k in range(n):
                        if k != j:  # Omitir la columna j
                            fila_sub.append(matriz[i][k])
                    submatriz.append(fila_sub)

                # Calcular el cofactor: (-1)^(0+j) * elemento * determinante de submatriz
                cofactor = ((-1) ** j) * matriz[0][j] * calc_determinant(Matrix(submatriz))
                total += cofactor

            return total

        return calc_determinant(self)

    @property
    def inverse(self) -> "Matrix":
        """Calcula y retorna la matriz inversa."""
        pass

    def is_square(self) -> bool:
        """Verifica si la matriz es cuadrada."""
        return self.num_rows == self.num_columns

    def is_symmetric(self) -> bool:
        """Verifica si la matriz es simétrica."""
        return self.data == self.T.data

    def is_diagonal(self) -> bool:
        """Verifica si la matriz es diagonal."""
        pass

    def get_row(self, index: int) -> "Vector":
        """
        Obtiene una fila específica como vector.

        Args:
            index: Índice de la fila

        Returns:
            Vector con los elementos de la fila
        """
        return Vector(self.data[index])

    def get_column(self, index: int) -> "Vector":
        """
        Obtiene una columna específica como vector.

        Args:
            index: Índice de la columna

        Returns:
            Vector con los elementos de la columna
        """
        return Vector([self.data[i][index] for i in range(self.num_rows)])


# =============================================================================
# FUNCIONES DE MATRIZ
# =============================================================================


def scale(matrix: Matrix, scalar: Union[int, float]) -> Matrix:
    """
    Multiplica una matriz por un escalar.

    Args:
        matrix: La matriz
        scalar: El escalar

    Returns:
        Una nueva matriz escalada
    """
    return Matrix([[x * scalar for x in row] for row in matrix.data])


def add(m1: Matrix, m2: Matrix) -> Matrix:
    """
    Suma dos matrices.

    Args:
        m1: Primera matriz
        m2: Segunda matriz

    Returns:
        Una nueva matriz resultado de la suma
    """
    return m1 + m2


def subtract(m1: Matrix, m2: Matrix) -> Matrix:
    """
    Resta dos matrices.

    Args:
        m1: Primera matriz
        m2: Segunda matriz

    Returns:
        Una nueva matriz resultado de la resta
    """
    return m1 - m2


def vector_multiply(matrix: Matrix, vector: Vector) -> Vector:
    """
    Multiplica una matriz por un vector.

    Args:
        matrix: La matriz
        vector: El vector

    Returns:
        Un nuevo vector resultado de la multiplicación
    """
    return Matrix([[sum(x * y for x, y in zip(row, vector.data)) for row in matrix.data]])


def matrix_multiply(m1: Matrix, m2: Matrix) -> Matrix:
    """
    Multiplica dos matrices.

    Args:
        m1: Primera matriz
        m2: Segunda matriz

    Returns:
        Una nueva matriz resultado de la multiplicación
    """
    return m1 * m2


def transpose(matrix: Matrix) -> Matrix:
    """
    Calcula la transpuesta de una matriz.

    Args:
        matrix: La matriz

    Returns:
        Una nueva matriz transpuesta
    """
    return matrix.T


def determinant(matrix: Matrix) -> Union[int, float]:
    """
    Calcula el determinante de una matriz cuadrada.

    Args:
        matrix: La matriz cuadrada

    Returns:
        El determinante
    """
    return matrix.determinant


def inverse(matrix: Matrix) -> Matrix:
    """
    Calcula la matriz inversa.

    Args:
        matrix: La matriz cuadrada invertible

    Returns:
        Una nueva matriz inversa
    """



def identity_matrix(size: int) -> Matrix:
    """
    Crea una matriz identidad de tamaño especificado.

    Args:
        size: El tamaño de la matriz (size x size)

    Returns:
        Una nueva matriz identidad
    """
    pass


def zeros_matrix(rows: int, columns: int) -> Matrix:
    """
    Crea una matriz de ceros con las dimensiones especificadas.

    Args:
        rows: Número de filas
        columns: Número de columnas

    Returns:
        Una nueva matriz llena de ceros
    """
    pass


def ones_matrix(rows: int, columns: int) -> Matrix:
    """
    Crea una matriz de unos con las dimensiones especificadas.

    Args:
        rows: Número de filas
        columns: Número de columnas

    Returns:
        Una nueva matriz llena de unos
    """
    pass
