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
    def update_menu_player():

        print("\n which value do you want to update: ")
        print("[1] id: ")
        print("[2] first name: ")
        print("[3] last name: ")
        print("[4] birthdate: ")
        print("[exit] return to player menu: ")
        user_input = input("\n enter your choice:")
        return user_input

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
        print(" ##### REPORT MENU ##### ")
        print("\n[1] Report all Players")
        print("[2] Report all Tournament")
        print("[3] Report selected Tournament by id")
        print("\n[exit] return to tournament menu")

    @staticmethod
    def view_sorted_player_list():
        print("\n Sorting player list by:")
        print("\n[1] By Last name")
        print("[2] By ID")
        print("[3] By date of birth")
        print("\n[exit] Back to Menu Player")
        user_input = input("\n enter your choice:")
        return user_input

    @staticmethod
    def update_tournament_menu():

        print("\n which value do you want to update: ")
        print("[1] tournament name: ")
        print("[2] tournament location: ")
        print("[3] start date (yyyy-mm-dd): ")
        print("[4] end date (yyyy-mm-dd): ")
        print("[5] description: ")
        print("[exit] return to player menu: ")
        user_input = input("\n enter your choice:")
        return user_input

    @staticmethod
    def sorted_tournament_menu():

        print("[1] sorted the tournament list by name")
        print("[2] sorted the tournament list by creation_date")
        print("[3] sorted the tournament list by Id")
        print("\n[exit] return to tournament menu")
        user_input = input("\n enter your choice: ")
        return user_input

    @staticmethod
    def edit_round_menu():
        print("\n[1] edit/end current round")
        print("[2] start next round")
        print("\n[exit] return to tournament menu")
        user_input = input("\nenter your choice: ")
        return user_input
