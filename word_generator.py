from random import randint

wordlists = ["hangman_words.txt", "countries.txt", "animals.txt", "places.txt"]
hint = ""

class WordManager:
    def word_gen():
        wordlist_picked = wordlists[randint(0,3)]
        word_file = open(f"wordlists/{wordlist_picked}", "r")
        word_file_contents = word_file.readlines()
        file_line_length = len(word_file_contents)
        word_index = randint(1, file_line_length)

        if word_index == file_line_length:
            word_index = file_line_length - 1

        chosen_word = word_file_contents[word_index] 

        if wordlist_picked == 0:
            hint = "General Word"
        elif wordlist_picked == 1:
            hint = "Country"
        elif wordlist_picked == 2:
            hint = "Animal"
        else:
            hint = "Place"
            
        return chosen_word


    def get_hint():
        return hint
