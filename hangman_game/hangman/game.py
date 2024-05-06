# In game.py
from .player import HMPlayer, HMHumanPlayer, HMAIPlayer

import random
from time import sleep


class HMGame:
    def __init__(self, players:list) -> None:
        self.word = None #we used self.word here as we used it in the next functions
        self.players = players
        self.guessed_letters = []

    def display_word(self):
        display = ""
        for i in self.word:
            if i in self.guessed_letters:
                display += i
            else:
                display += "_"
        return display
    
    def play(self):
        winner = None
        for p in self.players:
            p.lives = 5
            p.score = 0
            self.guessed_letters = []
            self.word = random.choice(["mohamed", "letsgo", "vamos", "barcelona"])
            while p.lives > 0 and self.word != self.display_word():
                print("----------------")
                self.turn(p)
            
            if self.word == self.display_word():
                print(f"Congratulations {p.name}, you won!")
                p.score += 1
            else:
                print(f"Player {p.name} lost!")


        max_score = -1
        winner = None
        for player in self.players:
            if player.score > max_score:
                max_score = player.score
                winner = player

        if winner is not None:
            print(f"The player with the highest score is {winner.name} with a score of {winner.score}.")
        else:
            print("No player has won the game based on score.")

    
    def turn(self, p:HMPlayer) -> None:
        print(f"Player {p.name}. Word: {self.display_word()}")

        l = p.propose_letter()
        print(f"Player {p.name} propose letter: {l}")

        if l in self.word and l not in self.guessed_letters:
            print("Correct, nice guess")
            self.guessed_letters.append(l)
            p.score += 1
        else:
            print("Wrong guess")
            p.lives -= 1
            print(f"{p.lives} attempts left")