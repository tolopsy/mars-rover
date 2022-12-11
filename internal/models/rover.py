from dataclasses import dataclass, field
from copy import deepcopy
from .mechanics import Position
from .land import Land
from utils import exit_program


@dataclass
class Rover:
    """ Represents a rover.

        Main Attributes:
            name: name of rover.
            position: position of rover on a land.
            land: land where rover is situated.

        Main Methods:
            move: moves rover by one unit based on its position.
            spin: rotates rover by a given angle.
            spin_left: rotates rover to the left by 90 degrees
            spin_right: rotates rover to the right by 90 degrees
            set_instruction: gives rover instruction to execute.
            reset_instruction: clears previous instruction given to rover.
            run_instruction: executes the instruction given to rover.
            clone: returns a clone of rover.
    """

    name: str
    position: Position
    land: Land
    _instruction: str = field(default="", init=False, repr=False)

    @property
    def land(self) -> Land:
        return self._land

    @land.setter
    def land(self, new_land: Land):
        self._land = new_land
        self.validate_position_is_on_land()

    def move(self):
        "moves rover by one unit based on its position."

        hypothetic_position = self.position.clone()
        hypothetic_position.move()
        if self.land.is_address_within(hypothetic_position.point):
            self.position = hypothetic_position
 
    def spin(self, angle: int):
        self.position.rotate(angle)
    
    def spin_left(self):
        self.spin(-90)
    
    def spin_right(self):
        self.spin(90)
    
    def set_instruction(self, instruction: str):
        self._instruction = instruction
    
    def reset_instruction(self):
        self._instruction = ""
    
    def validate_position_is_on_land(self):
        if not self.land.is_address_within(self.position.point):
            exit_program(f"Rover '{self.name}' is outside specified land")
    
    @property
    def instruction(self):
        return self._instruction
    
    def run_instruction(self):
        """ Executes instruction given to rover.

            Instruction executed is a string stream of characters.
            The executable instruction characters are `L`, `R` and `M`.

                L: Makes rover spin leftward.
                R: Makes rover spin rightward.
                M: Makes rover move one unit along the direction it is facing.
        """

        if not self.instruction:
            return
        
        for instruction in self.instruction:
            if instruction == "L":
                self.spin_left()
            elif instruction == "R":
                self.spin_right()
            elif instruction == "M":
                self.move()
        
        self.reset_instruction()
    
    def clone(self):
        return deepcopy(self)
