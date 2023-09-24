from helpers import (
    Collection,
    Array,
    Matrix,
    Matrix3D,
)


def binary_search(collection: Collection, target: int) -> bool:
    """Generic Binary Search, you can find and element from an array or 2d Matrix

    Args:
        collection (List[Union[int, List[int],List[[int]] ]]): An Array or 2d/3d Matrix of integers.
        target (int): Number to find.

    Returns:
        bool: result if exist or not that element

    Example:
    >>> matrix = [
        [1, 2, 4],
        [4, 5, 6],
        [7, 8, 9],
    ]
    >>> target = 9
    >>> result = binary_search(matrix, target)
    >>> print(result)
    True
    >>> array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 100, 1000]
    >>> target = 10000
    >>> result = binary_search(array, target)
    >>> print(result)
    False
    >>> matrix = [
        [
            [1, 2, 3],
            [4, 5, 6],
        ],
        [
            [7, 8, 9],
            [10, 11, 12]
        ],
        [
            [13, 14, 15],
            [16, 17, 18]
        ]
    ]

    >>> target = 11
    >>> result = binary_search(matrix, target)
    >>> print(result)
    True
    """
    size: int = len(collection)
    if not size:
        return False  # Empty Collection

    if isinstance(collection[0], int):
        return binary_search_array(collection, target)
    if isinstance(collection[0][0], list):
        return binary_search_matrix_3d(collection, target)
    return binary_search_matrix(collection, target)


def binary_search_array(array: Array, target: int) -> bool:
    """A binary search implementation for List of integers

    Args:
        array (List[int]): List of integers.
        target (int): Number to find.

    Returns:
        bool: result if exist or not that element

    Example:
    >>> array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 100, 1000]
    >>> target = 9
    >>> result = binary_search_array(array, target)
    >>> print(result)
    True
    """
    low: int = 0
    high: int = len(array)

    while low < high:
        mid = (low + high) // 2

        if array[mid] == target:
            return True
        elif array[mid] < target:
            low = mid + 1
        else:
            high = mid

    return False  # Item not found


def binary_search_matrix(matrix: Matrix, target: int) -> bool:
    """_summary_

    Args:
        matrix (List[List[int]]): 2D Matrix of integers.
        target (int): Number to find.

    Returns:
        bool: result if exist or not that element

    Example:
    >>> matrix = [
        [1, 2, 4],
        [4, 5, 6],
        [7, 8, 9],
    ]
    >>> target = 9
    >>> result = binary_search_matrix(matrix, target)
    >>> print(result)
    True
    """
    row_size: int = len(matrix)
    col_size: int = len(matrix[0])
    low: int = 0
    high: int = row_size * col_size

    while low < high:
        mid = (low + high) // 2
        mid_value = matrix[mid // col_size][mid % col_size]

        if mid_value == target:
            return True
        elif mid_value < target:
            low = mid + 1
        else:
            high = mid

    return False  # Item not found


def binary_search_matrix_3d(matrix: Matrix3D, target: int) -> bool:
    """__summary__
    Perform binary search to find the target in a 3D matrix.

    Args:
        matrix (List[List[List[int]]]): 3D Matrix of integers.
        target (int): Number to find.

    Returns:
        bool: True if the target exists in the matrix, False otherwise.

    Example:
    >>> matrix = [
        [
            [1, 2, 3],
            [4, 5, 6],
        ],
        [
            [7, 8, 9],
            [10, 11, 12]
        ],
        [
            [13, 14, 15],
            [16, 17, 18]
        ]
    ]

    >>> target = 11
    >>> result = binary_search_3d(matrix, target)
    >>> print(result)
    True
    """
    rows: int = len(matrix)
    cols: int = len(matrix[0])
    depth: int = len(matrix[0][0])

    low: int = 0
    high: int = rows * cols * depth - 1

    while low < high:
        mid: int = (low + high) // 2
        mid_row: int = mid // (cols * depth)
        mid_col: int = (mid // depth) % cols
        mid_depth: int = mid % depth
        mid_value: int = matrix[mid_row][mid_col][mid_depth]

        if mid_value == target:
            return True
        elif mid_value < target:
            low = mid + 1
        else:
            high = mid

    return False  # Item not found in the matrix
