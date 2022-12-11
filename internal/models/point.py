from dataclasses import dataclass


@dataclass
class Point:
    """ Represents point in cartesian coordinate system.

        Main Attributes:
            x: x coordinate of the point.
            y: y coordinate of the point.

        Main Methods:
            move_x: move along x axis.
            move_y: move along y axis.
            move:   move along x and/or y axis.
    """

    x: int
    y: int

    def move_x(self, x=0):
        """ move point along x axis and changes point's x coordinate.
            @param
                x - length along x axis to move by.
        """
        self.x += x
    
    def move_y(self, y=0):
        """ move point along y axis and changes point's y coordinate.
            @param
                y - length along y axis to move by.
        """
        self.y += y

    def move(self, x=0, y=0):
        """ move point along a plane and changes point's x and/or y coordinate accordingly.
            @params:
                x - length along x axis to move by.
                y - length along y axis to move by.
        """
        self.move_x(x)
        self.move_y(y)
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, Point):
            return False
        
        return self.x == other.x and self.y == other.y