from random import randint

wordlists = ["hangman_words.txt", "countries.txt", "animals.txt", "places.txt", "foods.txt"]


class WordManager:

    hint = ""

    def __init__(self, gameMode: int):
        self.gameMode = gameMode

    def easy_mode():
        return randint(1, 4)

    def hard_mode():
        return 0

    def word_gen(self):
        wordlist_picked = wordlists[self.gameMode]
        word_file = open(f"wordlists/{wordlist_picked}", "r")
        word_file_contents = word_file.readlines()
        file_line_length = len(word_file_contents)
        word_index = randint(1, file_line_length)

        if word_index == file_line_length:
            word_index = file_line_length - 1

        chosen_word = word_file_contents[word_index]

        # Here we set the hint
        return chosen_word

    # Here is the get hint function
    def get_hint(self):
        if self.gameMode == 0:
            WordManager.hint = None
        elif self.gameMode == 1:
            WordManager.hint = "Country"
        elif self.gameMode == 2:
            WordManager.hint = "Living Organism"
        elif self.gameMode == 3:
            WordManager.hint = "Place"
        else:
            WordManager.hint = "Food / Ingredient"
        return WordManager.hint