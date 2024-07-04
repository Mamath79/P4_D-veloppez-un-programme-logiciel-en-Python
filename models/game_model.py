from models.player_model import PlayerModel
import random


class GameModel:
    # creation de la class Game(match) avec attributs specifiés dans le cdc

    def __init__(self,
                 game_id: int,
                 gamer_1: PlayerModel,
                 color_gamer_1: str,
                 score_gamer_1: float,
                 gamer_2: PlayerModel,
                 color_gamer_2: str,
                 score_gamer_2: float,
                 ):

        self.game_id = game_id
        self.gamer_1 = gamer_1
        self.color_gamer_1 = color_gamer_1
        self.score_gamer_1 = score_gamer_1
        self.gamer_2 = gamer_2
        self.color_gamer_2 = color_gamer_2
        self.score_gamer_2 = score_gamer_2

    def game_assign_colors(self):
        # methode permettant d'assigner à un joueur
        # une couleur sur l'echiquie de façon aléatoire.

        if random.choice([True, False]):
            self.color_gamer_1 = "white"
            self.color_gamer_2 = "black"
        else:
            self.color_gamer_1 = "black"
            self.color_gamer_2 = "white"

    def game_convert_to_tuple(self):
        return ([self.gamer_1, self.score_gamer_1],
                [self.gamer_2, self.score_gamer_2])

    def game_convert_to_dict(self):
        return {
            'game_id': self.game_id,
            'gamer_1': self.gamer_1,
            'color_gamer_1': self.color_gamer_1,
            'score_gamer_1': self.score_gamer_1,
            'gamer_2': self.gamer_2,
            'color_gamer_2': self.color_gamer_2,
            'score_gamer_2': self.score_gamer_2,
        }
