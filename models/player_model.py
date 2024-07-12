from tinydb import TinyDB, Query


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
        PlayerModel.player_db().insert(player_data)

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
        player_db = PlayerModel.player_db()
        player_db.update(new_data, Query().ID == player_id)
