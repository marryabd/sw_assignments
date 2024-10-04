 # Finite State Machine and find_best_threshold Function Assignments

This project contains two assignments:

1. **Assignment 1**: Implementation of the **find_best_threshold** function, which finds the optimal threshold for machine learning classification problems based on recall and precision metrics using TP, TN, FP, and FN.
2. **Assignment 2**: Implementation of a **Finite State Machine (FSM)** and a specialized subclass, **ModThreeFSM**, to compute the remainder when dividing a binary number by 3.

Both assignments follow **Object-Oriented Design (OOD)** principles and are tested thoroughly using Python's `unittest` framework.

---

## Project Structure

```plaintext
my_project/
│
├── assignment1/
│   ├── src/
│   │   ├── my_module1/    # Package for assignment 1
│   │   │   ├── __init__.py
│   │   │   ├── functions.py
│   │   │   └── classes.py
│   ├── run_assignment1.py
│   ├── tests/             # Unit tests for assignment 1
│   │   └── test_functions.py
│   └── run_test.ipynb      # Jupyter notebook for running the tests
│
├── assignment2/
│   ├── src/
│   │   ├── my_module2/    # Package for assignment 2
│   │   │   ├── __init__.py
│   │   │   ├── functions.py
│   │   │   └── classes.py
│   ├── run_assignment2.py
│   ├── tests/             # Unit tests for assignment 2
│   │   └── test_fsm.py
│   └── run_test.ipynb      # Jupyter notebook for running the tests
│
├── setup.py               # Project installation script
└── README.md              # Project overview and instructions

## Installation

To set up the project, follow these steps:

1. **Clone the Repository**: Clone the repository to your local machine.
    ```bash
    git clone https://github.com/your-repo/your-project.git
    cd your-project
    ```

2. **Create a Virtual Environment**: It is recommended to use a virtual environment to manage dependencies.
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate
    ```

3. **Install the Project**: Use `pip` to install the project and its dependencies.
    ```bash
    pip install .
    ```

This will install all the necessary dependencies and set up the project for further development or testing.

---

## Running the Tests

Each assignment has its own tests organized in the respective `tests/` folder.

- **Assignment 1 Tests**: The tests for the `find_best_threshold` function are located in `assignment1/tests/test_functions.py`.
- **Assignment 2 Tests**: The tests for the FSM and ModThreeFSM classes are located in `assignment2/tests/test_fsm.py`.

To run the tests, use the following command inside each assignment folder:

```bash
# Inside assignment1/ or assignment2/
python -m unittest discover tests

## Assignment 1: find_best_threshold

The **find_best_threshold** function evaluates classification thresholds by calculating recall and precision based on true positives (TP), false negatives (FN), true negatives (TN), and false positives (FP). It returns the best threshold where recall >= 0.9 and maximizes precision (if FP is provided).

- **Examples and Edge Cases**: Refer to `run_assignment1.py` or `run_test.ipynb` inside the `assignment1/` folder to see examples of this function and the corresponding test cases.

---

## Assignment 2: Finite State Machine and ModThreeFSM

The **FiniteStateMachine** class implements a generic FSM framework with encapsulated attributes like states, alphabet, transitions, and final states. The **ModThreeFSM** subclass specializes in computing the remainder when dividing a binary number by 3.

- **Usage**: Refer to `run_assignment2.py` or `run_test.ipynb` inside the `assignment2/` folder for examples of how to use the FSM and ModThreeFSM classes and run tests.

---

## Dependencies

The following dependencies will be installed via `pip install .`:

- **unittest**: For running the unit tests (standard library).
- **warnings**: For generating warnings (standard library).

---

## Conclusion

This project demonstrates the practical application of **Object-Oriented Design (OOD)** principles across two assignments: optimizing machine learning classification thresholds and implementing a flexible FSM framework for specific use cases like binary remainder computation.

