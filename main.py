from word_generator import word_gen
import sys

chosen_word = word_gen()

def guess_row(word):
    guess_length = ["_" for letter in range(len(chosen_word) - 1)]
    return guess_length

hang_man = [
    " |",
    " O",
    "-^-",
    " |",
    "/ \ ",
]
not_hang_man = [
    "",
    "",
    "",
    "",
    "",
    "",
]
def hang_man_func(hman_list):
    for index in hman_list:
        print(str(index))

def main():
    count = 0
    guess_row_list = guess_row(chosen_word)
    try:
        while "_" in guess_row_list:
            hang_man_func(not_hang_man)
            for _ in guess_row_list:
                print(f"{_}" ,end=" ")
            print("")
            guess_input = str(input("Try to Guess: "))
            while len(guess_input) > 1:
                print("Guess can only be 1 character")
                guess_input = str(input("Invalid input, try again:"))
            if guess_input in chosen_word:
                for pos,char in enumerate(chosen_word):
                    if char == guess_input:
                        guess_row_list[pos] = str(guess_input)
            else:
                count += 1
                not_hang_man[count] = hang_man[count - 1]
    except IndexError:
        print(f"you lost, the word was {chosen_word}")
        sys.exit()
main()
