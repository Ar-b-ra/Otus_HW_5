from sorting import selection_sort, insertion_sort, merge_sort


def test_selection_sort():
    # Testing an empty list
    for sorting_methods in (selection_sort, insertion_sort, merge_sort):
        arr = []
        assert sorting_methods(arr) == []

        # Testing a list with one element
        arr = [5]
        assert sorting_methods(arr) == [5]

        # Testing a list with multiple elements
        arr = [3, 1, 4, 2]
        assert sorting_methods(arr) == [1, 2, 3, 4]

        # Testing a list with duplicate elements
        arr = [5, 2, 3, 2, 1, 4]
        assert sorting_methods(arr) == [1, 2, 2, 3, 4, 5]

        # Testing a list with negative numbers
        arr = [10, -5, 3, -8, 0]
        assert sorting_methods(arr) == [-8, -5, 0, 3, 10]

        # Testing a list with already sorted elements
        arr = [1, 2, 3, 4, 5]
        assert sorting_methods(arr) == [1, 2, 3, 4, 5]

