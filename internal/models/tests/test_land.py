from unittest import TestCase
from internal.models.land import RectangularLand, Land, LandFactory, LandShape
from internal.models.point import Point


class TestRectangularLand(TestCase):
    def setUp(self):
        self.land = RectangularLand(upper_right_edge=Point(3,3))

    def test_rectangular_land_instance_of_land(self):
        self.assertIsInstance(self.land, Land)
    
    def test_point_is_on_land(self):
        point = Point(1,2)
        self.assertTrue(self.land.is_address_within(point))
    
    def test_point_on_land_upper_right_edge_is_on_land(self):
        point = self.land.upper_right_edge
        self.assertTrue(self.land.is_address_within(point))

    def test_point_on_land_upper_left_edge_is_on_land(self):
        point = Point(self.land.lower_left_edge.x, self.land.upper_right_edge.y)
        self.assertTrue(self.land.is_address_within(point))

    def test_point_on_land_lower_right_edge_is_on_land(self):
        point = Point(self.land.upper_right_edge.x, self.land.lower_left_edge.y)
        self.assertTrue(self.land.is_address_within(point))

    def test_point_on_land_lower_left_edge_is_on_land(self):
        point = self.land.lower_left_edge
        self.assertTrue(self.land.is_address_within(point))
    
    def test_point_above_land_is_not_on_land(self):
        # y coordinate just above land's maximum y coordinate
        y_coordinate = self.land.upper_right_edge.y + 1

        # point just above land's upper right edge
        point = Point(self.land.upper_right_edge.x, y_coordinate)
        self.assertFalse(self.land.is_address_within(point))

        # point just above land's upper left edge
        point = Point(self.land.lower_left_edge.x, y_coordinate)
        self.assertFalse(self.land.is_address_within(point))

        # mid x-coordinate of land
        mid_x_coordinate = int((self.land.lower_left_edge.x + self.land.upper_right_edge.x) / 2)

        point = Point(mid_x_coordinate, y_coordinate)
        self.assertFalse(self.land.is_address_within(point))


    def test_point_below_land_is_not_on_land(self):
        # y coordinate just below land's minimum y coordinate
        y_coordinate = self.land.lower_left_edge.y - 1

        # point just below land's lower right edge
        point = Point(self.land.upper_right_edge.x, y_coordinate)
        self.assertFalse(self.land.is_address_within(point))

        # point just below land's lower left edge
        point = Point(self.land.lower_left_edge.x, y_coordinate)
        self.assertFalse(self.land.is_address_within(point))

        # mid or near-mid x-coordinate of land
        mid_x_coordinate = int((self.land.lower_left_edge.x + self.land.upper_right_edge.x) / 2)

        point = Point(mid_x_coordinate, y_coordinate)
        self.assertFalse(self.land.is_address_within(point))

    def test_point_before_land_left_side_is_not_on_land(self):
        # x coordinate just before the land's minimum x coordinate
        x_coordinate = self.land.lower_left_edge.x - 1

        # point just before land's left side upper edge
        point = Point(x_coordinate, self.land.upper_right_edge.y)
        self.assertFalse(self.land.is_address_within(point))

        # point just before land's left side lower edge
        point = Point(x_coordinate, self.land.lower_left_edge.y)
        self.assertFalse(self.land.is_address_within(point))

        # mid or near mid y-coordinate of land
        mid_y_coordinate = int((self.land.upper_right_edge.y + self.land.lower_left_edge.y)/2)

        point = Point(x_coordinate, mid_y_coordinate)
        self.assertFalse(self.land.is_address_within(point))

    def test_point_after_land_right_side_is_not_on_land(self):
        # x coordinate just before the land's maximum x coordinate
        x_coordinate = self.land.upper_right_edge.x + 1

        # point just after land's right side upper edge
        point = Point(x_coordinate, self.land.upper_right_edge.y)
        self.assertFalse(self.land.is_address_within(point))

        # point just after land's right side lower edge
        point = Point(x_coordinate, self.land.lower_left_edge.y)
        self.assertFalse(self.land.is_address_within(point))

        # mid or near mid y-coordinate of land
        mid_y_coordinate = int((self.land.upper_right_edge.y + self.land.lower_left_edge.y)/2)

        point = Point(x_coordinate, mid_y_coordinate)
        self.assertFalse(self.land.is_address_within(point))


class TestLandFactory(TestCase):
    def test_land_factory_creates_rectangular_land(self):
        land = LandFactory.create(land_shape=LandShape.RECTANGULAR, upper_right_edge=Point(3,3))
        self.assertIsInstance(land, RectangularLand)
