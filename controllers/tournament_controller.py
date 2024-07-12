from models.tournament_model import TournamentModel
from models.player_model import PlayerModel
from views.report_view import ReportView
from views.menu_view import MenuView
from views.message_view import MessageView
from views.titles import Title
from views.user_input import UserInput
from datetime import datetime
from tinydb import Query
from controllers.round_controller import RoundController
from controllers.game_controller import GameController
from prettytable import PrettyTable


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

        new_name = UserInput.ask_tournament_name()
        new_location = UserInput.ask_tournament_location()
        new_start_date = UserInput.ask_tournament_start_date()
        new_end_date = UserInput.ask_tournament_end_date()
        new_description = UserInput.ask_tournament_description()

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
        user_input = UserInput.ask_players_tournament()

        # si exit fourni par l'utilisateur
        if user_input.lower() == "exit":
            MenuView.tournament_menu()

        try:
            user_input = int(user_input)
            if user_input not in [2, 4, 6, 8]:
                MessageView.display_invalid_user_input()
                return self.choose_players(tournament)
        except ValueError:
            MessageView.display_invalid_user_input()
            return self.choose_players(tournament)

        selected_players = []
        while len(selected_players) < user_input:

            Title.available_players_title()
            ReportView.view_list_all_players(available_players)

            player_id = UserInput.ask_choose_player(selected_players)
            if not PlayerModel.check_player_id(player_id):
                MessageView.display_invalid_user_input()
                continue

            elif player_id in selected_players:
                MessageView.display_player_already_registered()
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
        MessageView.tournament_had_to_db()

    def update_by_id():

        # methode permettant l'edition d'un tournois déjà présent dans la database

        while True:
            Title.update_tournament_title()

            # affichage de la liste des tournois pour permettre à
            # l'utilisateur de choisir par l'id le tournois à modiffier
            data = TournamentModel.tournament_db()
            ReportView.view_list_all_tournaments(data)
            selected_tournament_id = UserInput.ask_tournament_id()

            while True:
                user_input = MenuView.update_tournament_menu()

                if user_input == "1":
                    new_name = UserInput.ask_tournament_name()
                    new_data = {"name": new_name}

                elif user_input == "2":
                    new_location = UserInput.ask_tournament_location()
                    new_data = {"location": new_location}

                elif user_input == "3":
                    new_start_date = UserInput.ask_tournament_start_date()
                    new_data = {"start_date": new_start_date}

                elif user_input == "4":
                    new_end_date = UserInput.ask_tournament_end_date()
                    new_data = {"end_date": new_end_date}

                elif user_input == "5":
                    new_description = UserInput.ask_tournament_description()
                    new_data = {"description": new_description}

                elif user_input == "exit":
                    MenuView.tournament_menu()
                    return

                else:
                    MessageView.display_invalid_user_input()
                    continue

                # Appeler la db et mise à jour de celle ci
                TournamentModel.update_tournament_data_by_id(selected_tournament_id, new_data)

                data = TournamentModel.tournament_db()
                ReportView.view_list_all_tournaments(data)
                MessageView.display_tournament_updated(selected_tournament_id)
                break
            break

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
            MessageView.display_no_tournament_found()
            return

        rounds_list = selected_tournament_data.get("rounds")

        if not rounds_list:
            MessageView.display_no_round_started_yet()

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
        TournamentController.sorted_tournament_list()

    @staticmethod
    def display_selected_tournament(selected_tournament_id):
        # methode servant a afficher une vue resumé d'un tournois
        # selectionné par son id.

        result = TournamentModel.check_tournament_id(selected_tournament_id)
        if not result:
            MessageView.display_no_tournament_found()

        else:
            selected_tournament_data = result
            round_info = selected_tournament_data.get("rounds")
            ReportView.view_rounds_and_games(round_info)

    @staticmethod
    def navigate_selected_tournament():

        data = TournamentModel.tournament_db()
        if not data:
            MessageView.display_no_tournament_found()
            return

        ReportView.view_list_all_tournaments(data)
        selected_tournament_id = UserInput.ask_tournament_id()

        data = TournamentModel.access_tournament_data_id(
            selected_tournament_id)
        selected_tournament_data = data
        if not selected_tournament_data:
            MessageView.display_no_tournament_found()
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
                user_input = UserInput.ask_start_round_and_game()

                if user_input.lower() == "y":
                    TournamentController.set_ranking(
                        selected_tournament_id)
                    RoundController.generate_round(
                        selected_tournament_id)
                    TournamentController.edit_display_current_round(
                        selected_tournament_id)
                    GameController.generate_game(
                        selected_tournament_id)

                    MessageView.display_round_genereted()

                    TournamentController.display_selected_tournament(
                        selected_tournament_id)

                    return TournamentController.navigate_selected_tournament()

                elif user_input.lower() == "n":
                    return

                else:
                    MessageView.display_invalid_user_input()

            else:
                TournamentController.display_selected_tournament(
                    selected_tournament_id)
                TournamentController.display_ranking(
                    selected_tournament_id)
                user_input = MenuView.edit_round_menu()

                if user_input == "1":
                    TournamentController.edit_end_current_round(
                        selected_tournament_id)
                    TournamentController.update_players_score_and_ranking(
                        selected_tournament_id)

                elif user_input == "2":
                    RoundController.generate_round(selected_tournament_id)

                    user_input = UserInput.ask_start_next_game()

                    if user_input == "y":
                        TournamentController.edit_display_current_round(
                            selected_tournament_id)
                        GameController.generate_game(
                            selected_tournament_id)

                    elif user_input == "n":
                        return

                    else:
                        MessageView.display_invalid_user_input()

                elif user_input == "exit":
                    return

                else:
                    MessageView.display_invalid_user_input()

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

        user_input = UserInput.ask_end_game_edit_score()
        end_time = {'end_time': datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

        if user_input.lower() == "y":
            for game in selected_game:
                try:
                    user_input_2 = float(UserInput.ask_gamer_score(game))
                except ValueError:
                    MessageView.display_invalid_entry_score()
                    return

                if user_input_2 not in [1, 0, 0.5]:
                    MessageView.display_invalid_entry_score()
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
                        MessageView.display_invalid_entry_score()
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
            MessageView.display_invalid_user_input()
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
                                   "player_ranking": 0}
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
                        player["player_score"]) + float(game['score_gamer_1'])
                elif player['player_id'] == game['gamer_2']:
                    player["player_score"] = float(
                        player["player_score"]) + float(game['score_gamer_2'])

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

    @staticmethod
    def report_selected_tournament():

        # methode dont le but est l'affiche ge de toutes les données
        # sous forme de plusieurs tableaux d'un tournois selectionné

        data = TournamentModel.tournament_db()
        if not data:
            MessageView.display_no_tournament_found()
            return

        ReportView.view_list_all_tournaments(data)
        selected_tournament_id = UserInput.ask_tournament_id()

        selected_tournament_data = TournamentModel.access_tournament_data_id(
            selected_tournament_id)
        if not selected_tournament_data:
            MessageView.display_no_tournament_found
            return

        ReportView.header_info_selected_tournament(selected_tournament_data)
        TournamentController.display_selected_tournament(selected_tournament_id)
        TournamentController.display_ranking(selected_tournament_id)

    @staticmethod
    def sorted_tournament_list():

        # creer fonction de tri par appel utlisateur
        # sort_tournaments_by_field(tournaments, fieldname)

        data = TournamentModel.tournament_db()
        tournaments = data.all()
        table = PrettyTable()

        fields_to_display = ['ID_tournament',
                             'name',
                             'location',
                             'creation_date',
                             'start_date',
                             'end_date'
                             ]
        table.field_names = fields_to_display

        tournaments_sorted_name = sorted(tournaments,
                                         key=lambda x:
                                         x.get("name"))
        tournaments_sorted_creation_date = sorted(tournaments,
                                                  key=lambda x:
                                                  x.get("creation_date"))
        tournaments_sorted_ID = sorted(tournaments,
                                       key=lambda x:
                                       x.get("ID_tournament"))

        while True:
            user_input = MenuView.sorted_tournament_menu()

            if user_input == '1':
                table.clear_rows()
                for row in tournaments_sorted_name:
                    selected_row = {}
                    for key, value in row.items():
                        if key in fields_to_display:
                            selected_row[key] = value
                    table.add_row(selected_row.values())
                MessageView.display_table(table)

            elif user_input == "2":
                table.clear_rows()
                for row in tournaments_sorted_creation_date:
                    selected_row = {}
                    for key, value in row.items():
                        if key in fields_to_display:
                            selected_row[key] = value
                    table.add_row(selected_row.values())
                MessageView.display_table(table)

            elif user_input == "3":
                table.clear_rows()
                for row in tournaments_sorted_ID:
                    selected_row = {}
                    for key, value in row.items():
                        if key in fields_to_display:
                            selected_row[key] = value
                    table.add_row(selected_row.values())
                MessageView.display_table(table)

            elif user_input == "exit":
                break
            else:
                MessageView.display_invalid_user_input()
