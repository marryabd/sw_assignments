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
│   │   │   └── functions.py
│   ├── run_assignment1.py
│   ├── tests/             # Unit tests for assignment 1
│   │   └── test_best_threshold.py
│   └── run_test_assignment1.ipynb      # Jupyter notebook for running the tests
│
├── assignment2/
│   ├── src/
│   │   ├── my_module2/    # Package for assignment 2
│   │   │   ├── __init__.py
│   │   │   ├── fsm.py
│   │   │   └── mod_three_fsm.py
│   ├── run_assignment2.py
│   ├── tests/             # Unit tests for assignment 2
│   │   ├── test_mod_three_fsm.py
│   │   └── test_fsm.py
│   └── run_test_assignment2.ipynb      # Jupyter notebook for running the tests
│
├── setup.py               # Project installation script
└── README.md              # Project overview and instructions
```

## Installation

To set up the project, follow these steps:

1. **Clone the Repository**: Clone the repository to your local machine.
    ```bash
    git clone https://github.com/marryabd/sw_assignments.git
    cd sw_assignments
    ```

2. **Create a Virtual Environment**: It is recommended to use a virtual environment to manage dependencies.
    ```bash
     python -m venv venv
    ```
    **Activate the Virtual Environment** depending on your operating system:
     - **On Linux/macOS**:
      ```bash
     source venv/bin/activate
      ```
     - **On Windows (Git Bash)**:
     ```bash
     source venv/Scripts/activate
     ```
     - **On Windows (Command Prompt)**:
    ```bash
     venv\Scripts\activate
    ```

3. **Install the Project**: Use `pip` to install the project and its dependencies.
    ```bash
    pip install .
    ```

This will install all the necessary dependencies and set up the project for further development or testing.

---

## Assignment 1: find_best_threshold

The **find_best_threshold** function evaluates classification thresholds by calculating recall and precision based on true positives (TP), false negatives (FN), true negatives (TN), and false positives (FP). It returns the best threshold where recall >= 0.9 and maximizes precision (if FP is provided).

- **Report, Examples, and Edge Cases**: Refer to `run_assignment1.py` inside the `assignment1/` folder for a detailed report, including the logic explanation, examples, and edge cases that demonstrate the function’s behavior.

---

## Assignment 2: Finite State Machine and ModThreeFSM

The **FiniteStateMachine** class implements a generic FSM framework with encapsulated attributes like states, alphabet, transitions, and final states. The **ModThreeFSM** subclass specializes in computing the remainder when dividing a binary number by 3.

- **Report, Examples, and Edge Cases**: Refer to `run_assignment2.py` inside the `assignment2/` folder for a detailed report, including examples of how to use the FSM and ModThreeFSM classes and how the design follows Object-Oriented Design (OOD) principles.

---

## Running the Tests

Each assignment has its own tests organized in the respective `tests/` folder.

- **Assignment 1 Tests**: The tests for the `find_best_threshold` function are located in `assignment1/tests/test_functions.py`.
- **Assignment 2 Tests**: The tests for the FSM and ModThreeFSM classes are located in `assignment2/tests/test_fsm.py` and `assignment2/tests/test_mod_three_fsm.py`.

To run the tests, use the following command inside each assignment folder:

```bash
# Inside assignment1/ or assignment2/
python -m unittest discover tests
```
Alternatively, you can view the test results interactively:

- **Assignment 1**: In the `run_test_assignment1.ipynb` notebook inside the `assignment1/` folder.
- **Assignment 2**: In the `run_test_assignment2.ipynb` notebook inside the `assignment2/` folder.


---

## Dependencies

The project uses standard Python libraries like `unittest` and `warnings`, which come with Python. No additional third-party libraries are required for running the tests or using the functionality provided.


