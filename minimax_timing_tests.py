import time
from checker_model import CheckerModel
from minimax_model import MinimaxModel


def play_game(player1, player2):
    game = CheckerModel()
    current_player = player1

    while not game.is_game_over():
        move = current_player.get_move(game)
        game.apply_move(move)
        current_player = player2 if current_player == player1 else player1

    return game.get_winner()  # Assume this function returns the winner


def test_agents(depth1, depth2, num_games=10):
    results = {'player1_wins': 0, 'player2_wins': 0, 'draws': 0}
    execution_times = []

    for _ in range(num_games):
        player1 = MinimaxModel(depth1, maximize=True)
        player2 = MinimaxModel(depth2, maximize=False)

        start_time = time.time()
        winner = play_game(player1, player2)
        end_time = time.time()

        execution_times.append(end_time - start_time)

        if winner == 'player1':
            results['player1_wins'] += 1
        elif winner == 'player2':
            results['player2_wins'] += 1
        else:
            results['draws'] += 1

    average_time = sum(execution_times) / len(execution_times)
    return results, average_time


# Example test between depths 2 and 3
depth1 = 2
depth2 = 3
results, avg_time = test_agents(depth1, depth2)
print(f"Results for Minimax depth {depth1} vs Minimax depth {depth2}: {results}")
print(f"Average execution time: {avg_time:.2f} seconds")
