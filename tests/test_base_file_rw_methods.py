import json
import os
import unittest
from pathlib import Path

from sorting_fabric import SortingMethodChooser


class TestSortFromFile(unittest.TestCase):
    def setUp(self):
        self.input_file_path = Path("input.txt")
        self.output_file_path = Path("output.txt")
        self.expecting_list = [12, 13, 15, 18, 19, 21, 23, 24, 25, 27, 28, 29, 31, 32, 34, 36, 38, 39, 41, 42, 45, 47,
                               51,
                               52, 54, 56, 57, 60, 63, 65, 66, 68, 69, 71, 73, 74, 76, 77, 78, 79, 81, 83, 85, 86, 88,
                               89,
                               91, 92, 95, 97, 98]
        with open(self.input_file_path, "w") as file_to_write:
            file_to_write.write(
                "45 12 83 27 66 39 51 74 18 92 63"
                " 56 29 88 42 71 34 77 23 68 15 97"
                " 81 47 60 32 79 25 69 36 98 52 86"
                " 21 73 38 95 57 13 89 65 31 76 19"
                " 91 54 28 85 41 78 24")
        with open(self.output_file_path, "w") as file_to_write:
            file_to_write.write("")

    def tearDown(self):
        os.remove(self.input_file_path)
        os.remove(self.output_file_path)

    def test_sort_from_file_existing_file(self):
        for method in SortingMethodChooser.sorting_methods:
            my_class = SortingMethodChooser.get_sorter(method)()
            my_class.sort_from_file(self.input_file_path)
            self.assertEqual(my_class.sorted_list, self.expecting_list)

    def test_write_to_file_sorted_list(self):

        for method in SortingMethodChooser.sorting_methods:
            my_class = SortingMethodChooser.get_sorter(method)()
            my_class.sort_from_file(self.input_file_path)
            my_class.write_to_file(self.output_file_path)

            expected_text = {"sort_type": method, "sorted_list": self.expecting_list}
            with open(self.output_file_path, "r") as json_file:
                self.assertEqual(json.load(json_file), expected_text)

    def test_incorrect_input_path(self):
        for method in SortingMethodChooser.sorting_methods:
            my_class = SortingMethodChooser.get_sorter(method)()
            with self.assertRaises(FileNotFoundError):
                my_class.sort_from_file("incorrect_path")


if __name__ == '__main__':
    unittest.main()
