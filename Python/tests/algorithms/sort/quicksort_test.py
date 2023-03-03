import pytest
from dataclasses import dataclass

from algorithms.sort.quicksort import quicksort
from helpers import Collection, List


@dataclass
class TestCases:
    description: str
    collection: Collection
    left: int
    right: int
    expected: Collection
    __test__: bool = False


class TestQuickSort:
    ARRAY_UNSORTED: List[int] = [9, 8, 6, 7, 2, 3, 5, 1, 4]
    SORTED_ARRAY: List[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    EXPECTED_ARRAY: List[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    EMPTY_ARRAY: List = []
    EXPECTED_EMPTY_ARRAY: List = []
    test_cases: List[TestCases] = [
        TestCases(
            "Happy Path", ARRAY_UNSORTED, 0, len(ARRAY_UNSORTED) - 1, EXPECTED_ARRAY
        ),
        TestCases(
            "Empty Array Test Case",
            EMPTY_ARRAY,
            0,
            len(EMPTY_ARRAY) - 1,
            EXPECTED_EMPTY_ARRAY,
        ),
        TestCases(
            "Sorted Array Test Case",
            SORTED_ARRAY,
            0,
            len(SORTED_ARRAY) - 1,
            EXPECTED_ARRAY,
        ),
    ]

    @pytest.mark.parametrize(
        "collection, left, right, expected",
        list(
            map(
                lambda item: (
                    item.collection,
                    item.left,
                    item.right,
                    item.expected,
                ),
                test_cases,
            )
        ),
        ids=list(map(lambda item: item.description, test_cases)),
    )
    def test(
        self, collection: Collection, left: int, right: int, expected: Collection
    ) -> None:
        quicksort(collection, left, right)
        assert collection == expected
