class UserInput:
    def __init__(self) -> None:
        pass

    @staticmethod
    def ask_players_tournament():
        return input("\nselect tournament's players "
                     "( 2, 4, 6 or 8) or exit to return: ")

    @staticmethod
    def ask_enter_your_choice():
        return input("\n enter your choice:")

    # =============== PLAYERS ===============

    @staticmethod
    def ask_player_id():
        return input("\n Enter player's Id : ")

    @staticmethod
    def ask_player_first_name():
        return input("Enter player's first name : ")

    @staticmethod
    def ask_player_last_name():
        return input("Enter player's last name : ")

    @staticmethod
    def ask_player_date_of_birth():
        return input("Enter player's date of birth : ")

    # =============== TOURNAMENT ===============
    @staticmethod
    def ask_tournament_name():
        return input("Enter tournament's name : ")

    @staticmethod
    def ask_tournament_location():
        return input("Enter tournament's location : ")

    @staticmethod
    def ask_tournament_start_date():
        return input("Enter tournament's start date (yyyy-mm-dd) : ")

    @staticmethod
    def ask_tournament_end_date():
        return input("Enter tournament's end date (yyyy-mm-dd) : ")

    @staticmethod
    def ask_tournament_description():
        return input("Enter tournament's description : ")

    @staticmethod
    def ask_tournament_id():
        return input("\nEnter the ID of the tournament to display: ")

    @staticmethod
    def ask_start_round_and_game():
        return input("\ndo you want to start the first/next round "
                     "and the first/next game ? (y/n): ")

    @staticmethod
    def ask_choose_player(selected_players):
        return input(f"Select player {len(selected_players) + 1} ID: ")

    # =============== ROUND&GAME ===============

    @staticmethod
    def ask_start_next_game():
        return input("\ndo you want to start the next game ? (y/n): \n")

    @staticmethod
    def ask_end_game_edit_score():
        return input("Do you want to end the game and edit scores ? (y/n): ")

    @staticmethod
    def ask_gamer_score(game):
        return input(f"Please enter {game["gamer_1"]}'s score win = 1, "
                     "loose = 0 , tie = 0.5:")
