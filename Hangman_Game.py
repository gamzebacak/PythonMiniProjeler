import time


def clear_screen():
    print("\n" * 25)  # 25 satır boşluk bırakarak kelimenin gizlenmesini sağla


def main():
    global word, display, already_guessed, count
    word = input("Enter the word to guess: ").lower().strip()
    clear_screen()
    display = " ".join(["-"] * len(word))
    already_guessed = []
    count = 0
    hangman()


def play_loop():
    play_game = input("Do You want to play again? y = yes, n = no \n").lower()
    while play_game not in ["y", "n"]:
        play_game = input(
            "Do You want to play again? y = yes, n = no \n").lower()
    if play_game == "y":
        main()
    else:
        print("Thanks For Playing! We expect you back again!")
        exit()


def hangman():
    global count, display, word, already_guessed
    limit = 5
    print("This is the Hangman Word:", display)
    guess = input("Enter your guess: ").lower().strip()

    if len(guess) != 1 or not guess.isalpha():
        print("Invalid Input, Try a letter\n")
        hangman()
    elif guess in already_guessed:
        print("You already guessed that letter. Try another one.\n")
    elif guess in word:
        already_guessed.append(guess)
        display_list = display.split()
        for index, letter in enumerate(word):
            if letter == guess:
                display_list[index] = guess
        display = " ".join(display_list)
        print(display + "\n")
    else:
        count += 1
        print(f"Wrong guess. {limit - count} guesses remaining\n")
        if count == 1:
            print("   _____ \n"
                  "  |     | \n"
                  "  |     \n"
                  "  |     \n"
                  "  |     \n"
                  "  |     \n"
                  "__|__\n")
        elif count == 2:
            print("   _____ \n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |     \n"
                  "  |     \n"
                  "  |     \n"
                  "__|__\n")
        elif count == 3:
            print("   _____ \n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |     | \n"
                  "  |     \n"
                  "  |     \n"
                  "__|__\n")
        elif count == 4:
            print("   _____ \n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |     \n"
                  "  |     \n"
                  "__|__\n")
        elif count == 5:
            print("   _____ \n"
                  "  |     | \n"
                  "  |     O \n"
                  "  |    /|\ \n"
                  "  |    / \ \n"
                  "  |     \n"
                  "__|__\n")
            print("Wrong guess. You are hanged!!!\n")
            print("The word was:", word)
            play_loop()

    if "-" not in display:
        print("Congrats! You have guessed the word correctly!")
        play_loop()
    elif count != limit:
        hangman()


main()
