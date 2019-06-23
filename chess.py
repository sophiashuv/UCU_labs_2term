boards = ['Normal chessboard', 'Hexagon chessboard', 'Glinsky chessboard', 'Quad chessboard', 'Double chessboard']
for i in boards:
    print(i)
choice = input('Choose one board: ')

class Board:
    """Class for boards representation"""
    def __init__(self, board_type):
        self.board_type = board_type
        self.board = None
        self.positions = []

    def create_board(self):
        """
        (Board) -> NoneType
        Creates different boards
        """
        if self.board_type == 'Normal chessboard':
            self.board = [Pawn('Black', ["A", 7]), Pawn('White', ["A", 2]), Pawn('Black', ["B", 7]),
                          Pawn('White', ["B", 2]), Pawn('Black', ["C", 7]), Pawn('White', ["C", 2]),
                          Pawn('Black', ["D", 7]), Pawn('White', ["D", 2]), Pawn('Black', ["E", 7]),
                          Pawn('White', ["E", 2]), Pawn('Black', ["F", 7]), Pawn('White', ["F", 2]),
                          Pawn('Black', ["G", 7]), Pawn('White', ["G", 2]), Pawn('Black', ["H", 7]),
                          Pawn('White', ["H", 2]), Queen('Black', ['D', 8]), Queen('White', ['D', 1]),
                          King('Black', ['E', 8]), King('White', ['E', 1]), Rook('Black', ["A", 8]),
                          Rook('Black', ["H", 8]), Rook('White', ["A", 1]), Rook('White', ["H", 1]),
                          Bishop('Black', ["C", 8]), Bishop('Black', ["F", 8]), Bishop('White', ["C", 1]),
                          Bishop('White', ["F", 1]), Knight('Black', ["B", 8]), Knight('Black', ["G", 8]),
                          Knight('White', ["B", 1]), Knight('White', ["G", 1])]

        elif self.board_type == 'Hexagon chessboard':
            self.board = [Pawn('Black', ["H", 11]), Pawn('White', ["A", 2]), Pawn('Black', ["G", 11]),
                          Pawn('White', ["B", 2]), Pawn('Black', ["F", 11]), Pawn('White', ["C", 2]),
                          Pawn('Black', ["E", 11]), Pawn('White', ["D", 2]), Pawn('Black', ["I", 11]),
                          Pawn('White', ["E", 2]), Pawn('Black', ["J", 11]), Pawn('White', ["F", 2]),
                          Pawn('Black', ["K", 11]), Pawn('White', ["G", 2]), Pawn('Black', ["L", 11]),
                          Pawn('White', ["H", 2]), Pawn('Red', ["G", 7]), Pawn('Red', ["A", 7]),
                          Pawn('Red', ["B", 7]), Pawn('Red', ["C", 7]), Pawn('Red', ["D", 7]), Pawn('Red', ["L", 7]),
                          Pawn('Red', ["I", 7]), Pawn('Red', ["K", 7]), Queen('Black', ['I', 12]),
                          Queen('White', ['E', 1]), Queen('Red', ['D', 8]), King('Black', ['E', 12]),
                          King('White', ['D', 1]), King('Red', ['I', 8]), Rook('Black',["H", 12]),
                          Rook('Black',["L", 12]), Rook('White',["A", 1]), Rook('White',["H", 1]),
                          Rook('Red',["A", 8]), Rook('Red',["L", 8]), Bishop('Black', ["J", 12]),
                          Bishop('Black', ["F", 12]), Bishop('White', ["C", 1]), Bishop('White', ["F", 1]),
                          Bishop('Red', ["C", 8]), Bishop('Red', ["G", 8]), Knight('Black', ["G", 12]),
                          Knight('Black', ["K", 12]), Knight('White', ["B", 1]), Knight('White', ["G", 1]),
                          Knight('Red', ["B", 8]), Knight('Red', ["K", 8])]

        elif self.board_type == 'Glinsky chessboard':
            self.board = [Pawn('Black', ["B", 7]), Pawn('White', ["B", 1]), Pawn('Black', ["C", 7]),
                          Pawn('White', ["C", 2]), Pawn('Black', ["D", 7]), Pawn('White', ["D", 3]),
                          Pawn('Black', ["E", 7]), Pawn('White', ["E", 4]), Pawn('Black', ["F", 7]),
                          Pawn('White', ["F", 5]), Pawn('Black', ["G", 7]), Pawn('White', ["G", 4]),
                          Pawn('Black', ["H", 7]), Pawn('White', ["H", 3]), Pawn('Black', ["I", 7]),
                          Pawn('White', ["I", 2]), Pawn('Black', ["K", 7]), Pawn('White', ["K", 1]),
                          Pawn('White', ["K", 5]), Queen('White', ['E', 1]),
                          Queen('Black', ['E', 10]), King('Black', ['G', 10]), King('White', ['G', 1]),
                          Rook('Black', ["I", 8]), Rook('Black', ["C", 8]), Rook('White', ["I", 1]),
                          Rook('White', ["C", 1]), Bishop('Black', ["F", 9]), Bishop('Black', ["F", 10]),
                          Bishop('White', ["F", 1]), Bishop('White', ["F", 2]), Bishop('Black', ["F", 11]),
                          Bishop('White', ["F", 3]), Knight('Black', ["H", 9]), Knight('Black', ["D", 9]),
                          Knight('White', ["H", 1]), Knight('White', ["D", 1])]

        elif self.board_type == 'Quad chessboard':
            self.board = [Pawn('Black', ["I", 13]), Pawn('White', ["I", 2]), Pawn('Black', ["J", 13]),
                          Pawn('White', ["J", 2]), Pawn('Black', ["K", 13]), Pawn('White', ["K", 2]),
                          Pawn('Black', ["D", 13]), Pawn('White', ["D", 2]), Pawn('Black', ["E", 13]),
                          Pawn('White', ["E", 2]), Pawn('Black', ["F", 13]), Pawn('White', ["F", 2]),
                          Pawn('Black', ["G", 13]), Pawn('White', ["G", 2]), Pawn('Black', ["H", 13]),
                          Pawn('White', ["H", 2]), Pawn('Red', ["M", 4]), Pawn('Blue', ["B", 4]), Pawn('Red', ["M", 5]),
                          Pawn('Blue', ["B", 5]), Pawn('Red', ["M", 6]), Pawn('Blue', ["B", 6]),
                          Pawn('Red', ["M", 7]), Pawn('Blue', ["B", 7]), Pawn('Red', ["M", 8]),
                          Pawn('Blue', ["B", 8]), Pawn('Red', ["M", 9]), Pawn('Blue', ["B", 9]),
                          Pawn('Red', ["M", 10]), Pawn('Blue', ["B", 10]), Pawn('Red', ["M", 11]),
                          Pawn('Blue', ["B", 11]), Queen('Black', ['G', 14]), Queen('White', ['G', 1]),
                          Queen('Red', ['N', 7]), Queen('Blue', ['A', 7]), King('Black', ['H', 14]),
                          King('White', ['H', 1]), King('Red', ['N', 8]), King('Blue', ['A', 7]),
                          Rook('Black', ["D", 14]), Rook('Black', ["K", 14]), Rook('White', ["D", 1]),
                          Rook('White', ["K", 1]), Rook('Blue', ["A", 11]), Rook('Blue', ["A", 4]),
                          Rook('Red', ["N", 11]), Rook('Red', ["N", 4]), Bishop('Black', ["F", 14]),
                          Bishop('Black', ["I", 14]), Bishop('White', ["E", 1]), Bishop('White', ["J", 1]),
                          Bishop('Red', ["N", 9]), Bishop('Red', ["N", 6]), Bishop('Blue', ["A", 9]),
                          Bishop('Blue', ["A", 6]), Knight('Black', ["E", 14]), Knight('Black', ["J", 14]),
                          Knight('White', ["E", 1]), Knight('White', ["J", 1]), Knight('Red', ["N", 5]),
                          Knight('Red', ["N", 10]), Knight('Blue', ["A", 5]), Knight('Blue', ["A", 10])]

        elif self.board_type == 'Double chessboard':
            self.board = [Pawn('Black', ["A", 11]), Pawn('White', ["A", 2]), Pawn('Black', ["B", 11]),
                          Pawn('White', ["B", 2]), Pawn('Black', ["C", 11]), Pawn('White', ["C", 2]),
                          Pawn('Black', ["D", 11]), Pawn('White', ["D", 2]), Pawn('Black', ["E", 11]),
                          Pawn('White', ["E", 2]), Pawn('Black', ["F", 11]), Pawn('White', ["F", 2]),
                          Pawn('Black', ["G", 11]), Pawn('White', ["G", 2]), Pawn('Black', ["H", 11]),
                          Pawn('White', ["H", 2]), Pawn('Black', ["I", 11]), Pawn('White', ["I", 2]),
                          Pawn('Black', ["J", 11]),
                          Pawn('White', ["J", 2]), Pawn('Black', ["K", 11]), Pawn('White', ["K", 2]),
                          Pawn('Black', ["L", 11]), Pawn('White', ["L", 2]), Pawn('Black', ["M", 11]),
                          Pawn('White', ["M", 2]), Pawn('Black', ["N", 11]), Pawn('White', ["N", 2]),
                          Pawn('Black', ["O", 11]), Pawn('White', ["O", 2]), Pawn('Black', ["P", 11]),
                          Pawn('White', ["P", 2]), Queen('Black', ['D', 12]), Queen('White', ['D', 1]),
                          Queen('Black', ['L', 12]), Queen('White', ['L', 1]), King('Black', ['E', 12]),
                          King('White', ['E', 1]), King('Black', ['M', 12]), King('White', ['M', 1]),
                          Rook('Black', ["A", 12]), Rook('Black', ["H", 12]), Rook('White', ["A", 1]),
                          Rook('White', ["H", 1]), Rook('Black', ["I", 12]), Rook('Black', ["P", 12]),
                          Rook('White', ["I", 1]), Rook('White', ["P", 1]), Bishop('Black', ["C", 12]),
                          Bishop('Black', ["F", 12]), Bishop('White', ["C", 1]), Bishop('White', ["F", 1]),
                          Bishop('Black', ["N", 12]), Bishop('White', ["N", 1]), Bishop('Black', ["K", 12]),
                          Bishop('White', ["K", 1]), Knight('Black', ["B", 12]), Knight('Black', ["G", 12]),
                          Knight('White', ["B", 1]), Knight('White', ["G", 1]), Knight('Black', ["J", 12]),
                          Knight('Black', ["O", 12]), Knight('White', ["J", 1]), Knight('White', ["O", 1])]

        for objective in self.board:
            self.positions.append(Position(objective.position[0], objective.position[1]))

    def printing_board(self):
        """
        (Board) -> str
        Prints the board
        """

        for figure in self.board:
            print(figure.color, figure.shape, (figure.position[0], figure.position[1]))


