from helpers import (
    Collection,
    Array,
    Matrix,
)


def binary_search(collection: Collection, target: int) -> bool:
    """Generic Binary Search, you can find and element from an array or 2d Matrix

    Args:
        collection (List[Union[int, List[int]]]): An Array or 2d Matrix of integers.
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
    """
    size: int = len(collection)
    if not size:
        return False  # Empty Collection
    if isinstance(collection[0], list):
        return binary_search_matrix(collection, target)
    return binary_search_array(collection, target)


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
    mid: int

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
    mid: int

    while low < high:
        mid = (low + high) // 2

        if matrix[mid // col_size][mid % col_size] == target:
            return True
        elif matrix[mid // col_size][mid % col_size] < target:
            low = mid + 1
        else:
            high = mid

    return False  # Item not found
