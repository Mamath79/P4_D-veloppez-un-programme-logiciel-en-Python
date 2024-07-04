from controllers.player_controller import PlayerController
from controllers.tournament_controller import TournamentController
from views.menu_view import MenuView


class Router:

    @staticmethod
    # menu principal du programme
    def navigate_main_menu():

        while True:
            MenuView.main_menu()
            user_input = input("\n enter your choice:")
            if user_input == "1":
                Router.navigate_player_menu()
            elif user_input == "2":
                Router.navigate_tournement_menu()
            elif user_input == "exit":
                exit()
                break
            else:
                print("invalid user input")

    @staticmethod
    # menu concernant la creation et la gestion des joueurs
    def navigate_player_menu():

        while True:
            MenuView.player_menu()
            user_input = input("\n enter your choice:")
            if user_input == "1":
                PlayerController.add()
            elif user_input == "2":
                PlayerController.update_by_id()
            elif user_input == "3":
                PlayerController.display_list_all_players()
            elif user_input == "exit":
                break
            else:
                print("invalid user input")

    @staticmethod
    # menu concernant la creation et la gestion des tournois
    def navigate_tournement_menu():
        tournament_controler = TournamentController()

        while True:
            MenuView.tournament_menu()
            user_input = input("\n enter your choice:")
            if user_input == "1":
                tournament_controler.add()
            elif user_input == "2":
                TournamentController.update()
            elif user_input == "3":
                TournamentController.display_list_all_tournaments()
            elif user_input == "4":
                TournamentController.navigate_selected_tournament()
            elif user_input == "exit":
                break

            else:
                print("Invalid user input")
