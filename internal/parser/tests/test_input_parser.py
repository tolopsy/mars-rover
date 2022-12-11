from unittest import TestCase
from typing import List
from internal.parser.input_parser import InputParser


class InputParserTestCase(TestCase):
    def _build_valid_inputs(
        self,
        no_of_rovers: int,
        test_plateau_upper_right_edge_str,
        test_landing_position_str,
        test_instruction: str
    ) -> List[str]:
        test_inputs = []
        test_inputs.append(f"Plateau:{test_plateau_upper_right_edge_str}")
        
        for rover_no in range(no_of_rovers):
            rover_name = f"Rover{rover_no+1}"
            test_inputs.append(f"{rover_name} Landing:{test_landing_position_str}")
            test_inputs.append(f"{rover_name} Instructions:{test_instruction}")
        
        return test_inputs

    def setUp(self):
        self.rovers_count = 3
        self.test_plateau_upper_right_edge_str = "6 7"
        self.test_landing_position_str = "1 3 N"
        self.test_instruction = "LMLMMLRM"
        self.inputs = self._build_valid_inputs(
            no_of_rovers=self.rovers_count,
            test_plateau_upper_right_edge_str=self.test_plateau_upper_right_edge_str,
            test_landing_position_str=self.test_landing_position_str,
            test_instruction=self.test_instruction
        )

    def assert_exit_program(self, inputs):
        with self.assertRaises(SystemExit):
            InputParser(inputs=inputs)
    
    def assert_exit_program_on_set_input(self):
        self.assert_exit_program(inputs=self.inputs)
    
    def test_should_not_receive_empty_inputs(self):
        self.assert_exit_program(inputs=[])
        
    def test_must_receive_inputs(self):
        self.assert_exit_program(inputs=None)
    
    def test_parser_sets_input_instruction_for_each_rovers(self):
        parser = InputParser(inputs=self.inputs)
        for rover in parser.rovers:
            self.assertEqual(rover.instruction, self.test_instruction)

    def test_get_rovers_returns_correct_list_of_rovers(self):
        parser = InputParser(inputs=self.inputs)
        self.assertEqual(len(parser.rovers), self.rovers_count)
    
    def test_valid_inputs_parses_successfully(self):
        try:
            InputParser(inputs=self.inputs)
        except:
            self.fail("InputParser() raises an unexpected exception")

    def test_first_item_in_input_must_be_for_plateau(self):
        inputs = self.inputs[1:]    # remove plateau input
        self.assert_exit_program(inputs=inputs)

    def test_invalid_plateau_input_exits_program(self):
        self.inputs[0] = "Plateau:v 7"
        self.assert_exit_program_on_set_input()

    def test_invalid_rover_landing_position_exits_program(self):
        # invalid landing x coordinate
        self.inputs.append("Rover Landing:r 2 N")
        self.assert_exit_program_on_set_input()

        # invalid landing y coordinate
        self.inputs.append("Rover Landing:2 t N")
        self.assert_exit_program_on_set_input()
        
        # invalid landing cardinal compass point
        self.inputs.append("Rover Landing:2 2 Q")
        self.assert_exit_program_on_set_input()

    def test_rover_landing_position_typo_error_input_exits_program(self):
        typo_landing_statement = "Rover Landiong:2 2 N"
        self.inputs.append(typo_landing_statement)
        self.assert_exit_program_on_set_input()
    
    def test_rover_instruction_typo_error_input_exits_program(self):
        typo_instruction = "Rover Instuctn:LMLMMR"
        self.inputs.append(typo_instruction)
        self.assert_exit_program_on_set_input()