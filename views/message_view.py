class MessageView:

    def __init__(self) -> None:
        pass

    @staticmethod
    def display_invalid_user_input():
        print("invalid user input")

    @staticmethod
    def display_table(table):
        print(table)

    # ================= TOURNAMENT ===================

    @staticmethod
    def display_no_tournament_found(selected_tournament_id):
        print(f"No tournament found with this ID: "
              f"{selected_tournament_id}")

    @staticmethod
    def tournament_had_to_db():
        print("tournament has been add to the database.")

    @staticmethod
    def display_no_player_found(selected_tournament_id):
        print(f"No player found with this tournament ID: "
              f"{selected_tournament_id}")

    @staticmethod
    def display_player_already_registered():
        print("player already add in the tournament, please select another player")

    @staticmethod
    def display_tournament_updated(selected_tournament_id):
        print(f"\ntournament ID {selected_tournament_id} has been updated!\n")

    # =================== PLAYER =====================
    @staticmethod
    def display_not_enough_players():
        print("not enough registered players to start a round")

    @staticmethod
    def player_not_found():
        print(" Player not found in the database ")

    @staticmethod
    def display_player_add_db(player_data):
        print(f"\n {player_data['firstname']} {player_data['lastname']} "
              " has been add to the database.")

    @staticmethod
    def display_player_allready_in_db():
        print("player allready existing registered in the players database,")

    @staticmethod
    def display_player_updated():
        print("Player has been updated!")

    # ================= ROUND & GAME ===================
    @staticmethod
    def display_no_round_found(selected_tournament_id):
        print(f"No round found with this tournament ID: "
              f"{selected_tournament_id}")

    @staticmethod
    def display_4_round_limit():
        print("you reach the 4 round limit,the tournament is over.")

    @staticmethod
    def display_current_round_unfinished():
        print("Current round is not finish yet."
              " Please edit current round before start another one")

    @staticmethod
    def display_no_game_found(selected_tournament_id):
        print(f"No game found with this  tournament ID: "
              f" {selected_tournament_id}")

    @staticmethod
    def display_no_round_started_yet():
        print(" no round started yet in this tournament")

    @staticmethod
    def display_round_genereted():
        print("\n\nRound_1 and games have been genereted.\n")

    @staticmethod
    def display_invalid_entry_score():
        print("invalid entry please select win:1,"
              " loose:0 or tie: 0.5")
