from configurations import *
import model
import piece


class Controller(): # if view need to access backend then it request controller to fetch the data from backend.

    def __init__(self):
        self.init_model()

    def init_model(self):
        self.model = model.Model()

    #getter setter method
    def get_numeric_notation(self, position):
        return piece.get_numeric_notation(position)

    def get_alphanumeric_position(self, rowcolumntuple):
        return self.model.get_alphanumeric_position(rowcolumntuple)

    def get_all_pieces_on_chess_board(self):
        return self.model.items()

    def get_piece_at(self, position_of_click):
        return self.model.get_piece_at(position_of_click)
    #getter setter method end

    #wrapper method
    def reset_game_data(self):
        self.model.reset_game_data()

    def reset_to_initial_locations(self):
        self.model.reset_to_initial_locations()

    def pre_move_validation(self, start_pos, end_pos):
        return self.model.pre_move_validation(start_pos, end_pos)

    def player_turn(self):
        return self.model.player_turn

    def moves_available(self, position):
        return self.model.moves_available(position)
    #wrapper method end