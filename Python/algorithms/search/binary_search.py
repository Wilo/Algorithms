from helpers import (
    Collection,
    List,
)


def binary_search(collection: Collection, target) -> bool:
    size: int = len(collection)
    if not size:
        return False  # Empty Collection
    if isinstance(collection[0], list):
        return binary_search_matrix(collection, target)
    return binary_search_array(collection, target)


def binary_search_array(array: List[int], target: int) -> bool:
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


def binary_search_matrix(matrix: List[List[int]], target: int) -> bool:
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
