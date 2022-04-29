from word_manager import WordManager
from rich import print
import rich
from rich.markdown import Markdown
from rich.console import Console
import sys
import os


hang_man = [
    " 0",
    "[magenta]\|/[/magenta]",
    " [magenta]|[/magenta]",
    "/ [magenta]\ [/magenta] ",
    ""
]

not_hang_man = [
    " |",
    "",
    "",
    "",
    "",
    ""
]

console = Console()
won = 0
lost = 0


class Hangman:
    def __init__(self, chosen_word="", hint="", rejected_letters=[], count=0):
        self.chosen_word = chosen_word
        self.hint = hint
        self.rejected_letters = rejected_letters
        self.count = count

    def guess_row(self, chosen_word):
        guess_length = ["_" for letter in range(len(chosen_word)-1)]
        return guess_length

    def show_row(self, row):
        for index in row:
            print(str(index), end=" ")
        print("")

    def get_chosen_word(self):
        return self.chosen_word

    def show_hang_man(self, hman_list: list):
        print("=|")
        for index in hman_list:
            print(str(index))
    
    def clear_hang_man(self, hman_list: list):
        for index in range(1, 5, 1):
            hman_list[index] = ""

    def display_menu(self):
        md = ""
        with open("menu.md") as menu:
            menu_list = menu.readlines()
            for line in menu_list:
                md += str(line)
        console.print(Markdown(md))
        return menu_list

    def select_mode(self):
        menu = self.display_menu()
        selecting = True
        while selecting == True:
            try:
                select_val = int(input("Select Mode: "))

                while select_val < 1 or select_val > 3:
                    os.system("cls" if os.name == "nt" else "clear")
                    print("Invalid Value: Integer out of range")
                    print(Markdown(str(menu[-1])))
                    select_val = int(input("Select Mode: "))
                
                if select_val == 3:
                    sys.exit()

                selecting = False
            except ValueError or TypeError:
                print("Invalid Value: Only input integers")
                print(Markdown(str(menu[-1])))
                continue

        return select_val

    def initiate_game(self):
        global won, lost
        hint_status = ""
        guess_row_list = self.guess_row(self.chosen_word)
        hint_count = 0
        try:
            while "_" in guess_row_list:
                if len(self.rejected_letters) == 3 and hint_count == 0:
                    hint_status = str(console.input("Want a [bold blue]hint[/bold blue]? (y/n): "))
                    while len(hint_status) > 1 or len(hint_status) == 0:
                        print("Error: Only one character can be input")
                        hint_status = str(console.input("Want a [bold blue]hint[/bold blue]? (y/n): "))
                    while 'y' not in hint_status and 'n' not in hint_status:
                        print("Error: Please only enter 'y'es or 'n'o")
                        hint_status = str(console.input("Want a [bold blue]hint[/bold blue]? (y/n): "))
                    hint_count += 1

                os.system("cls" if os.name == "nt" else "clear")
                print(f"Won: {won}")
                print(f"Lost: {lost}")
                self.show_hang_man(not_hang_man)
                self.show_row(guess_row_list)

                if 'y' in hint_status or 'Y' in hint_status:
                    print(f"Hint: It is a [bold green]{self.hint}[/bold green]")

                print(f"Rejected Letters: {self.rejected_letters}")
                print(f"Next Up: [{hang_man[self.count]}]")
                guess_input = input("Try to Guess: ")

                while len(guess_input) > 1 or len(guess_input) == 0:
                    print("Guess can only be 1 character")
                    guess_input = str(input("Try to Guess: "))
                
                while type(guess_input) != str:
                    print("Error: Only Input letters")
                    guess_input = str(input("Try to Guess"))

                if guess_input in self.chosen_word:
                    for pos, char in enumerate(self.chosen_word):
                        if char == guess_input:
                            guess_row_list[pos] = str(guess_input)
                elif guess_input in self.rejected_letters:
                    continue
                else:
                    self.count += 1
                    not_hang_man[self.count] = hang_man[self.count - 1]
                    self.rejected_letters.append(guess_input)
        except IndexError:
            underscores_num = 0
            for _ in guess_row_list:
                if '_' in _:
                    underscores_num += 1
            
            if underscores_num >= 1:
                print(f"You [red]Lost[/red], the word was [bold italic green]{self.chosen_word}[/bold italic green]")
                self.clear_hang_man(not_hang_man)
                print(underscores_num)
                lost += 1
            elif underscores_num == 0:
                print(f"And that's a [bold yello]WIN[/bold yellow]!, the word was [bold italic green]{self.chosen_word}[/bold italic green]")
                self.clear_hang_man(not_hang_man)
                print(underscores_num)
                won += 1