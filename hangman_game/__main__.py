from hangman.game import HMGame
from hangman.player import HMHumanPlayer, HMAIPlayer

def main():
    p1 = HMHumanPlayer("Mohamed")
    p2 = HMAIPlayer("mooo")
    players = [p1, p2]
    game = HMGame(players)
    game.play()

if __name__ == '__main__':
    main()
