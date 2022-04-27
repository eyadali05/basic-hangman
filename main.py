from word_generator import word_gen
import sys
import os

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

rejected_letters = []

won = 0
lost = 0


def hang_man_func(hman_list):
    for index in hman_list:
        print(str(index))


def main():
    chosen_word = word_gen()
    count = 0
    guess_row_list = guess_row(chosen_word)
    global won
    global lost
    try:
        while "_" in guess_row_list:
            os.system("clear")
            print(f"Won: {won}")
            print(f"Lost: {lost}")
            hang_man_func(not_hang_man)
            for _ in guess_row_list:
                print(f"{_}", end=" ")
            print("")
            print(f"rejected letters: {rejected_letters}")
            guess_input = str(input("Try to Guess: "))
            while len(guess_input) > 1:
                print("Guess can only be 1 character")
                guess_input = str(input("Invalid input, try again:"))
            if guess_input in chosen_word:
                for pos, char in enumerate(chosen_word):
                    if char == guess_input:
                        guess_row_list[pos] = str(guess_input)
            else:
                count += 1
                not_hang_man[count] = hang_man[count - 1]
                rejected_letters.append(guess_input)
    except IndexError:
        print(f"you lost, the word was {chosen_word}")
        lost += 1
        replay()
    if "_" not in guess_row_list:
        print(f"And that's a win!, the word was {chosen_word}")
        won += 1
        replay()


def replay():
    play_again = input("Play again? (y/n): ")
    while play_again != "y" and play_again != "n":
        print("invalid choice, Play again? (y/n): ")
        play_again = input()
    if play_again == "y":
        for i in range(len(not_hang_man)):
            not_hang_man[i] = ""
        rejected_letters.clear()
        main()
    else:
        sys.exit()


main()
