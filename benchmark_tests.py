import random
from checker_model import CheckerModel
from minimax_model import MinimaxModel
from random_model import RandomModel


def play_game(player1, player2):
    game = CheckerModel()
    current_player = player1

    while not game.is_game_over():
        move = current_player.get_move(game)
        game.apply_move(move)
        current_player = player2 if current_player == player1 else player1

    return game.get_winner()


def test_agents(depths, num_games=10):
    results = {depth: {'minimax_wins': 0, 'random_wins': 0} for depth in depths}

    for depth in depths:
        minimax_agent = MinimaxModel(depth)
        random_agent = RandomModel()

        for _ in range(num_games):
            if random.choice([True, False]):
                winner = play_game(minimax_agent, random_agent)
            else:
                winner = play_game(random_agent, minimax_agent)

            if winner == 'minimax':
                results[depth]['minimax_wins'] += 1
            elif winner == 'random':
                results[depth]['random_wins'] += 1

    return results


# Test with depths 1, 2, 3, and 4
depths = [1, 2, 3, 4]
results = test_agents(depths)
print(results)
