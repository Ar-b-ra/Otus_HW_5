import json
from abc import abstractmethod
from pathlib import Path

from utility.custom_logger import root_logger
from utility.sorting import merge_sort, selection_sort, insertion_sort


class BaseSort:
    sort_type: str = ""

    def sort_from_file(self, input_file_path: str | Path = "input.txt",
                       output_file_path: str | Path = "output.txt") -> None:
        if (file_to_read := Path(input_file_path)).exists:
            with open(file_to_read) as file:
                base_list = [int(x) for x in file.read().split()]
                self.sort_and_write_to_file(base_list, output_file_path)
        else:
            root_logger.exception(f"File {file_to_read} not found")
            raise FileNotFoundError(f"File {file_to_read} not found")

    @abstractmethod
    def sort(self, list_to_sort: list) -> list:
        return []

    def sort_and_write_to_file(self, list_to_sort: list, file_path: str | Path = "output.txt") -> None:
        sorted_list = self.sort(list_to_sort)
        with open(file_path, "w") as file:
            output_information = {
                "sort_type": self.sort_type,
                sorted_list: self.sort(list_to_sort)
            }
            json.dump(output_information, file)


class MergeSort(BaseSort):
    sort_type = "merge"

    def sort(self, list_to_sort: list) -> list:
        return merge_sort(list_to_sort)


class SelectionSort(BaseSort):
    sort_type = "selection"

    def sort(self, list_to_sort: list) -> list:
        return selection_sort(list_to_sort)


class InsertionSort(BaseSort):
    sort_type = "insertion"

    def sort(self, list_to_sort: list) -> list:
        return insertion_sort(list_to_sort)


class SortingMethodChooser:

    @classmethod
    def get_sorter(cls, sorting_method: str) -> BaseSort:
        sorting_methods = {
            "merge": MergeSort,
            "selection": SelectionSort,
            "insertion": InsertionSort
        }

        if sorting_method in sorting_methods:
            return sorting_methods[sorting_method]()
        else:
            raise ValueError(f"Unknown sorting method: {sorting_method}")
