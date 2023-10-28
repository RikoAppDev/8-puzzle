import copy

from constants import *


class Move:
    def __init__(self, value, game_board_state):
        self.value = value
        self.game_board_state = game_board_state


class Node:
    def __init__(self, previous, children: list, move: Move):
        self.previous: Node = previous
        self.children: list[Node] = children
        self.move: Move = move


class Game:
    def __init__(self, default_input: list, default_output: list):
        self.game_field_start: list = default_input
        self.game_field_end: list = default_output
        self.start_node: Node = Node(None, [], Move(None, self.game_field_start))
        self.end_node: Node = Node(None, [], Move(None, self.game_field_end))

    @staticmethod
    def print_game_field(game_field):
        for row in game_field:
            for col in row:
                if col == VOID:
                    print(" ■ ", end=""),
                else:
                    print(f"{col:>2} ", end=""),
            print()
        print()

    @staticmethod
    def print_both_game_field(game_board_start, game_board_end):
        print("START:\t\tEND:")
        for i in range(0, M):
            row = game_board_start[i] + game_board_end[i]
            space = 0
            for col in row:
                if space == N:
                    print("   ", end="")

                if col == VOID:
                    print("■  ", end=""),
                else:
                    print(f"{col}  ", end=""),
                space += 1
            print()
        print()

    @staticmethod
    def find_void(game_field):
        i = 0
        j = 0
        for row in game_field:
            for col in row:
                if col == VOID:
                    return [i, j]
                j += 1
            i += 1
            j = 0

    def get_possible_moves(self, game_field: list):
        moves: [Move] = []

        possible_down_move = self.down(copy.deepcopy(game_field))
        possible_up_move = self.up(copy.deepcopy(game_field))
        possible_left_move = self.left(copy.deepcopy(game_field))
        possible_right_move = self.right(copy.deepcopy(game_field))

        if possible_down_move != game_field:
            moves.append(Move(0, possible_down_move))
        if possible_up_move != game_field:
            moves.append(Move(1, possible_up_move))
        if possible_left_move != game_field:
            moves.append(Move(2, possible_left_move))
        if possible_right_move != game_field:
            moves.append(Move(3, possible_right_move))

        return moves

    def down(self, game_field):
        void = self.find_void(game_field)
        x = void[0]
        y = void[1]

        if x == 0:
            return game_field
        else:
            game_field[x][y] = game_field[x - 1][y]
            game_field[x - 1][y] = VOID
            return game_field

    def up(self, game_field):
        void = self.find_void(game_field)
        x = void[0]
        y = void[1]

        if x == M - 1:
            return game_field
        else:
            game_field[x][y] = game_field[x + 1][y]
            game_field[x + 1][y] = VOID
            return game_field

    def right(self, game_field):
        void = self.find_void(game_field)
        x = void[0]
        y = void[1]

        if y == 0:
            return game_field
        else:
            game_field[x][y] = game_field[x][y - 1]
            game_field[x][y - 1] = VOID
            return game_field

    def left(self, game_field):
        void = self.find_void(game_field)
        x = void[0]
        y = void[1]

        if y == N - 1:
            return game_field
        else:
            game_field[x][y] = game_field[x][y + 1]
            game_field[x][y + 1] = VOID
            return game_field
