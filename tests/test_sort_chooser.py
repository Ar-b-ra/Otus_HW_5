import unittest

from sorting_fabric import InsertionSort, SelectionSort, MergeSort, SortingMethodChooser


class TestGetSorter(unittest.TestCase):
    def test_get_sorter_merge(self):
        sorter = SortingMethodChooser.get_sorter("merge")
        self.assertIsInstance(sorter, MergeSort)

    def test_get_sorter_selection(self):
        sorter = SortingMethodChooser.get_sorter("selection")
        self.assertIsInstance(sorter, SelectionSort)

    def test_get_sorter_insertion(self):
        sorter = SortingMethodChooser.get_sorter("insertion")
        self.assertIsInstance(sorter, InsertionSort)

    def test_get_sorter_unknown_method(self):
        with self.assertRaises(ValueError):
            SortingMethodChooser.get_sorter("unknown")


if __name__ == '__main__':
    unittest.main()
