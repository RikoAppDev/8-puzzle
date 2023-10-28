# 8-Puzzle
# ROW = M, COL = N
M = 3
N = 3
VOID = -1

# Default input for a solvable 8-Puzzle (0 steps to solve)
# DEFAULT_INPUT = [[1, 2, 3], [4, 5, 6], [7, 8, -1]]
# Default input for a solvable 8-Puzzle (16 steps to solve)
DEFAULT_INPUT = [[1, 2, 3], [4, -1, 5], [6, 7, 8]]
# Default input for a solvable 8-Puzzle (3 steps to solve)
# DEFAULT_INPUT = [[1, -1, 2], [4, 5, 3], [7, 8, 6]]
# Default input for a solvable 8-Puzzle (4 steps to solve)
# DEFAULT_INPUT = [[-1, 1, 2], [4, 5, 3], [7, 8, 6]]
# Default input for a solvable 8-Puzzle (3 steps to solve)
# DEFAULT_INPUT = [[1, 2, 3], [-1, 4, 5], [7, 8, 6]]
# Default input for a solvable 8-Puzzle (3 steps to solve)
# DEFAULT_INPUT = [[1, 2, 3], [-1, 4, 6], [7, 5, 8]]
# Default input for a solvable 8-Puzzle (unsolvable)
# DEFAULT_INPUT = [[4, -1, 2], [3, 1, 5], [7, 8, 6]]
# Default input for a solvable 8-Puzzle (33 steps to solve)
# DEFAULT_INPUT = [[3, 7, 1], [6, 2, 8], [4, -1, 5]]
# Default input for a solvable 8-Puzzle (23 steps to solve)
# DEFAULT_INPUT = [[7, -1, 8], [3, 2, 1], [6, 5, 4]]
# Default input for a solvable 8-Puzzle (unsolvable)
# DEFAULT_INPUT = [[-1, 2, 3], [1, 4, 5], [8, 7, 6]]
# Default input for a solvable 8-Puzzle (1 step to solve)
# DEFAULT_INPUT = [[1, 2, 3], [4, 5, -1], [7, 8, 6]]
# Default input for a solvable 8-Puzzle (1 step to solve)
# DEFAULT_INPUT = [[1, 2, 3], [4, 5, 6], [7, -1, 8]]

# Default output for 8-Puzzle
DEFAULT_OUTPUT = [[1, 2, 3], [4, 5, 6], [7, 8, -1]]
# DEFAULT_OUTPUT = [[-1, 8, 7], [6, 5, 4], [3, 2, 1]]

# 15-Puzzle
# ROW = M, COL = N
# M = 4
# N = 4

# Default input for a solvable 15-Puzzle (8 step to solve)
# DEFAULT_INPUT = [[1, 2, -1, 4], [5, 6, 3, 8], [9, 10, 7, 15], [13, 14, 12, 11]]
# Default output for a 15-Puzzle
# DEFAULT_OUTPUT = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, -1]]

MOVE = ("DOWN", "UP", "LEFT", "RIGHT")
OPPOSITE_MOVE = ("UP", "DOWN", "RIGHT", "LEFT")