class ChessSet:
    """Class for chess set representation"""
    def __init__(self, board):
        self.board = board

class Position:
    """Class for figur position representation"""
    def __init__(self, letter, number):
        self.letter = letter
        self.number = number


class Piece:
    """Class for chess piece representation"""
    def __init__(self, color, position):
        self.position = position
        self.color = color


class Knight(Piece):
    """Class for knight representation"""
    def __init__(self,color, position):
        self.shape = 'Knight'
        super().__init__(color, position)

    def move(self):
        """
        Move figure
        """
        pass

class Rook(Piece):
    """Class for rook representation"""
    def __init__(self, color, position):
        self.shape = 'Rook'
        super().__init__(color, position)

    def move(self):
        """
        Move figure
        """
        pass

class Bishop(Piece):
    """Class for piece representation"""
    def __init__(self, color, position):
        self.shape = 'Bishop'
        super().__init__(color, position)

    def move(self):
        """
        Move figure
        """
        pass

class Queen(Piece):
    """Class for queen representation"""
    def __init__(self, color, position):
        self.shape = 'Queen'
        super().__init__(color, position)

    def move(self):
        """
        Move figure
        """
        pass

class King(Piece):
    """Class for king representation"""
    def __init__(self, color, position):
        self.shape = 'King'
        super().__init__(color, position)

    def move(self):
        """
        Move figure
        """
        pass


class Pawn(Piece):
    def __init__(self, color, position):
        self.shape = 'Pawn'
        super().__init__(color, position)

    def move(self):
        """
        Move figure
        """
        pass

if __name__ == '__main__':
    if choice in boards:
        board = Board(choice)
        board.create_board()
        board.printing_board()
        chess_set = ChessSet(board)
    else:
        print('You wrote wrong board')