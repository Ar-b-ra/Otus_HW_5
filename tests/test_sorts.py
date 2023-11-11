import unittest

from utility.sorting import selection_sort, insertion_sort, merge_sort


class SortingTestCase(unittest.TestCase):
    def test_selection_sort(self):
        # Testing an empty list
        arr = []
        self.assertEqual(selection_sort(arr), [])

        # Testing a list with one element
        arr = [5]
        self.assertEqual(selection_sort(arr), [5])

        # Testing a list with multiple elements
        arr = [3, 1, 4, 2]
        self.assertEqual(selection_sort(arr), [1, 2, 3, 4])

        # Testing a list with duplicate elements
        arr = [5, 2, 3, 2, 1, 4]
        self.assertEqual(selection_sort(arr), [1, 2, 2, 3, 4, 5])

        # Testing a list with negative numbers
        arr = [10, -5, 3, -8, 0]
        self.assertEqual(selection_sort(arr), [-8, -5, 0, 3, 10])

        # Testing a list with already sorted elements
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(selection_sort(arr), [1, 2, 3, 4, 5])
        
    def test_merge_sort(self):
        # Testing an empty list
        arr = []
        self.assertEqual(merge_sort(arr), [])

        # Testing a list with one element
        arr = [5]
        self.assertEqual(merge_sort(arr), [5])

        # Testing a list with multiple elements
        arr = [3, 1, 4, 2]
        self.assertEqual(merge_sort(arr), [1, 2, 3, 4])

        # Testing a list with duplicate elements
        arr = [5, 2, 3, 2, 1, 4]
        self.assertEqual(merge_sort(arr), [1, 2, 2, 3, 4, 5])

        # Testing a list with negative numbers
        arr = [10, -5, 3, -8, 0]
        self.assertEqual(merge_sort(arr), [-8, -5, 0, 3, 10])

        # Testing a list with already sorted elements
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(merge_sort(arr), [1, 2, 3, 4, 5])
        
    def test_insertion_sort(self):
        # Testing an empty list
        arr = []
        self.assertEqual(insertion_sort(arr), [])

        # Testing a list with one element
        arr = [5]
        self.assertEqual(insertion_sort(arr), [5])

        # Testing a list with multiple elements
        arr = [3, 1, 4, 2]
        self.assertEqual(insertion_sort(arr), [1, 2, 3, 4])

        # Testing a list with duplicate elements
        arr = [5, 2, 3, 2, 1, 4]
        self.assertEqual(insertion_sort(arr), [1, 2, 2, 3, 4, 5])

        # Testing a list with negative numbers
        arr = [10, -5, 3, -8, 0]
        self.assertEqual(insertion_sort(arr), [-8, -5, 0, 3, 10])

        # Testing a list with already sorted elements
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(insertion_sort(arr), [1, 2, 3, 4, 5])


if __name__ == '__main__':
    unittest.main()