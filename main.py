import os
import sys
from game import Hangman
from word_manager import WordManager

def get_mode():
    
    os.system("cls" if os.name == "nt" else "clear")
    game = Hangman()
    mode = game.select_mode()
    return mode

def play_game(modeNum):

    game = Hangman()
    game.rejected_letters = []
    game.count = 0
    manager = WordManager(modeNum)
    game.chosen_word = manager.word_gen()
    game.hint = manager.get_hint()
    game.initiate_game()

def replay():
    replay_status = str(input("Play Again? (y/n): "))
    while replay_status not in ("y", "n"):
        print("Invalid Value: You can only enter 'y' or 'n'")
        replay_status = str(input("Play Again? (y/n): "))
    if replay_status == "y":
        mode = get_mode()
        play_game(mode)

    else:
        sys.exit()

def start_up():
    mode = get_mode()
    if mode == 1:
        mode_num = WordManager.hard_mode()
        play_game(mode_num)
        replay()
    else:
        mode_num = WordManager.easy_mode()
        play_game(mode_num)
        replay()
if __name__ == "__main__":
    start_up()