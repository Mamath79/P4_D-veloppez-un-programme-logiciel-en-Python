from controllers.player_controller import PlayerController
from controllers.tournament_controller import TournamentController
from views.menu_view import MenuView
from views.message_view import MessageView
from views.user_input import UserInput


class Router:

    @staticmethod
    # menu principal du programme
    def navigate_main_menu():

        while True:
            MenuView.main_menu()
            user_input = UserInput.ask_enter_your_choice()
            if user_input == "1":
                Router.navigate_player_menu()
            elif user_input == "2":
                Router.navigate_tournement_menu()
            elif user_input == "3":
                Router.report_menu()
            elif user_input.lower() == "exit":
                exit()
            else:
                MessageView.display_invalid_user_input()

    @staticmethod
    # menu concernant la creation et la gestion des joueurs
    def navigate_player_menu():

        while True:
            MenuView.player_menu()
            user_input = UserInput.ask_enter_your_choice()
            if user_input == "1":
                PlayerController.add()
            elif user_input == "2":
                PlayerController.update_by_id()
            elif user_input == "3":
                PlayerController.display_list_all_players()
            elif user_input == "exit":
                break
            else:
                MessageView.display_invalid_user_input()

    @staticmethod
    # menu concernant la creation et la gestion des tournois
    def navigate_tournement_menu():
        tournament_controler = TournamentController()

        while True:
            MenuView.tournament_menu()
            user_input = UserInput.ask_enter_your_choice()
            if user_input == "1":
                tournament_controler.add()
            elif user_input == "2":
                TournamentController.update_by_id()
            elif user_input == "3":
                TournamentController.display_list_all_tournaments()
            elif user_input == "4":
                TournamentController.navigate_selected_tournament()
            elif user_input == "exit":
                break

            else:
                MessageView.display_invalid_user_input()

    @staticmethod
    # menu destiné a l'affichage des rapports sur les joueurs et les tournois
    def report_menu():

        while True:
            MenuView.report_menu()
            user_input = UserInput.ask_enter_your_choice()
            if user_input == "1":
                PlayerController.display_list_all_players()
            elif user_input == "2":
                TournamentController.display_list_all_tournaments()
            elif user_input == "3":
                TournamentController.report_selected_tournament()
            elif user_input == "exit":
                break

            else:
                MessageView.display_invalid_user_input()
