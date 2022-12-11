from sys import exit
from os.path import isfile
from typing import List

def exit_program(error_message: str):
    exit(f"error occured: {error_message}")

def get_input_from_args(file_path: str, plateau_arg: str, rovers_arg: List[str]) -> List[str]:
    if file_path and isfile(file_path):
        with open(file_path, "r") as file:
            # filter off empty lines in file and read to list
            data = list(filter(lambda x: x.strip() != '', file.readlines()))
    else:
        data = [plateau_arg, *rovers_arg]
    
    return data
