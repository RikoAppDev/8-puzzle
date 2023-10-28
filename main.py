from timeit import default_timer as timer

from Game import *


def show_solution(s_node, e_node):
    start_moves = []
    end_moves = []

    while s_node.previous is not None:
        start_moves.append(s_node.move)
        s_node = s_node.previous

    while e_node.previous is not None:
        end_moves.append(e_node.move)
        e_node = e_node.previous

    start_moves.reverse()

    help_move = ""
    if len(end_moves) != 0:
        help_move = OPPOSITE_MOVE[end_moves[0].value]
        end_moves.pop(0)

    print("\r------------ SOLUTION STEPS ------------")

    print("INITIAL STATE:")
    game.print_game_field(game.game_field_start)

    step = 1

    if len(end_moves) != 0:
        for node_move in start_moves:
            print(f"STEP: {step} | MOVE: {MOVE[node_move.value]}")
            game.print_game_field(node_move.game_board_state)
            step += 1
    else:
        print(f"STEP: {step} | MOVE: {MOVE[start_moves[0].value]}")
        print("FINAL STATE:")
        game.print_game_field(start_moves[0].game_board_state)

    if len(end_moves) != 0:
        print(f"STEP: {step} | MOVE: {help_move}")
        for node_move in end_moves:
            game.print_game_field(node_move.game_board_state)
            step += 1
            print(f"STEP: {step} | MOVE: {OPPOSITE_MOVE[node_move.value]}")

        print("FINAL STATE:")
        game.print_game_field(game.game_field_end)

    if step >= 2:
        print(f"Game solved in {step} steps.")
    else:
        print(f"Game solved in {step} step.")

    print("----------------------------------------")
    print(f"       Created start nodes: {len(created_start_nodes)}")
    print(f"         Created end nodes: {len(created_end_nodes)}")
    print(f"         ALL created nodes: {len(created_start_nodes) + len(created_end_nodes)}")
    print(f"    Controlled start nodes: {len(controlled_start_nodes)}")
    print(f"      Controlled end nodes: {len(controlled_end_nodes)}")
    print(f"      ALL controlled nodes: {len(controlled_start_nodes) + len(controlled_end_nodes)}")
    print(f"            Execution time: {format((end - start) * 1000, '.2f')} milliseconds")
    print("----------------------------------------")
    exit(0)


# Setup
game = Game(DEFAULT_INPUT, DEFAULT_OUTPUT)

created_start_nodes = []
created_end_nodes = []
uncontrolled_start_nodes = []
uncontrolled_end_nodes = []
controlled_start_nodes = []
controlled_end_nodes = []

actual_start_node = game.start_node
actual_end_node = game.end_node

created_start_nodes.append(actual_start_node)
created_end_nodes.append(actual_end_node)
uncontrolled_start_nodes.append(actual_start_node)
uncontrolled_end_nodes.append(actual_end_node)

is_game_finished = False
counter = 0

if game.game_field_start == game.game_field_end:
    uncontrolled_start_nodes.remove(actual_start_node)
    uncontrolled_end_nodes.remove(actual_end_node)
    controlled_start_nodes.append(actual_start_node)
    controlled_end_nodes.append(actual_end_node)
    print("Game is already solved! No moves needed.")
else:
    start = timer()
    print("Still looking for a solution | LOADING: |", end="")

    while not is_game_finished:
        counter += 1

        if len(uncontrolled_start_nodes) == 0 or len(uncontrolled_end_nodes) == 0:
            print("\rError: Game cannot be solved!")
            exit("Solution does not exist!")

        start_child = []
        for actual_start_node in uncontrolled_start_nodes:
            for move in game.get_possible_moves(actual_start_node.move.game_board_state):
                new_node = Node(actual_start_node, [], move)

                if new_node.previous.previous is not None:
                    if new_node.move.game_board_state != new_node.previous.previous.move.game_board_state:
                        actual_start_node.children.append(new_node)
                        created_start_nodes.append(new_node)
                        start_child.append(new_node)
                else:
                    actual_start_node.children.append(new_node)
                    created_start_nodes.append(new_node)
                    start_child.append(new_node)

            controlled_start_nodes.append(actual_start_node)
            uncontrolled_start_nodes.remove(actual_start_node)

        uncontrolled_start_nodes.extend(start_child)

        for start_node in uncontrolled_start_nodes:
            actual_start_node = start_node

            for uncontrolled_end_node in uncontrolled_end_nodes:
                if start_node.move.game_board_state == uncontrolled_end_node.move.game_board_state:
                    end = timer()
                    is_game_finished = True
                    show_solution(start_node, uncontrolled_end_node)

        end_child = []
        for actual_end_node in uncontrolled_end_nodes:
            for move in game.get_possible_moves(actual_end_node.move.game_board_state):
                new_node = Node(actual_end_node, [], move)

                if new_node.previous.previous is not None:
                    if new_node.move.game_board_state != new_node.previous.previous.move.game_board_state:
                        actual_end_node.children.append(new_node)
                        created_end_nodes.append(new_node)
                        end_child.append(new_node)
                else:
                    actual_end_node.children.append(new_node)
                    created_end_nodes.append(new_node)
                    end_child.append(new_node)

            controlled_end_nodes.append(actual_end_node)
            uncontrolled_end_nodes.remove(actual_end_node)

        uncontrolled_end_nodes.extend(end_child)

        for end_node in uncontrolled_end_nodes:
            actual_end_node = end_node

            for uncontrolled_start_node in uncontrolled_start_nodes:
                if end_node.move.game_board_state == uncontrolled_start_node.move.game_board_state:
                    end = timer()
                    is_game_finished = True
                    show_solution(uncontrolled_start_node, end_node)

        print("|", end="")

        if counter == 100:
            print("\rError: Game cannot be solved!")
            exit("Too much operations!")

        if (timer() - start) > 20:
            print("\rError: Game cannot be solved!")
            exit("Solution does not exist!")
