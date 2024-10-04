from .fsm import FiniteStateMachine
import warnings
from typing import List


class ModThreeFSM(FiniteStateMachine):
    def __init__(self):
        """
        Initializes the ModThreeFSM class which is a specific FSM for calculating the remainder
        when dividing a binary number by 3 using a Finite State Machine.
        """
        states = {'S0', 'S1', 'S2'}
        alphabet = {'0', '1'}  # Valid input alphabet for binary input
        initial_state = 'S0'
        final_states = {'S0', 'S1', 'S2'}

        # Transitions based on input (0 or 1)
        transitions = {
            ('S0', '0'): 'S0', ('S0', '1'): 'S1',
            ('S1', '0'): 'S2', ('S1', '1'): 'S0',
            ('S2', '0'): 'S1', ('S2', '1'): 'S2'
        }

        # Initialize the base FSM with the mod-three specific parameters
        super().__init__(states, alphabet, initial_state, final_states, transitions)

    def transition(self, input_symbol: str) -> str:
        """
        Applies the transition function based on the current state and input symbol.

        Args:
            input_symbol: The input symbol to process.

        Returns:
            The next state based on the transition function.
        """
        # Check if a transition exists for the current state and input symbol
        if (self.current_state, input_symbol) not in self.transitions:
            # Generate a warning if no valid transition is found
            warnings.warn(f"No transition defined for state '{self.current_state}' with symbol '{input_symbol}'. "
                          f"FSM remains in the current state.", UserWarning)

        # Get the next state, or remain in the current state if no transition is found
        self.current_state = self.transitions.get((self.current_state, input_symbol), self.current_state)
        return self.current_state

    def compute_remainder(self, binary_string: str) -> int:
        """
        Processes a binary string and computes the remainder when divided by 3.

        Args:
            binary_string (str): A string of '0's and '1's representing the binary input.

        Returns:
            int: The remainder when the binary number is divided by 3.
        """
        # Reset the FSM to the initial state before processing
        self.reset()

        if not binary_string:
            return 0  # If the input is empty, return 0

        # Process the input string (input validation is already handled in the parent class)
        self.process_input(list(binary_string)) # Convert string to list of symbols

        # Map final states to remainders
        remainder_map = {'S0': 0, 'S1': 1, 'S2': 2}
        return remainder_map[self.get_final_state()]
