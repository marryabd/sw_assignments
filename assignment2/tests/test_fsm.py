import unittest
from modul_2.fsm import FiniteStateMachine


# Mock subclass of FiniteStateMachine for testing
class TestFSM(FiniteStateMachine):
    def __init__(self):
        states = {'q0', 'q1', 'q2'}
        alphabet = {'a', 'b'}
        initial_state = 'q0'
        final_states = {'q2'}
        transitions = {('q0', 'a'): 'q1', ('q1', 'b'): 'q2'}
        super().__init__(states, alphabet, initial_state, final_states, transitions)

    def transition(self, input_symbol):
        # Implement basic transition logic for testing
        self.current_state =  self.transitions.get((self.current_state, input_symbol), self.current_state)
        return self.current_state


class TestFiniteStateMachine(unittest.TestCase):

    def setUp(self):
        # Set up the mock FSM for testing
        self.fsm = TestFSM()

    def test_initial_state(self):
        # Test if FSM initializes to the correct initial state
        self.assertEqual(self.fsm.get_current_state(), 'q0')

    def test_valid_transition(self):
        # Test valid transition
        self.fsm.reset()
        self.fsm.transition('a')
        self.assertEqual(self.fsm.current_state, 'q1')
        self.fsm.transition('b')
        self.assertEqual(self.fsm.current_state, 'q2')

    def test_final_state(self):
        # Test final state recognition
        self.fsm.reset()
        self.fsm.transition('a')
        self.fsm.transition('b')
        self.assertEqual(self.fsm.get_final_state(), 'q2')

    def test_not_final_state(self):
        # Test non-final state
        self.fsm.reset()
        self.fsm.transition('a')
        with self.assertRaises(ValueError) as context:
            self.fsm.get_final_state()
        self.assertTrue(f"Current state {self.fsm.current_state} is not a final state." in str(context.exception))

    def test_invalid_input(self):
        # Test that invalid input raises a ValueError
        with self.assertRaises(ValueError) as context:
            self.fsm.process_input(['c'])
        self.assertTrue(f"Invalid input symbol: c" in str(context.exception))

    def test_reset(self):
        # Test the reset functionality
        self.fsm.reset()
        self.fsm.process_input(['a'])
        self.assertEqual(self.fsm.get_current_state(), 'q1')
        self.fsm.reset()
        self.assertEqual(self.fsm.get_current_state(), 'q0')

    def test_is_in_final_state(self):
        # Test if FSM correctly identifies final states
        self.fsm.reset()
        self.fsm.process_input(['a'])
        self.assertFalse(self.fsm.is_in_final_state())
        self.fsm.process_input(['b'])
        self.assertTrue(self.fsm.is_in_final_state())

    def test_process_input(self):
        self.fsm.process_input(['a'])
        self.assertEqual(self.fsm.get_current_state(), 'q1')
        self.fsm.process_input(['b'])
        self.assertEqual(self.fsm.get_current_state(), 'q2')

    if __name__ == '__main__':
        unittest.main()