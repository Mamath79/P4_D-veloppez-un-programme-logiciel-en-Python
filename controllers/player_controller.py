from models.player_model import PlayerModel
from views.report_view import ReportView
from views.menu_view import MenuView


class PlayerController:

    @staticmethod
    def add():

        print("\n ##### NEW PLAYER #####")

        new_player_id = input("\n Enter new player's Id : ")

        # verification si l'id n'est pas déjà present dans la DB
        result = PlayerModel.check_player_id(new_player_id)

        if result is not None:
            print("player allready existing registered in the players database,")
            MenuView.player_menu()

        else:
            new_player_first_name = input("Enter new player's first name : ")
            new_player_last_name = input("Enter new player's last name : ")
            new_player_date_of_birth = input("Enter new player date of birth (yyyy-mm-dd) : ")

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
            print(
                f"\n {player_data['firstname']} {player_data['lastname']} "
                "has been add to the database.")

    @staticmethod
    def update_by_id():

        # methode permettant l'edition d'un joueur déjà présent dans la database

        while True:
            print("\n ##### UPDATE EXISTING PLAYER #####")

            # affichage de la liste des joeurs pour permettre à
            # l'utilisateur de choisir par l'id le joueUr à modiffier
            players = PlayerModel.player_db().all()

            if not players:
                print("no players yet in the database. Please create one")
                return
            else:
                ReportView.view_list_all_players(players)
                player_id = input("\nEnter the ID of the player to update: ")

                # si exit fourni
                if player_id.lower() == "exit":
                    MenuView.player_menu()
                    break

                # verification si l'id n'est pas déjà present dans la DB
                result = PlayerModel.check_player_id(player_id)
                if not result:
                    print("this Id is not registered in the players database,")
                    continue

                while True:
                    print("\n which value do you want to update: ")
                    print("[1] id: ")
                    print("[2] first name: ")
                    print("[3] last name: ")
                    print("[4] birthdate: ")
                    print("[exit] return to player menu: ")
                    user_input = input("\n enter your choice:")

                    if user_input == "1":
                        new_id = input("New ID: ")
                        new_data = {"ID": new_id}

                    elif user_input == "2":
                        new_firstname = input("New Firstname: ")
                        new_data = {"firstname": new_firstname}

                    elif user_input == "3":
                        new_lastname = input("New laststname: ")
                        new_data = {"lastname": new_lastname}

                    elif user_input == "4":
                        new_date_of_birth = input("New Date of Birth: ")
                        new_data = {"date_of_birth": new_date_of_birth}

                    elif user_input == "exit":
                        MenuView.player_menu()
                        return

                    else:
                        print("invalid user input")
                        continue

                    # Appeler la db et mise à jour de celle ci
                    PlayerModel.update_player_db_by_id(new_data, player_id)

                    players = PlayerModel.player_db().all()
                    ReportView.view_list_all_players(players)
                    print("Player has been updated!")
                    break
                break

    @staticmethod
    def display_list_all_players():

        players = PlayerModel.player_db().all()
        if not players:
            print("no players yet in the database. Please create one")
            return
        else:
            print("\n\n##### LIST ALL PLAYERS #####\n")
            ReportView.view_list_all_players(players)
            PlayerModel.sorted_player_list()

    @staticmethod
    def delete():
        # pas dans le cdc
        pass
