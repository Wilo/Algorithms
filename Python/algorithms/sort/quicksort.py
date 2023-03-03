from helpers import Array

# function to find the partition position
def __partition(array: Array, low: int, high: int) -> int:

    # choose the rightmost element as pivot
    pivot: int = array[high]

    # pointer for greater element
    i: int = low - 1

    # traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:
            # if element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1

            # swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])

    # swap the pivot element with the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])

    # return the position from where partition is done
    return i + 1


# function to perform quicksort
def quicksort(array: Array, low: int, high: int) -> None:
    """Array sorting using quicksort algorithm

    Time Complexity:
        Best: O(n log(n))
        Average: O(n log(n))
        Wrost: O(n²)

    Space Complexity:
        Wrost: O(log(n))

    Args:
        array (Array): Unsorted Array
        low (int): Array's left position
        high (int): Array's right position

    Example:
    >>> array = [9, 8, 6, 7, 2, 3, 5, 1, 4]
    >>> quicksort(array)
    >>> print(array)
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    """
    if low < high:

        # find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi: int = __partition(array, low, high)

        # recursive call on the left of pivot
        quicksort(array, low, pi - 1)

        # recursive call on the right of pivot
        quicksort(array, pi + 1, high)
