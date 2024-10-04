from abc import ABC, abstractmethod
from typing import List, Any, Set, TypeVar

# Define a generic type for states
StateType = TypeVar('StateType')
AlphabetType = TypeVar('AlphabetType')


class FiniteStateMachine(ABC):
    """
    A generic Finite State Machine (FSM) implementation with encapsulated attributes.
    """

    def __init__(self, states: Set[StateType], alphabet: Set[AlphabetType], initial_state: StateType,
                 final_states: Set[StateType], transitions: Any):
        self.__states = states  # Private: not to be modified directly
        self.__alphabet = alphabet  # Private: not to be modified directly
        self.__initial_state = initial_state  # Private: immutable initial state
        self.__final_states = final_states  # Private: not to be modified directly
        self.__transitions = transitions  # Private: not to be modified directly
        self.current_state = initial_state  # Public: this can change during execution

    @property
    def states(self) -> Set[StateType]:
        """Returns the states of the FSM."""
        return self.__states

    @property
    def alphabet(self) -> Set[AlphabetType]:
        """Returns the input alphabet of the FSM."""
        return self.__alphabet

    @property
    def initial_state(self) -> StateType:
        """Returns the initial state of the FSM."""
        return self.__initial_state

    @property
    def final_states(self) -> Set[StateType]:
        """Returns the final (accepting) states of the FSM."""
        return self.__final_states

    @property
    def transitions(self) -> Any:
        """Returns the transition function of the FSM."""
        return self.__transitions

    @abstractmethod
    def transition(self, input_symbol: AlphabetType) -> None:
        """
        Abstract method for handling state transitions. Must be implemented by subclasses.

        Args:
            input_symbol: The input symbol to process.
        """
        pass

    def process_input(self, input_sequence: List[AlphabetType]) -> None:
        """
        Processes a sequence of input symbols, updating the current state accordingly.

        Args:
            input_sequence: A string or list of input symbols to process.

        Raises:
            ValueError: If the input symbol is not in the alphabet.
        """
        for input_symbol in input_sequence:
            if input_symbol not in self.__alphabet:
                raise ValueError(f"Invalid input symbol: {input_symbol}")
            self.transition(input_symbol)

    def get_current_state(self) -> StateType:
        """
        Returns the current state of the FSM.

        Returns:
            The current state.
        """
        return self.current_state

    def is_in_final_state(self) -> bool:
        """
        Checks if the FSM is currently in one of the final states.

        Returns:
            bool: True if the current state is a final state, False otherwise.
        """
        return self.current_state in self.__final_states

    def get_final_state(self) -> StateType:
        """
        Returns the final state if the current state is a final state.

        Returns:
            The current state if it's a final state.

        Raises:
            ValueError: If the current state is not a final state.
        """
        if self.is_in_final_state():
            return self.current_state
        else:
            raise ValueError(f"Current state {self.current_state} is not a final state.")

    def reset(self) -> None:
        """
        Resets the FSM to the initial state.
        """
        self.current_state = self.__initial_state
