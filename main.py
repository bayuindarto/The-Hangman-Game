import random
from replit import clear
from hangman_words import word_list, alphabet
from hangman_art import logo, stages

# part 1
# chosing random words

chosen_word = random.choice(word_list)
word_lenght = len(chosen_word)
lives = 6
# debugging
# print(f"chosen word: '{chosen_word}'")

print(f"{logo} {stages[6]}")
print("Welcome to the Hangman Games")
print("Guess letters to find the hidden word. Don't run out of tries!")

display = []
for _ in chosen_word:
    display += "_"
print(f"{' '.join(display)}")

# part 2
# guessing letter part

end_game = False
guess_list = []

while not end_game:
    guess = input("Guess a letter: ").lower()

    clear()
    # debugging
    # print(guess)

    # checking under alphabetic
    if guess not in alphabet:
        print("Only can input one Alphabetic.")

    else:
    
        # checking duplicate letter
        if guess in guess_list:
            print("You already guess this letter, Try others!")
        
    
        # checking correct letter
        for i in range(word_lenght):
            if chosen_word[i] == guess:
                display[i] = guess
        if guess in display:
            print(f"Nice guess!! Let's continue, you still have {lives} tiers left")
    
        # checking wrong letter
        if guess not in chosen_word:
            lives -= 1
            if lives > 0:
                print(f"Wrong!! Try again, you still have {lives} tries left!!")
            else:
                end_game = True
                print("Out of tries!! You Lose!!!")
    
    print(f"{' '.join(display)}")
    print(stages[lives])
    guess_list.append(guess)
    
    # end game
    if "_" not in display:
        end_game = True
        print("Congratulation, You Win!!")

print(f'The answer is : "{chosen_word}"!! Let\'s play again!')