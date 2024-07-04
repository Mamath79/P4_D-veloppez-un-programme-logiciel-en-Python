class RoundModel:

    def __init__(
            self,
            round_id: int = None,
            round_name: str = None,
            round_start: str = None,
            round_end: str = None,
            games: list = None,
            ):

        self.round_id = round_id
        self.round_name = round_name
        self.round_start = round_start
        self.round_end = round_end
        self.games = games if games is not None else []

    def set_round_id(self):
        pass

    def set_games(self, games):
        self.games = games

    def round_convert_to_dict(self):
        return {
            'round_id': self.round_id,
            'round_name': self.round_name,
            'round_start': self.round_start,
            'round_end': self.round_end,
            'games': [game.game_convert_to_tuple() for game in self.games]
        }
