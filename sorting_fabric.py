import json
from abc import abstractmethod
from pathlib import Path
from typing import Union, Optional

from utility.custom_logger import root_logger
from utility.sorting import merge_sort, selection_sort, insertion_sort
from utility.timer_decorator import timer


class BaseSort:
    sort_type: str = ""

    def __init__(self):
        self.sorted_list = []

    def sort_from_file(self, input_file_path: Union[str, Path] = "input.txt",
                       ) -> Optional[list]:
        if (file_to_read := Path(input_file_path)).exists:
            with open(file_to_read) as file:
                self.sorted_list = self.sort([int(x) for x in file.read().split()])
                return self.sorted_list
        else:
            root_logger.exception(f"File {file_to_read} not found")
            raise FileNotFoundError(f"File {file_to_read} not found")

    @abstractmethod
    def sort(self, list_to_sort: list) -> list:
        return []

    def write_to_file(self, file_path: Union[str, Path] = "output.txt") -> None:
        with open(file_path, "w") as file:
            output_information = {
                "sort_type": self.sort_type,
                "sorted_list": self.sorted_list
            }
            json.dump(output_information, file)


class MergeSort(BaseSort):
    sort_type = "merge"

    @timer
    def sort(self, list_to_sort: list) -> list:
        self.sorted_list = merge_sort(list_to_sort)
        return self.sorted_list


class SelectionSort(BaseSort):
    sort_type = "selection"

    @timer
    def sort(self, list_to_sort: list) -> list:
        self.sorted_list = selection_sort(list_to_sort)
        return self.sorted_list


class InsertionSort(BaseSort):
    sort_type = "insertion"

    @timer
    def sort(self, list_to_sort: list) -> list:
        self.sorted_list = insertion_sort(list_to_sort)
        return self.sorted_list


class SortingMethodChooser:
    sorting_methods = {
        "merge": MergeSort,
        "selection": SelectionSort,
        "insertion": InsertionSort
    }

    @classmethod
    def get_sorter(cls, sorting_method: str) -> type[BaseSort]:

        if sorting_method in cls.sorting_methods:
            return cls.sorting_methods[sorting_method]
        else:
            raise ValueError(f"Unknown sorting method: {sorting_method}")
