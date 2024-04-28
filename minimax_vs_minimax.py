from checker_model import CheckerModel
from minimax_model import MinimaxModel


def play_game(player1, player2):
    game = CheckerModel()
    current_player = player1

    while not game.is_game_over():
        move = current_player.get_move(game)
        game.apply_move(move)
        current_player = player2 if current_player == player1 else player1

    return game.get_winner()


def test_agents(depth1, depth2, num_games=10):
    results = {'player1_wins': 0, 'player2_wins': 0, 'draws': 0}

    for _ in range(num_games):
        player1 = MinimaxModel(depth1, maximize=True)  # Maximizing for player 1
        player2 = MinimaxModel(depth2, maximize=False)  # Minimizing for player 2

        winner = play_game(player1, player2)

        if winner == 'player1':
            results['player1_wins'] += 1
        elif winner == 'player2':
            results['player2_wins'] += 1
        else:
            results['draws'] += 1

    return results


# Example test between depths 2 and 3
depth1 = 2
depth2 = 3
results = test_agents(depth1, depth2)
print(f"Results for Minimax depth {depth1} vs Minimax depth {depth2}: {results}")
