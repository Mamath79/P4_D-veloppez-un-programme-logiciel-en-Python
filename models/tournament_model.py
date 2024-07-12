from tinydb import TinyDB, Query
from datetime import datetime


class TournamentModel:
    # class  permettant de créer des instances tournoid
    def __init__(self,
                 ID_tournament=None,
                 name=None,
                 location=None,
                 creation_date=None,
                 start_date=None,
                 end_date=None,
                 description=None,
                 registered_players=None,
                 rounds=[],
                 current_round=None,
                 total_rounds=None,
                 ranking=[],
                 ):

        self.ID_tournament = ID_tournament
        self.name = name
        self.location = location
        self.creation_date = (
            creation_date if creation_date else datetime.now()
            .strftime("%Y-%m-%d %H:%M:%S"))
        self.start_date = start_date
        self.end_date = end_date
        self.description = description
        self.registered_players = (
            registered_players if registered_players is not None else [])
        self.rounds = rounds
        self.current_round = current_round
        self.total_rounds = total_rounds if total_rounds else 4
        self.ranking = ranking

    def set_players(self, players: list[dict]):
        self.registered_players = players

    def set_rounds(self, rounds):
        self.rounds = rounds

    def set_ranking(self, ranking):
        self.ranking = ranking

    @staticmethod
    # creation et appel de la database via Tinydb
    def tournament_db():
        return TinyDB("database/tournament.json")

    @staticmethod
    # acces dans la db aun tournois via son id
    def access_tournament_data_id(selected_tournament_id):
        data = TournamentModel.tournament_db()
        search = Query()
        result = data.get(search.ID_tournament == int
                          (selected_tournament_id))
        return result

    @staticmethod
    # methode de class servant à la sauvegarde d'un tournoi dans la database
    def save(tournament):
        tournament_db = TournamentModel.tournament_db()
        # convert to dict a mettre dans le model
        tournament_data = {
            'ID_tournament': tournament.ID_tournament,
            'name': tournament.name,
            'location': tournament.location,
            'creation_date': tournament.creation_date,
            'start_date': tournament.start_date,
            'end_date': tournament.end_date,
            'description': tournament.description,
            'registered_players': tournament.registered_players,
            'rounds': tournament.rounds,
            'current_round': tournament.current_round,
            'total_rounds': tournament.total_rounds,
            'ranking': tournament.ranking
            }
        tournament_db.insert(tournament_data)

    @staticmethod
    def check_tournament_id(ID_tournament):
        # methode de class servant à aller chercher si
        # un tournois est present dans la db via son id
        tournament_db = TournamentModel.tournament_db()
        result = tournament_db.get(doc_id=int
                                   (ID_tournament))
        return result

    @staticmethod
    def update_tournament_data_by_id(selected_tournament_id,
                                     selected_tournament_data):
        # methode servant à updater les metadatas
        # d'un tournois déjà créer
        data = TournamentModel.tournament_db()
        tournament = Query()
        data.update(selected_tournament_data,
                    tournament.ID_tournament == int(selected_tournament_id))
