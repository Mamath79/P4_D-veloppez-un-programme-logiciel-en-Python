from models.player_model import PlayerModel
from views.report_view import ReportView
from views.menu_view import MenuView
from views.message_view import MessageView
from views.titles import Title
from views.user_input import UserInput
from prettytable import PrettyTable


class PlayerController:

    @staticmethod
    def add():

        Title.new_player_menu()

        new_player_id = UserInput.ask_player_id()

        # verification si l'id n'est pas déjà present dans la DB
        result = PlayerModel.check_player_id(new_player_id)

        if result is not None:
            MessageView.display_player_allready_in_db()
            MenuView.player_menu()

        else:
            new_player_first_name = UserInput.ask_player_first_name()
            new_player_last_name = UserInput.ask_player_last_name()
            new_player_date_of_birth = UserInput.ask_player_date_of_birth()

            # Créer un nouvel objet Player avec les informations fournies par l'utilisateur
            new_player = PlayerModel(new_player_id,
                                     new_player_first_name,
                                     new_player_last_name,
                                     new_player_date_of_birth)

            # Convertir l'objet Player en un dictionnaire avant de l'insérer dans la base de données
            player_data = {
                "ID": new_player.ID,
                "firstname": new_player.firstname,
                "lastname": new_player.lastname,
                "date_of_birth": new_player.date_of_birth
                }

            # Insérer le nouveau joueur dans la base de données
            PlayerModel.insert_player_db(player_data)
            MessageView.display_player_add_db(player_data)

    @staticmethod
    def update_by_id():

        # methode permettant l'edition d'un joueur déjà présent dans la database

        while True:

            # affichage de la liste des joeurs pour permettre à
            # l'utilisateur de choisir par l'id le joueUr à modiffier
            Title.update_player_title()
            players = PlayerModel.player_db().all()

            if not players:
                MessageView.player_not_found()
                return
            else:
                ReportView.view_list_all_players(players)
                player_id = UserInput.ask_player_id()

                # si exit fourni
                if player_id.lower() == "exit":
                    MenuView.player_menu()
                    break

                # verification si l'id n'est pas déjà present dans la DB
                result = PlayerModel.check_player_id(player_id)
                if not result:
                    MessageView.display_no_player_found()
                    continue

                while True:

                    user_input = MenuView.update_menu_player()

                    if user_input == "1":
                        new_id = UserInput.ask_player_id()
                        new_data = {"ID": new_id}

                    elif user_input == "2":
                        new_firstname = UserInput.ask_player_first_name()
                        new_data = {"firstname": new_firstname}

                    elif user_input == "3":
                        new_lastname = UserInput.ask_player_last_name()
                        new_data = {"lastname": new_lastname}

                    elif user_input == "4":
                        new_date_of_birth = UserInput.ask_player_date_of_birth()
                        new_data = {"date_of_birth": new_date_of_birth}

                    elif user_input == "exit":
                        MenuView.player_menu()
                        return

                    else:
                        MenuView.display_invalid_user_input()
                        continue

                    # Appeler la db et mise à jour de celle ci
                    PlayerModel.update_player_db_by_id(new_data, player_id)

                    players = PlayerModel.player_db().all()
                    ReportView.view_list_all_players(players)
                    MessageView.display_player_updated()
                    break
                break

    @staticmethod
    def display_list_all_players():

        players = PlayerModel.player_db().all()
        if not players:
            MessageView.display_no_player_found()
            return
        else:
            Title.all_player_title()
            ReportView.view_list_all_players(players)
            PlayerController.sorted_player_list()

    @staticmethod
    def sorted_player_list():

        # trier le liste de joueurs en fonction du
        # nom de famille , de l'ID ou de la date de naissance afin de
        # lister et afficher les joueurs triés par ordre alphabetique.

        players = PlayerModel.player_db().all()

        if players:

            # trier la db player  par ordre alphabetique( last Name)
            players_sorted_by_lastname = sorted(
                players, key=lambda x: x["lastname"])
            players_sorted_by_ID = sorted(
                players, key=lambda x: x["ID"])
            players_sorted_by_date_of_birth = sorted(
                players, key=lambda x: x["date_of_birth"])

            while True:

                table = PrettyTable()
                table.field_names = players[0].keys()
                user_input = MenuView.view_sorted_player_list()

                if user_input == "1":
                    for row in players_sorted_by_lastname:
                        table.add_row(row.values())
                    MessageView.display_table(table)
                elif user_input == "2":
                    for row in players_sorted_by_ID:
                        table.add_row(row.values())
                    MessageView.display_table(table)
                elif user_input == "3":
                    for row in players_sorted_by_date_of_birth:
                        table.add_row(row.values())
                    MessageView.display_table(table)
                elif user_input == "exit":
                    break
                else:
                    MessageView.display_invalid_user_input()
        else:
            MessageView.display_no_player_found()

    @staticmethod
    def delete():
        # pas dans le cdc
        pass
