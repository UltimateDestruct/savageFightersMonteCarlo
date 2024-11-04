import random


class Fighter:
    def __init__(self, name, hp, moves, current_move):
        self.name = name
        self.hp = hp
        self.moves = moves
        self.current_move = current_move
        self.next_moves = self.__find_next_moves()

    def __find_next_moves(self):
        move_id = str(self.current_move)
        moves = self.moves
        options = []
        if move_id in moves:
            move = moves[move_id]
            options = move.get('moveOptions', [])
        return options

    def randomly_select_next_move(self):
        return random.choice(self.next_moves)

    def update_next_moves(self):
        self.next_moves = self.__find_next_moves()
