import unittest
from modul_2.mod_three_fsm import ModThreeFSM


class TestModThreeFSM(unittest.TestCase):

    def setUp(self):
        # Set up ModThreeFSM
        self.mod_three_fsm = ModThreeFSM()

    def test_compute_remainder(self):
        # Test binary string computation
        self.assertEqual(self.mod_three_fsm.compute_remainder('1101'),
                         1)  # '1101' in binary, remainder 1 when divided by 3
        self.assertEqual(self.mod_three_fsm.compute_remainder('11'),
                         0)  # '111' in binary, remainder 0 when divided by 3
        self.assertEqual(self.mod_three_fsm.compute_remainder('10'), 2)  # '10' in binary, remainder 2 when divided by 3

    def test_empty_input(self):
        # Test empty string input (should return remainder 0)
        self.assertEqual(self.mod_three_fsm.compute_remainder(''), 0)

    def test_modthreefsm_transition(self):
        fsm = ModThreeFSM()
        fsm.process_input(['1'])
        self.assertEqual(fsm.get_current_state(), 'S1')  # '1' transitions from S0 to S1
        fsm.process_input(['0'])
        self.assertEqual(fsm.get_current_state(), 'S2')  # '10' transitions from S1 to S2


if __name__ == '__main__':
    unittest.main()