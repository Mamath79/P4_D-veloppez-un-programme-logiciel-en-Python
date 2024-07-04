from models.tournament_model import TournamentModel
from models.player_model import PlayerModel
from views.report_view import ReportView
from views.menu_view import MenuView
from datetime import datetime
from tinydb import Query
from controllers.round_controller import RoundController
from controllers.game_controller import GameController


class TournamentController:

    def __init__(self):
        pass

    def generate_ID_tournament(self):

        # recuperation de l'id des id de tournois precedents , si ils existent,
        # pour incrementer l'id du nouveau tournois

        data = TournamentModel.tournament_db()
        keys = []
        for doc in data.all():
            keys.append(int(doc.get("ID_tournament", 0)))

        highest_key = max(keys) if keys else 0
        ID_tournament = highest_key + 1
        tournament = TournamentModel(ID_tournament=ID_tournament)
        return tournament

    def create_metadata(self, tournament: TournamentModel):

        # creation des metadata du nouveau tournois

        new_name = input("\nEnter new tournament's name : ")
        new_location = input("Enter new tournament's location : ")
        new_start_date = input(
            "Enter new tournament's start date (yyyy-mm-dd) : ")
        new_end_date = input("Enter new tournament's end date (yyyy-mm-dd) : ")
        new_description = input("Enter new tournament's description : ")

        tournament.name = new_name
        tournament.location = new_location
        tournament.start_date = new_start_date
        tournament.end_date = new_end_date
        tournament.description = new_description

        return tournament

    def choose_players(self, tournament: TournamentModel):

        # selection des participants dans la liste des joueurs déjà créée.
        players = PlayerModel.player_db().all()
        available_players = players.copy()
        ReportView.view_list_all_players(available_players)
        user_input = input(
            "\nselect tournament's players ( 2, 4, 6 or 8) or exit to return: ")

        # si exit fourni par l'utilisateur
        if user_input.lower() == "exit":
            MenuView.tournament_menu()

        try:
            user_input = int(user_input)
            if user_input not in [2, 4, 6, 8]:
                print("please select 2,4,6 or 8 players")
                return self.choose_players(tournament)
        except ValueError:
            print(
                "Invalid input,please enter a number (2, 4, 6, or 8) .")
            return self.choose_players(tournament)

        selected_players = []
        while len(selected_players) < user_input:
            
            print("\n ####  Availabble player list  ####\n")
            ReportView.view_list_all_players(available_players)

            player_id = input(f"Select player {len(selected_players) + 1} ID: ")
            if not PlayerModel.check_player_id(player_id):
                print("Id doesn't correspond to a registered player ")
                continue

            elif player_id in selected_players:
                print("player already add in the tournament, please select another player")
                continue

            else:
                selected_players.append(player_id)
                updated_available_players = []
                for player in available_players:
                    if str(player['ID']) != player_id:
                        updated_available_players.append(player)
                available_players = updated_available_players
                   

        tournament.set_players(selected_players)
        return tournament

    def add(self):

        tournament = self.generate_ID_tournament()
        tournament = self.create_metadata(tournament)
        tournament = self.choose_players(tournament)

        TournamentModel.save(tournament)

    def update():
        pass

        # implementer tournament edit pour les
        # infos du tournois ou les joueurs selectionnés

        print("\n ##### UPDATE EXISTING TOURNAMENT #####")

    @staticmethod
    def recall_tournament_db():
        # methode permettant de rappler la db tournoi
        TournamentModel.tournament_db()

    @staticmethod
    def access_tournament_data_by_id(selected_tournament_id):
        # méthode permettant d'acceder aux données d'un
        # tournois specifique choisi par son id.

        data = TournamentModel.tournament_db()
        tournament = Query()
        selected_tournament_data = data.get(
            tournament.ID_tournament == int(selected_tournament_id)
            )
        return selected_tournament_data

    @staticmethod
    def edit_display_current_round(selected_tournament_id):
        # methode permettant de mettre à jour le cuurent id necessaire
        # pour la creation des matches et l'edit de ses derniers

        selected_tournament_data = TournamentModel.access_tournament_data_id(
            selected_tournament_id)
        if not selected_tournament_data:
            print("no tournament found with this id")
            return

        rounds_list = selected_tournament_data.get("rounds")

        if not rounds_list:
            print(" no round started yet in this tournament")

        else:
            rounds_ids = []
            for item in rounds_list:
                rounds_ids.append(item.get("round_id"))

            highest_round_id = max(rounds_ids)
            selected_tournament_data["current_round"] = highest_round_id
            TournamentModel.update_tournament_data_by_id(
                selected_tournament_id, selected_tournament_data)
            return (selected_tournament_data.get('current_round'))

    @staticmethod
    def display_list_all_tournaments():
        # methode permettant l'affichage sous forme de tableau
        # de tous les tournois existants
        data = TournamentModel.tournament_db()
        ReportView.view_list_all_tournaments(data)
        TournamentModel.sorted_tournament_list()

    @staticmethod
    def display_selected_tournament(selected_tournament_id):
        # methode servant a afficher une vue resumé d'un tournois
        # selectionné par son id.

        result = TournamentModel.check_tournament_id(selected_tournament_id)
        if not result:
            print("No tournament found with the provided ID.")

        else:
            selected_tournament_data = result
            round_info = selected_tournament_data.get("rounds")
            ReportView.view_rounds_and_games(round_info)

    @staticmethod
    def navigate_selected_tournament():

        data = TournamentModel.tournament_db()
        if not data:
            print("No tournament created yet. Please create one")
            return

        ReportView.view_list_all_tournaments(data)
        selected_tournament_id = input(
            "\nEnter the ID of the tournament to display: ")

        data = TournamentModel.access_tournament_data_id(
            selected_tournament_id)
        selected_tournament_data = data
        if not selected_tournament_data:
            print("Invalid tournament id")
            return

        ReportView.header_info_selected_tournament(
            selected_tournament_data)

        while True:
            TournamentController.edit_display_current_round(
                selected_tournament_id)

            # recuperation de current_id
            current_round = selected_tournament_data.get(
                "current_round")

            if not current_round:
                user_input = input(
                    "\ndo you want to start the first/next round"
                    "and the first/next game ? (y/n): ")

                if user_input.lower() == "y":
                    TournamentController.set_ranking(
                        selected_tournament_id)
                    RoundController.generate_round(
                        selected_tournament_id)
                    TournamentController.edit_display_current_round(
                        selected_tournament_id)
                    GameController.generate_game(
                        selected_tournament_id)

                    print("\n\nRound_1 and games have been genereted.\n")

                    TournamentController.display_selected_tournament(
                        selected_tournament_id)

                    return TournamentController.navigate_selected_tournament()

                elif user_input.lower() == "n":
                    return

                else:
                    print("Invalid user input")

            else:
                TournamentController.display_selected_tournament(
                    selected_tournament_id)
                TournamentController.display_ranking(
                    selected_tournament_id)
                print("\n[1] edit/end current round")
                print("[2] start next round")
                print("\n[exit] return to tournament menu")

                user_input = input("\nenter your choice: ")

                if user_input == "1":
                    TournamentController.edit_end_current_round(
                        selected_tournament_id)
                    TournamentController.update_players_score_and_ranking(
                        selected_tournament_id)

                elif user_input == "2":
                    RoundController.generate_round(selected_tournament_id)

                    user_input = input(
                        "\ndo you want to start the next game ? (y/n): \n")

                    if user_input == "y":
                        TournamentController.edit_display_current_round(
                            selected_tournament_id)
                        GameController.generate_game(
                            selected_tournament_id)

                    elif user_input == "n":
                        return

                    else:
                        print("Invalid user input")

                elif user_input == "exit":
                    return

                else:
                    print("Invalid user input")

    @staticmethod
    def edit_end_current_round(selected_tournament_id):
        # récuperation du dict du tournois choisi par ID
        selected_tournament_data = TournamentModel.access_tournament_data_id(
            selected_tournament_id)

        # à l'interieur du tournois selectionné ,
        # recuperation de la liste des rounds
        rounds_list = selected_tournament_data.get('rounds')

        # récuperation du tournois a editer grace au current round id
        current_round = TournamentController.edit_display_current_round(
            selected_tournament_id)

        selected_round = rounds_list[int(current_round - 1)]

        selected_game = selected_round['games']

        user_input = input(
            "Do you want to end the game and edit scores ? (y/n): ")

        end_time = {'end_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

        if user_input.lower() == "y":
            for game in selected_game:
                try:
                    user_input_2 = float(input(
                        f"Please enter {game["gamer_1"]}'s score win = 1,"
                        "loose = 0 , tie = 0.5:"))
                except ValueError:
                    print("invalid entry please select win:1,"
                          "loose:0 or tie: 0.5")
                    return

                if user_input_2 not in [1, 0, 0.5]:
                    print("invalid entry please select win:1,"
                          "loose:0 or tie: 0.5")
                    return

                else:
                    score_gamer_1 = user_input_2
                    if score_gamer_1 == 1:
                        game_score = {'score_gamer_1': 1,
                                      'score_gamer_2': 0}
                    elif score_gamer_1 == 0:
                        game_score = {'score_gamer_1': 0,
                                      'score_gamer_2': 1}
                    elif score_gamer_1 == 0.5:
                        game_score = {'score_gamer_1': 0.5,
                                      'score_gamer_2': 0.5}
                    else:
                        print("invalid entry please select 0 or 1 or 0.5")
                        return

                    game.update(game_score)

            rounds_list[int(current_round - 1)] = selected_round
            selected_round["games"] = selected_game

            # edition de fin de round.
            selected_round["round_end"] = end_time["end_time"]

            # maj de la db.
            selected_tournament_data['rounds'] = rounds_list
            TournamentModel.update_tournament_data_by_id(
                selected_tournament_id, selected_tournament_data)

        elif user_input.lower() == "n":
            return

        else:
            print("invalid entry,please select y or n")
            return

    @staticmethod
    def set_ranking(selected_tournament_id):
        # methode permetant de creer et recuperer
        # les infos des participant pour etablir
        # leur score en fonction des rounds et etablir un classement

        selected_tournament_data = TournamentModel.access_tournament_data_id(
            selected_tournament_id)

        registered_players = selected_tournament_data.get("registered_players")

        def player_ranking_dict(player_id):
            player_ranking_dict = {"player_id": player_id,
                                   "player_score": 0,
                                   "player_ranking": 0 }
            return player_ranking_dict

        ranking_list = []

        for item in registered_players:
            ranking_list.append(player_ranking_dict(item))

        selected_tournament_data["ranking"] = ranking_list

        # maj de la db
        TournamentModel.update_tournament_data_by_id(
            selected_tournament_id, selected_tournament_data)

    @staticmethod
    def update_players_score_and_ranking(selected_tournament_id):
        # methode dont le but est de mettre à jour les scores des joueurs

        # appel les données du tournois selectionné par son id
        selected_tournament_data = TournamentModel.access_tournament_data_id(
            selected_tournament_id)

        # recuperation des données necessaire à la maj des datas
        current_round = selected_tournament_data.get("current_round")
        ranking = selected_tournament_data.get("ranking")
        rounds = selected_tournament_data.get("rounds")
        current_round_info = rounds[int(current_round) - 1]
        games = current_round_info['games']

        # maj des scores en tenant compte des scores precedants
        for game in games:
            for player in ranking:
                if player['player_id'] == game['gamer_1']:
                    player["player_score"] = float(
                        player["player_score"])+ float(game['score_gamer_1'])
                elif player['player_id'] == game['gamer_2']:
                    player["player_score"] = float(
                        player["player_score"])+ float(game['score_gamer_2'])

        # Trier les joueurs par score décroissant
        ranking = sorted(ranking, key=lambda x: x['player_score'],
                         reverse=True)

        # Initialiser une variable pour le classement
        current_rank = 1

        # Attribuer le classement aux joueurs
        for player in ranking:
            player['player_ranking'] = current_rank
            current_rank += 1

        # trier ranking par valeur la plus basse de player ranking
        ranking = sorted(ranking, key=lambda x: x["player_ranking"],
                         reverse=True)

        # maj de la db
        TournamentModel.update_tournament_data_by_id(
            selected_tournament_id, selected_tournament_data)

    @staticmethod
    def display_ranking(selected_tournament_id):
        # methode permettant l'afficahe d'un tableau
        # avec le score et le rang des joueurs du tournois

        selected_tournament_data = TournamentModel.access_tournament_data_id(
            selected_tournament_id)
        ranking = selected_tournament_data.get("ranking")

        ReportView.view_registered_and_ranking_players(ranking)
