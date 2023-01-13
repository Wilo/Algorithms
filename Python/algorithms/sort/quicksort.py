from helpers import Collection

# function to find the partition position
def __partition(array: Collection, low: int, high: int) -> int:

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
def quicksort(array: Collection, low: int, high: int) -> None:
    if low < high:

        # find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi: int = __partition(array, low, high)

        # recursive call on the left of pivot
        quicksort(array, low, pi - 1)

        # recursive call on the right of pivot
        quicksort(array, pi + 1, high)
