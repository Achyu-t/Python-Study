import random

# import wordslist

# words = wordslist.words

from wordslist import words

hangman = { 0: ("   ",
                "   ",
                "   "),

            1: (" o  ",
                "   ",
                "   "),    


            2: (" o  ",
                " |  ",
                "   "), 

            3: (" o  ",
                "/|  ",
                "   "), 

            4: (" o  ",
                "/|\\",
                "   "),  

            5: (" o  ",
                "/|\\",
                "/  ") , 

            6: (" o  ",
                "/|\\",
                "/ \\")}



def display_hangman(wrong_guesses):
    print('*********')
    for i in hangman[wrong_guesses]:
        print(i)
    print('*********')


def display_hint(hint):
    print(" ".join(hint))


def display_answer(word,hint):

    if "_" not in hint:
        print('YOU WINN !!!!🎊🎊')
        print(f'The word is : {word}')

    else:
        print('YOU LOOSE 🤮')
        print(f'The correct word was {word}')
        print('BETTER LUCK NEXT TIME')



def main():

    wrong_guesses = 0

    random_word = random.choice(words)

    hint = ["_"]*len(random_word)
    is_running = True

    while is_running:

        display_hangman(wrong_guesses)
        display_hint(hint)
        print('-------------------------------------------')
        user_guess = input("Enter your guess: ").lower()

        if user_guess.isalpha() and len(user_guess) == 1 :

            if user_guess in hint:
                print("You have already guessed the word. Try different word.")
                continue

            if user_guess in random_word:
                
                for i in range(len(hint)):
                    if random_word[i] == user_guess:
                        hint[i] = user_guess
                display_hint(hint)

            else:
                wrong_guesses += 1

            if wrong_guesses == (len(hangman)-1) or "_" not in hint:
                display_hangman(wrong_guesses)
                display_answer(random_word,hint)
                is_running = False

        else:
            print("The input should be a single alphabetic character.")
            continue


if __name__ == "__main__":
    main()


    