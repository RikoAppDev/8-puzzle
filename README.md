# 8-Puzzle Solver

This project implements an 8-puzzle solver using bidirectional search.

## Introduction

The 8-puzzle is a sliding puzzle that consists of a 3x3 grid with numbered tiles and one blank space. The objective is
to rearrange the tiles to match a target configuration.

## Installation and Running

1. **Clone the repository:**
   ```bash
   git clone https://github.com/RikoAppDev/8-puzzle.git
   cd 8-puzzle
   ```
2. **Run the solver:**
    ```bash
    python main.py
    ```

## Usage

1. The program takes the initial and goal state of the 8-puzzle as input.
2. The solver uses bidirectional search to find the solution.
3. The solution path is printed as a sequence of moves.

## User Guide

The program is designed with minimal user interface, so for correct execution and results, you need to check the
constants.py file. This file contains predefined possible inputs and outputs mainly for the 8-puzzle (3x3 grid).

If you wish to change the DEFAULT_INPUT or DEFAULT_OUTPUT, you need to comment and uncomment the appropriate
configurations. For custom DEFAULT_INPUT or DEFAULT_OUTPUT, use the following template, where the empty space is
represented by -1:

```python
DEFAULT_INPUT = [[ , , ], [ , , ], [ , , ]]
```

The program is also designed to work for the 15-puzzle (4x4 grid). The program architecture should support larger grids.

For the 15-puzzle, you need to comment out M=3 and N=3 for rows and columns, and uncomment M=4 and N=4. Similarly,
comment out DEFAULT_INPUT and DEFAULT_OUTPUT for the 8-puzzle and uncomment them for the 15-puzzle.

## Testing Results

The results of the solver have been tested against online 8-puzzle solvers. The resulting sequences of moves were
consistent with the expected solutions.

## Documentation

For detailed documentation, please check [Technical Documentation](Dokumentacia_UI_P1.pdf) in the repository.
