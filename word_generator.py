from random import randint

def word_gen():
    word_index = randint(0, 213)
    word_file = open("hangman_words.txt", "r")
    word_file_contents = word_file.readlines() 
    chosen_word = word_file_contents[word_index]
    return chosen_word
