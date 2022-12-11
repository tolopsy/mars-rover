from dataclasses import dataclass
from abc import ABC, abstractmethod
from enum import Enum
from utils import exit_program
from .point import Point


class LandShape(Enum):
    RECTANGULAR = "rectangular"


class Land(ABC):
    @abstractmethod
    def is_address_within(self, address: Point) -> bool:
        "checks if a point is inside land"
        pass


@dataclass
class RectangularLand(Land):
    upper_right_edge: Point
    lower_left_edge: Point = Point(x=0, y=0)

    def is_address_within(self, address: Point) -> bool:
        return (
            (address.x <= self.upper_right_edge.x and address.y <= self.upper_right_edge.y) and
            (address.x >= self.lower_left_edge.x and address.y >= self.lower_left_edge.y)
        )


class LandFactory:
    """factory class to create Land instances based on properties like shape of the land."""

    @classmethod
    def create(cls, land_shape: LandShape, **kwargs) -> Land:
        if land_shape == LandShape.RECTANGULAR:
            return RectangularLand(**kwargs)
        else:
            exit_program(f"no such land. got {land_shape} as land_shape")

