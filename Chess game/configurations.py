# Configuration  for store all the constants and configurable values
from configparser import ConfigParser

config = ConfigParser()
config.read('chess_options.ini')
#Constrants
NUMBER_OF_ROWS = 8
NUMBER_OF_COLUMNS = 8
DIMENSION_OF_EACH_SQUARE = 64  # denoting 64 pixels
BOARD_COLOR_1 = config.get('chess_colors', 'board_color_1', fallback="#DDB88C")
BOARD_COLOR_2 = config.get('chess_colors', 'board_color_2', fallback="#A66D4F")
HIGHLIGHT_COLOR = config.get('chess_colors', 'highlight_color', fallback="#2EF70D")

SHORT_NAME = {
    'R': 'Rook', 'N': 'Knight', 'B': 'Bishop',
    'Q': 'Queen', 'K': 'King', 'P': 'Pawn'
    }

#Constrants end

X_AXIS_LABELS = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H')
Y_AXIS_LABELS = (1, 2, 3, 4, 5, 6, 7, 8)

#p = pawn, n = knight, b = bishop, r = rook, q = queen, k = king
#P= pawn, N = knight, B = bishop, R = rook, Q = queen, K = king

START_PIECES_POSITION = {
    "A8": "r", "B8": "n", "C8": "b", "D8": "q", "E8": "k", "F8": "b", "G8": "n", "H8": "r",
    "A7": "p", "B7": "p", "C7": "p", "D7": "p", "E7": "p", "F7": "p", "G7": "p", "H7": "p",

    "A1": "R", "B1": "N", "C1": "B", "D1": "Q", "E1": "K", "F1": "B", "G1": "N", "H1": "R",
    "A2": "P", "B2": "P", "C2": "P", "D2": "P", "E2": "P", "F2": "P", "G2": "P", "H2": "P"

    }

ORTHOGONAL_POSITIONS = ((-1, 0), (0, 1), (1, 0), (0, -1))
DIAGONAL_POSITIONS = ((-1, -1), (-1, 1), (1, -1), (1, 1))
KNIGHT_POSITIONS = ((-2, -1),(-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1))

