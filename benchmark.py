from checker_model import CheckerModel
import tqdm
import time



number_games_to_test = 10_000
wins_player_1 = 0
wins_player_2 = 0


for _ in tqdm.tqdm(range(number_games_to_test)):
	checker_model_object = CheckerModel()

	while True:
		checker_model_object.ia_move(model="random")
		game_state = checker_model_object.check_game_state()
		if game_state == "draw_game":
			break
		
		elif game_state == 1:
			wins_player_1 +=1
			break


		checker_model_object.ia_move(model="minimax")
		game_state = checker_model_object.check_game_state()
		if game_state == "draw_game":
			break
		
		elif game_state == -1:
			wins_player_2 +=1
			break


print(f"player 1  wins {wins_player_1}")
print(f"player 2  wins {wins_player_2}")
print(f"draws {number_games_to_test - wins_player_1 - wins_player_2}")

# Création d'une instance du modèle
model = CheckerModel()

# Position initiale ou position de test
position = model.create_grid()

# Démarrer le chronomètre
start_time = time.time()

# Exécution de l'algorithme de Monte Carlo pour choisir un coup
best_move = model.choose_best_move(position)

# Arrêter le chronomètre
end_time = time.time()

# Calculer et afficher le temps écoulé
print(f"Temps nécessaire pour choisir un coup : {end_time - start_time} secondes")