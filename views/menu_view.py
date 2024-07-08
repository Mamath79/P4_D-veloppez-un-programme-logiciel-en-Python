class MenuView:

    @staticmethod
    def main_menu():

        print("\n\n")
        print("##### MAIN MENU #####")

        print("\n[1] Players")
        print("[2] Tournament")
        print("[3] Report")

        print("\n[exit] quit programme")

    @staticmethod
    def player_menu():

        print("\n")
        print("##### PLAYER MENU #####")
        print("\n[1] Create new player")
        print("[2] Edit existing player")
        print("[3] List all players")

        print("\n[exit] Return to main menu")

    @staticmethod
    def tournament_menu():

        print("\n")
        print("##### TOUNAMENT MENU #####")

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

    @staticmethod
    def report_menu():

        print("\n")
        print("##### REPORT MENU #####")

        print("\n[1] Report all Players")
        print("[2] Report all Tournament")
        print("[3] Report selected Tournament by id")

        print("\n[exit] return to tournament menu")
