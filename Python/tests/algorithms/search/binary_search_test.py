from dataclasses import dataclass

import pytest

from algorithms.search.binary_search import binary_search
from helpers import Collection, List


@dataclass
class TestCases:
    description: str
    collection: Collection
    target: int
    expected: bool
    __test__: bool = False


class TestBinarySearch:
    ARRAY_BASE: Collection = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 30, 100, 1000]
    MATRIX_BASE: Collection = [
        [1, 2, 4],
        [4, 5, 6],
        [7, 8, 9],
    ]
    test_cases: List[TestCases] = [
        TestCases("Array:> Happy Path", ARRAY_BASE, 1000, True),
        TestCases("Array:> Sad Path", ARRAY_BASE, 50, False),
        TestCases("Array:> Empty Collection", [], 1, False),
        TestCases("Matrix:> Happy Path", MATRIX_BASE, 5, True),
        TestCases("Matrix:> Sad Path", MATRIX_BASE, 50, False),
        TestCases("Matrix:> Empty Collection", [], 10, False),
    ]

    @pytest.mark.parametrize(
        "collection, target, expected",
        list(
            map(
                lambda item: (
                    item.collection,
                    item.target,
                    item.expected,
                ),
                test_cases,
            )
        ),
        ids=list(map(lambda item: item.description, test_cases)),
    )
    def test_array(self, collection: Collection, target: int, expected: bool) -> None:
        result: bool = binary_search(collection, target)
        assert result == expected
