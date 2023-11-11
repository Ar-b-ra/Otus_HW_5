from argparse import ArgumentParser
from pathlib import Path

from sorting_fabric import SortingMethodChooser

if __name__ == "__main__":
    arg_parser = ArgumentParser(add_help=True)
    arg_parser.add_argument("-i", "--input_file", nargs="?", type=str, default="input.txt")
    arg_parser.add_argument("-o", "--output_file", nargs="?", type=str, default="output.txt")
    arg_parser.add_argument("-s", "--sort_method", nargs="?", type=str, default="insertion",
                            choices=["merge", "selection", "insertion"])
    args = arg_parser.parse_args()
    input_file_path = Path(args.path)
    output_file_path = Path(args.output_file)

    sorting_method = args.sort_method
    sorter = SortingMethodChooser.get_sorter(sorting_method)
    sorter.sort_from_file(input_file_path)
    sorter.write_to_file(output_file_path)
