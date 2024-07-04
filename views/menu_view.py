class MenuView:

    @staticmethod
    def main_menu():

        print("\n ##### MAIN MENU #####")

        print("\n[1] Players")
        print("[2] Tournament")

        print("\n[exit] quit programme")

    @staticmethod
    def player_menu():

        print("\n ##### PLAYER MENU #####")

        print("\n[1] Create new player")
        print("[2] Edit existing player")
        print("[3] List all players")

        print("\n[exit] Return to main menu")

    @staticmethod
    def tournament_menu():

        print("\n ##### TOUNAMENT MENU #####")

        print("\n[1] Create new tournament")
        print("[2] Edit existing tournament")
        print("[3] List all tournament")
        print("[4] Select a tournament")

        print("\n[exit] Return to main menu")

    @staticmethod
    def round_menu():

        print("[1] edit current round: ")
        print("[2] next round")

        print("\n[exit] return to tournament menu")
