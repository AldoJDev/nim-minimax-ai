'''
https://www.w3schools.com/python/ref_func_sorted.asp
https://www.w3schools.com/python/python_lambda.asp
https://realpython.com/python-minimax-nim/
https://en.wikipedia.org/wiki/Alpha–beta_pruning
https://www.youtube.com/watch?v=l-hh51ncgDI
'''

import random
from typing import List, Tuple

class Nim:
    def __init__(self, initial = [1, 3, 5, 7]):
        self.piles = initial.copy()
        self.player = 0
        self.winner = None

    @classmethod
    def available_actions(cls, piles: List[int]) -> List[Tuple[int, int]]:
        response = []
        for pile in range(len(piles)):
            for num in range(1, piles[pile] + 1):
                response.append((pile, num))

        return response

    @classmethod
    def other_player(cls, player: int) -> int:
        return 0 if player == 1 else 1

    def switch_player(self):
        self.player = self.other_player(self.player)

    def move(self, action: Tuple[int, int]):
        self.piles[action[0]] -= action[1]
        if all(pile == 0 for pile in self.piles):
            self.winner = self.other_player(self.player)

class AlphaBetaPrunning:
    def choose_action(self, state: List[int], depth: int, alpha: float, beta: float, isMaximizer: bool) -> Tuple[int, int]:
        best_eval = -float('inf')
        best_move = None

        actions = Nim.available_actions(state)

        for move in actions:
            state[move[0]] -= move[1]
            eval = self.minimax(state, depth, alpha, beta, False)
            state[move[0]] += move[1]

            if eval > best_eval:
                best_eval = eval
                best_move = move

        return best_move

    def minimax(self, state: List[int], depth: int, alpha: float, beta: float, isMaximizer: bool) -> float:
        if all(pile == 0 for pile in state):
            return 1 if isMaximizer else -1

        if depth == 0:
            ones = sum(1 for pile in state if pile == 1)    
            more_than_one = any(pile > 1 for pile in state) 

            if not more_than_one:
                return 1 if ones % 2 == 0 else -1 
            
            nim_sum = 0
            for pile in state:
                nim_sum ^= pile

            return -1 if nim_sum != 0 else 1

        actions = Nim.available_actions(state)

        if isMaximizer:
            max_eval = -float('inf')
            for move in actions:
                state[move[0]] -= move[1]
                eval = self.minimax(state, depth - 1, alpha, beta, False)
                state[move[0]] += move[1]

                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)

                if beta <= alpha:
                    break

            return max_eval

        else:
            min_eval = float('inf')
            for move in actions:
                state[move[0]] -= move[1]
                eval = self.minimax(state, depth - 1, alpha, beta, True)
                state[move[0]] += move[1]

                min_eval = min(min_eval, eval)
                beta = min(beta, eval)

                if beta <= alpha:
                    break
                
            return min_eval

def play(ai: AlphaBetaPrunning, human: int = None):
    if human is None:
        human = 0 if random.uniform(0, 1) < 0.5 else 1

    game = Nim()

    alpha = -float('inf')
    beta = float('inf')
    depth = 5

    while True:
        for i, pile in enumerate(game.piles):
            print(f'Pile {i} : {pile}')

        available_actions = Nim.available_actions(game.piles)

        if game.player == human:
            print('Your turn')
            while True:
                pile, count = map(int, input('Choose a pile and count: ').split())
                if (pile, count) in available_actions:
                    break

                print('Invalid move, try again')
        else:
            print('AI turn')
            pile, count = ai.choose_action(game.piles, depth, alpha, beta, True)
            print(f'AI chose to take {count} from pile {pile}.')

        game.move((pile, count))
        game.switch_player()

        if game.winner is not None:
            print('GAME OVER')
            winner = 'Human' if game.winner == human else 'AI'
            print(f'Winner is {winner}')
            break

play(AlphaBetaPrunning())