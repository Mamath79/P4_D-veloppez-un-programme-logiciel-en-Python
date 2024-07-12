from models.tournament_model import TournamentModel
from models.game_model import GameModel
from views.message_view import MessageView
import random


class GameController:
    def __init__(self) -> None:
        pass

    @staticmethod
    def generate_game(selected_tournament_id):
        # recuperation du dict du tournois choisi par ID
        selected_tournament_data = (
            TournamentModel.access_tournament_data_id(
                selected_tournament_id))

        # securité en cas de none existance du tournois avec l'id selectionnée
        if not selected_tournament_data:
            MessageView.display_no_tournament_found(selected_tournament_id)

        # recuperation de la liset des joueurs enregistrés.
        registered_players = (
            selected_tournament_data.get('registered_players')
            )

        # verification du nombre minimun de jouers pour un tournois
        if len(registered_players) < 2:
            MessageView.display_not_enough_players()
            return

        # a l'interieur du tournois selectionné ,
        # recuperation de la liste des rounds + verif d'existance

        selected_round = (
            selected_tournament_data.get('rounds')
            )
        if not selected_round:
            MessageView.display_no_round_found(selected_tournament_id)
            return

        # recuperartion current round
        current_round = selected_tournament_data.get("current_round")
        selected_round_info = selected_round[int(current_round) - 1]

        # creation des premiers match du premier round avec
        # attributions des paires de façon aleatoire.
        if current_round == 1:
            # copie de la liste des joueurs enregistrés pour manipulation
            registered_players_copy = registered_players.copy()
            games = []
            game_id = 1

            while len(registered_players_copy) >= 2:

                gamer_1 = random.choice(registered_players_copy)
                registered_players_copy.remove(gamer_1)
                gamer_2 = random.choice(registered_players_copy)
                registered_players_copy.remove(gamer_2)

                game = GameModel(game_id=game_id,
                                 gamer_1=gamer_1,
                                 color_gamer_1="",
                                 score_gamer_1=0,
                                 gamer_2=gamer_2,
                                 color_gamer_2="",
                                 score_gamer_2=0,
                                 )

                game.game_assign_colors()
                new_game = (
                    GameModel.game_convert_to_dict(game))
                games.append(new_game)
                game_id += 1

        # creation des match suivants pour les rounds suivants
        # avec attributions des paires en fonction du classement des joueurs.
        else:
            # copie de la liste des joueurs enregistrés pour manipulation
            registered_players_copy = registered_players.copy()
            games = []
            game_id = 1

            # recuperation du ranking
            ranking = selected_tournament_data.get("ranking")
            ranking_sorted = sorted(
                ranking, key=lambda x: x["player_ranking"])

            # recuperation des precedents match joués
            previous_game = []
            for round_data in selected_round:
                for game in round_data.get("games", []):
                    previous_game.append(
                        (game["gamer_1"], game["gamer_2"]))

            # choix des joueurs du nouveau match par rapport au classement
            for i in range(0, len(ranking_sorted), 2):
                player_1 = ranking_sorted[i]["player_id"]
                player_2 = ranking_sorted[i+1]["player_id"]

                # verification pour savoir si le match a deja ete joué,
                # et si oui ne pas generer la paire
                for potential_opponent in registered_players_copy:
                    if (player_1, potential_opponent) in previous_game or \
                            (potential_opponent, player_1) in previous_game:
                        player_2 = potential_opponent
                    break

                # creation du match par appel de la class game
                game = GameModel(game_id=game_id,
                                 gamer_1=player_1,
                                 color_gamer_1="",
                                 score_gamer_1=0,
                                 gamer_2=player_2,
                                 color_gamer_2="",
                                 score_gamer_2=0)
                game.game_assign_colors()
                new_game = GameModel.game_convert_to_dict(game)
                games.append(new_game)
                game_id += 1

        # maj des matchs dans le current round
        selected_round_info["games"] = games
        selected_round[int(current_round) - 1] = selected_round_info

        # insertion du game model dans la db par remontée d'étape
        selected_tournament_data["rounds"] = selected_round
        TournamentModel.update_tournament_data_by_id(
            selected_tournament_id, selected_tournament_data)
