from random import randint

wordlists = ["hangman_words.txt", "countries.txt", "animals.txt"]
def word_gen():
    word_index = randint(0, 213)
    word_file = open(f"wordlists/{wordlists[randint(0,2)]}", "r")
    word_file_contents = word_file.readlines()
    chosen_word = word_file_contents[word_index]
    return chosen_word

print(word_gen())
