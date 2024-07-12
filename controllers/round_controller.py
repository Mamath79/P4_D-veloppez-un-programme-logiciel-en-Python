from models.round_model import RoundModel
from models.tournament_model import TournamentModel
from views.message_view import MessageView
from datetime import datetime


class RoundController:

    def __init__(self):
        pass

    @staticmethod
    def generate_round(selected_tournament_id):

        # recuperation du dict du tournois choisi par ID
        selected_tournament_data = TournamentModel.access_tournament_data_id(selected_tournament_id)

        # a l'interieur du tournois selectionné , recuperation de la liste des rounds
        rounds_list = selected_tournament_data.get('rounds')

        # Vérification du nombre de rounds actuels
        if rounds_list and len(rounds_list) >= 4:
            MessageView.display_4_round_limit()
            return

        # Vérification si le dernier round est terminé
        if rounds_list and not rounds_list[-1].get("round_end"):
            MessageView.display_current_round_unfinished()
            return

        # attribution de l'id d'un round et eviter la possibilité de doublon
        if not rounds_list:
            round_id = 1
        else:
            rounds_ids = []
            for item in rounds_list:
                rounds_ids.append(item.get("round_id"))
                highest_round_id = max(rounds_ids)
                round_id = highest_round_id + 1

        # creation de l'objet nouveau round.
        new_round = RoundModel(round_id=int(round_id))
        new_round.round_name = f"Round {round_id}"
        new_round.round_start = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # sauvegarde du nouveau round dans le base de donnée
        data_round = RoundModel.round_convert_to_dict(new_round)
        rounds_list.append(data_round)
        selected_tournament_data['rounds'] = rounds_list
        TournamentModel.update_tournament_data_by_id(selected_tournament_id, selected_tournament_data)
