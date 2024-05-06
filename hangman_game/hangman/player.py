import random
from time import sleep

class HMPlayer:
    
    def __init__(self, name:str) -> None:
        #Constructor needs the player name
        self.name = name
        self.lives = 5
        self.score = 0

    def propose_letter(self):
        print("Warning! To be reimplemented in a derived class!") 

    def __str__(self) -> str:
        return f"{self.name} has {self.lives} lives left."
    
    def __lt__(self, other):
        return self.lives < other.lives
    

class HMHumanPlayer(HMPlayer):
    #A class to represent a HM human player
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def propose_letter(self) -> str:
        sleep(1)
        letter = ""
        while len(letter) != 1:
            letter = input("Propose a letter: ")
        return letter
    
class HMAIPlayer(HMPlayer):
    def __init__(self, name: str) -> None:
        super().__init__(name + "_bot")
        self.propose_letters = []
    
    def propose_letter(self) -> str:
        letter = random.choice("qwertyuiopasdfghjklzxcvbnm")
        while letter in self.propose_letters:
            letter = random.choice("qwertyuiopasdfghjklzxcvbnm")
        self.propose_letters.append(letter)
        return letter
    