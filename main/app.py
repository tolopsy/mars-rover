import argparse
from internal.parser import InputParser
from utils import get_input_from_args

if __name__ == "__main__":
    arg_parser = argparse.ArgumentParser(description="plateau and rover inputs", prog="Mars Rover")

    arg_parser.add_argument("file_path", type=str, help="file path for plateau and rover inputs' file", nargs="?")
    arg_parser.add_argument("-p", "--plateau_input", type=str, help="plateau input", nargs="?", default="")
    arg_parser.add_argument("-r", "--rovers_input", type=str, help="landing and instructions input for rovers", nargs="*", default=[])

    args = arg_parser.parse_args()

    data = get_input_from_args(args.file_path, args.plateau_input, args.rovers_input)

    parser = InputParser(inputs=data)
    rovers = parser.rovers

    for rover in rovers:
        rover.run_instruction()
        print(f"{rover.name}:{rover.position}")
