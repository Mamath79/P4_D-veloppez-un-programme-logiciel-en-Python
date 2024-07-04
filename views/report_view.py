from prettytable import PrettyTable


class ReportView:

    def __init__(self):
        pass

    @staticmethod
    def view_list_all_players(players):

        # methode servant a afficher un tableau de l'ensemble des joueurs
        # trier la db player  par ordre alphabetique (last Name)
        players_sorted_by_lastname = sorted(
            players, key=lambda x: x["lastname"])

        # a l'aide de PrettyTable convertir le dict sous forme de tableau
        table = PrettyTable()

        # recuperer les clés de chaque joueur comme en tete du tableau
        table.field_names = players[0].keys()
        for row in players_sorted_by_lastname:
            table.add_row(row.values())

        # Afficher le tableau
        print("\n ##### lIST ALL PLAYERS #####")
        print(table)

    @staticmethod
    def header_info_selected_tournament(selected_tournament_data):

        print((f"\n##### {selected_tournament_data['name']} #####"))
        print(f"\nLocation: {selected_tournament_data['location']}")
        print(
            f"From: {selected_tournament_data['start_date']}"
            f"to {selected_tournament_data['end_date']}")
        print(
            f"Description: {selected_tournament_data['description']}")
        print(
            f"\nCurrent Round: {selected_tournament_data['current_round']}\n")

    @staticmethod
    def view_list_all_tournaments(data):

        print("\n ##### lIST ALL TOURNAMENT #####\n")
        ReportView.table_list_tournament(data)

    @staticmethod
    def table_list_tournament(data):

        tournaments = data.all()
        table = PrettyTable()
        

        if tournaments:
            
            tournaments_sorted_ID = sorted(
            tournaments, key=lambda x: x.get("ID_tournament"))

            fields_to_display = ['ID_tournament',
                                 'name',
                                 'location',
                                 'creation_date',
                                 'start_date',
                                 'end_date']
            table.field_names = fields_to_display

            for row in tournaments_sorted_ID:
                selected_row = {
                    key: value for key,
                    value in row.items() if key in fields_to_display
                    }
                table.add_row(selected_row.values())

            print(table)
        else:
            print("\ntournament list is empty\n")

    @staticmethod
    def view_registered_and_ranking_players(ranking):
        # methode permettant d'afficher une liste
        # des joueurs du tournois et leur classement

        ranking_sorted = sorted(
            ranking, key=lambda x: x["player_ranking"])

        if not ranking_sorted:
            print("No players available to display.")
            return

        else:
            table = PrettyTable()
            keys_to_display = list(ranking_sorted[0].keys())

            table.field_names = keys_to_display
            for row in ranking:
                table.add_row(row.values())
                table.add_row(["-"*12, "-"*12, "-"*12])

            print(table)

    @staticmethod
    def view_rounds_and_games(round_info):
        # methode permettant l'affichage sous forme de tableau
        # des inforamtions des rounds et matches du tournois

        if not round_info:
            print("first round hasn't been started yet")

        else:
            table_round = PrettyTable()
            keys_to_display = ['round_id',
                               'round_name',
                               'round_start',
                               'round_end',
                               'games']
            table_round.field_names = keys_to_display

            for round_data in round_info:
                round_id = round_data.get("round_id")
                round_name = round_data.get("round_name")
                round_start = round_data.get("round_start")
                round_end = round_data.get("round_end")
                games = round_data.get("games")

                game_info_to_display = []
                for game in games:

                    game_info_to_display.append(
                        f"Game {game['game_id']}: "
                        f"{game['gamer_1']} {game["score_gamer_1"]} "
                        f"vs {game['gamer_2']} {game["score_gamer_2"]}")

                infos_to_display = [round_id,
                                    round_name,
                                    round_start,
                                    round_end,
                                    "\n".join(game_info_to_display)]

                table_round.add_row(infos_to_display)
                # Ajouter une ligne de séparation après chaque round
                table_round.add_row(["-"*12, "-"*12, "-"*24, "-"*24, "-"*42])

            print(table_round)
