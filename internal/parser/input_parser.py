from typing import List, Dict
from dataclasses import dataclass
from internal.models import (
    Land,
    LandFactory,
    LandShape,
    Point,
    Position,
    Orientation,
    Rover
)
from utils import exit_program


@dataclass
class InputParser:
    """ Implements the steps to parse inputs from users, give instructions to rovers and fetch the list of rovers on plateau.

        Main Attributes:
            inputs: list representing inputs from users (plateau input and per-rover landing/instructions inputs).

        Main Methods:
            get_rovers: returns list of rovers on plateau
    """
    inputs: List[str]

    def __post_init__(self):
        if not self.inputs:
            exit_program("no input was given")

        self.rovers = self._get_rovers()
    
    def _get_rovers(self) -> List[Rover]:
        rover_inputs = self.inputs[1:]
        rover_details = self._get_rover_details(rover_inputs)
        rovers = []
        plateau = self._get_plateau()

        for name, details in rover_details.items():
            rover = Rover(name=name, position=details["landing_position"], land=plateau)
            rover.set_instruction(details["instructions"])
            rovers.append(rover)

        return rovers

    @staticmethod
    def _parse_to_position(position_str: str) -> Position:
        """ Returns position instance as represented by a string.

            @param
                position_str: string representation of a position. For example: '0 3 E'
        """

        try:
            x, y, orientation = position_str.split()
            orientation = getattr(Orientation, orientation)
            assert x.isdigit() and y.isdigit()
            assert isinstance(orientation, Orientation)
        except (ValueError, AttributeError, AssertionError):
            exit_program(f"invalid position definition: {position_str}")

        return Position(int(x), int(y), orientation)

    def _get_plateau(self) -> Land:
        "get plateau as represented in the inputs"

        try:
            plateau_definition = self.inputs[0]
            plateau_definition_list = plateau_definition.lower().split("plateau:")
        except IndexError:
            exit_program("no input was given")

        if len(plateau_definition_list) != 2 or plateau_definition_list[0] != "":
            exit_program(f"plateau end point not correctly given. got {plateau_definition}")
        
        upper_right_edge_list_str = plateau_definition_list[1].split()
        if len(upper_right_edge_list_str) != 2:
            exit_program(f"coordinates definition must be exactly 2. got {upper_right_edge_list_str} for plateau")
        
        x_coordinate_str = upper_right_edge_list_str[0]
        y_coordinate_str = upper_right_edge_list_str[1]

        if not (x_coordinate_str.isdigit() and y_coordinate_str.isdigit()):
            exit_program(f"coordinate values must be integers. got {x_coordinate_str} and {y_coordinate_str}")

        upper_right_edge = Point(x=int(x_coordinate_str), y=int(y_coordinate_str))
        return LandFactory.create(land_shape=LandShape.RECTANGULAR, upper_right_edge=upper_right_edge)
    
    def _get_rover_details(self, inputs: List[str]) -> Dict:
        input_types = ("landing", "instructions")
        rover_details = {}

        for rover_input in inputs:
            try:
                key, value = rover_input.split(":")
                name, input_type = key.split()
                input_type = input_type.lower()
                assert input_type in input_types
    
            except (ValueError, AssertionError):
                exit_program(f"invalid rover input. got {rover_input}")
            
            rover_details.setdefault(name, {})

            if input_type == "landing":
                rover_details[name]["landing_position"] = self._parse_to_position(value)
            elif input_type == "instructions":
                rover_details[name]["instructions"] = value.strip()
        
        return rover_details
