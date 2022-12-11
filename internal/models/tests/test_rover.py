import random
from unittest import TestCase
from internal.models.rover import Rover
from internal.models.land import RectangularLand
from internal.models.mechanics import Position, Orientation
from internal.models.point import Point


class RoverTestCase(TestCase):
    def setUp(self):
        land = RectangularLand(upper_right_edge=Point(6, 6))
        self.rover = Rover(name="Test Rover", position=Position(2, 2, Orientation.N), land=land)
    
    def reset_rover_position_orientation(self, orientation=Orientation.N):
        self.rover.position.change_orientation(orientation)

    def test_rover_set_instruction(self):
        instruction = ''.join(random.choice(["L", "R", "M"]) for i in range(8))
        self.rover.set_instruction(instruction)
        self.assertEqual(self.rover.instruction, instruction)

    def test_rover_reset_instruction(self):
        instruction = ''.join(random.choice(["L", "R", "M"]) for i in range(8))
        self.rover.set_instruction(instruction)
        self.rover.reset_instruction()
        self.assertEqual(self.rover.instruction, "")
    
    def test_instruction_resets_at_end_of_every_run(self):
        instruction = "LMMRM"
        self.rover.set_instruction(instruction)
        self.rover.run_instruction()
        self.assertEqual(self.rover.instruction, "")

    def test_rover_moves_up_when_facing_north(self):
        self.reset_rover_position_orientation()
        position = self.rover.position.clone()
        self.rover.move()
        self.assertEqual(self.rover.position.point.y, position.point.y+1)
    
    def test_rover_moves_down_when_facing_south(self):
        self.reset_rover_position_orientation(Orientation.S)
        position = self.rover.position.clone()
        self.rover.move()
        self.assertEqual(self.rover.position.point.y, position.point.y-1)
    
    def test_rover_moves_left_when_facing_west(self):
        self.reset_rover_position_orientation(Orientation.W)
        position = self.rover.position.clone()
        self.rover.move()
        self.assertEqual(self.rover.position.point.x, position.point.x-1)

    def test_rover_moves_right_when_facing_east(self):
        self.reset_rover_position_orientation(Orientation.E)
        position = self.rover.position.clone()
        self.rover.move()
        self.assertEqual(self.rover.position.point.x, position.point.x+1)

    def test_rover_cannot_move_out_of_land(self):
        self.rover.land = RectangularLand(upper_right_edge=self.rover.position.point)
        self.reset_rover_position_orientation()
        position = self.rover.position.clone()
        self.rover.move()
        self.assertEqual(position, self.rover.position)

    def test_rover_spin_left_around(self):
        self.reset_rover_position_orientation()
        self.rover.spin_left()
        self.assertEqual(self.rover.position.direction.orientation, Orientation.W)

        self.rover.spin_left()
        self.assertEqual(self.rover.position.direction.orientation, Orientation.S)

        self.rover.spin_left()
        self.assertEqual(self.rover.position.direction.orientation, Orientation.E)

        self.rover.spin_left()
        self.assertEqual(self.rover.position.direction.orientation, Orientation.N)

    def test_rover_spin_right_around(self):
        self.reset_rover_position_orientation()
        self.rover.spin_right()
        self.assertEqual(self.rover.position.direction.orientation, Orientation.E)

        self.rover.spin_right()
        self.assertEqual(self.rover.position.direction.orientation, Orientation.S)

        self.rover.spin_right()
        self.assertEqual(self.rover.position.direction.orientation, Orientation.W)

        self.rover.spin_right()
        self.assertEqual(self.rover.position.direction.orientation, Orientation.N)

    def test_rover_can_only_spin_to_a_cardinal_compass_point(self):
        with self.assertRaises(SystemExit):
            self.rover.spin(70)

    def test_rover_run_instruction(self):
        self.reset_rover_position_orientation()
        rover_clone = self.rover.clone()
        self.assertEqual(self.rover.position, rover_clone.position)

        instruction = "LMMRM"
        self.rover.set_instruction(instruction)
        self.rover.run_instruction()
        self.assertNotEqual(self.rover.position, rover_clone.position)

        # manually performs instruction for clone
        rover_clone.spin_left()
        rover_clone.move()
        rover_clone.move()
        rover_clone.spin_right()
        rover_clone.move()

        self.assertEqual(self.rover.position, rover_clone.position)

    def test_rover_cannot_land_outside_specified_land(self):
        land = RectangularLand(upper_right_edge=Point(3, 4))
        with self.assertRaises(SystemExit):
            Rover(name="Test Rover", position=Position(6, 7, Orientation.N), land=land)
