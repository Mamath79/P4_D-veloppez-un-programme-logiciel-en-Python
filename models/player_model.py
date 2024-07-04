from tinydb import TinyDB, Query
from prettytable import PrettyTable


class PlayerModel:
    # creation de la classe player, avec les attributs definis dans le cdc
    def __init__(
            self,
            ID: str,
            first_name: str,
            last_name: str,
            date_of_birth: str,
            ):

        self.ID = ID
        self.firstname = first_name
        self.lastname = last_name
        self.date_of_birth = date_of_birth

    @staticmethod
    # appel de la db player
    def player_db():
        return TinyDB("database/players.json")

    @staticmethod
    # methode d'insertion dans la player db avec
    # verification de reussite de la methode
    def insert_player_db(player_data):
        try:
            PlayerModel.player_db().insert(player_data)
            return True
        except Exception as e:
            print(f"something went wrong:{e} please try again")
            return False

    @staticmethod
    # methode servant à verifier si l'id d'un joueur est bien
    # present dans la db.
    def check_player_id(player_id):
        player_db = PlayerModel.player_db()
        search = Query()
        result = player_db.get(search.ID == player_id)
        return result

    @staticmethod
    # methode de mise a jour des informations d'un joueur.
    def update_player_db_by_id(new_data, player_id):
        try:
            player_db = PlayerModel.player_db()
            player_db.update(new_data, Query().ID == player_id)
            return True
        except Exception as e:
            print(f"something went wrong:{e} please try again")
            return False

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
                print("\n Sorting player list by:")
                print("\n[1] By Last name")
                print("[2] By ID")
                print("[3] By date of birth")
                print("\n[exit] Back to Menu Player")
                user_input = input("\n enter your choice:")

                if user_input == "1":
                    for row in players_sorted_by_lastname:
                        table.add_row(row.values())
                    print(table)
                elif user_input == "2":
                    for row in players_sorted_by_ID:
                        table.add_row(row.values())
                    print(table)
                elif user_input == "3":
                    for row in players_sorted_by_date_of_birth:
                        table.add_row(row.values())
                    print(table)
                elif user_input == "exit":
                    break
                else:
                    print("invalid user input")
        else:
            print(
                "no players database found"
                "please enter new player in the db : ")
