from enum import Enum
from copy import deepcopy
from dataclasses import dataclass
from utils import exit_program
from .point import Point


class Orientation(Enum):
    "Represents any of the four cardinal compass points."

    N = 0       # North
    E = 90      # East
    S = 180     # South
    W = 270     # West


@dataclass
class Direction:
    orientation: Orientation

    def rotate(self, rotation: int):
        if rotation % 90 != 0:
            exit_program("rotation should be to one of the four cardinal compass points")

        angle_of_orientation = (self.orientation.value + rotation) % 360
        self.orientation = Orientation(angle_of_orientation)
    
    @property
    def label(self):
        return self.orientation.name
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, Direction):
            return False

        return self.orientation == other.orientation

class Position:
    """ Represents the position of a mobile object.

        Main Attributes:
            point: Point (x and y coordinate) of the object.
            direction: Direction that the object is facing.

        Main Methods:
            rotate: changes direction of the object.
            move: moves the object by one unit along the direction faced.
            clone: copies the current position of an object
    """

    def __init__(self, x: int, y: int, orientation: Orientation) -> None:
        """ Initializer
        @params
            x: x coordinate of the point at a position.
            y: y coordinate of the point at a position.
            orientation: cardinal compass point faced at a position.
        """

        self.point = Point(x, y)
        self.direction = Direction(orientation)

    def rotate(self, angle: int):
        self.direction.rotate(angle)
    
    def change_orientation(self, orientation: Orientation):
        self.direction.orientation = orientation
    
    def move(self):
        "moves an object by one unit along the direction faced."

        if self.direction.orientation == Orientation.N:
            self.move_up()
        elif self.direction.orientation == Orientation.S:
            self.move_down()
        elif self.direction.orientation == Orientation.E:
            self.move_right()
        elif self.direction.orientation == Orientation.W:
            self.move_left()
    
    def move_up(self):
        self.point.move_y(1)
    
    def move_down(self):
        self.point.move_y(-1)
    
    def move_right(self):
        self.point.move_x(1)
    
    def move_left(self):
        self.point.move_x(-1)
    
    def clone(self):
        return deepcopy(self)

    def __str__(self):
        return f"{self.point.x} {self.point.y} {self.direction.label}"
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, Position):
            return False

        return self.point == other.point and self.direction == other.direction
