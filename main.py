import random

# These strings are stored as variables and represent the amount of guesses the user has left
zero_guesses_person = """
_________ 
|/      |
|       0
|      \|/
|       |
|      / \\
|
"""

one_life_person = """
_________ 
|/      |
|       0
|      \|/
|       |
|      / 
|
"""
two_guesses_person = """
_________ 
|/      |
|       0
|      \|/
|       |
|       
|
"""
three_guesses_person = """
_________ 
|/      |
|       0
|      \|
|       |
|       
|
"""
four_guesses_person = """
_________ 
|/      |
|       0
|       |
|       |
|       
|
"""
five_guesses_person = """
_________ 
|/      |
|       0
|       
|       
|       
|
"""
six_guesses_person = """
_________ 
|/      |
|       
|       
|       
|       
|
"""
# This defines the variable guesses_left, the user starts out with 6 guesses left
guesses_left = 6
# Usage of a list that stores the user's previously entered guesses
letters_guessed = []
# Usage of lists to store the possible answers that are chosen in the function choose_answer()
easy_answers = ["thought", "perfume", "posture", "display", "recruit", "haircut", "achieve", "station"]
medium_answers = ["staircase", "chemistry", "favorable", "perforate", "conscious", "breakdown", "beautiful", "tradition"]
hard_answers = ["jazz", "rhythm", "twelfth", "jukebox", "conceptualize", "injured", "critique", "gregarious"]
# Definition of the global variable answer, which is changed to be one of the possible answers in the function choose_answer()
answer = ""
# Definition of the global variable blanks, which is also updated in the function choose_answer()
blanks = ""
# Definition of the global variable previous_guess, which is changed every time the user enters a valid guess in the function get_guess()
previous_guess = ""

# This function prints out a congratulatory message and is only called if the user wins the game
def show_win():
    print()
    print(f"Congrats, you win! The word was {answer} and you still had {guesses_left} guesses left! Would you like to try again on a different difficulty?")

# This function prints out a message after the user loses asking them to play again
def show_loss():
    print()
    print(f"You lose! The word was {answer}! Would you like to try again on a lower difficulty?")

# This function updates the blanks after the user enters a correct guess and takes in the guess as a parameter
def update_blanks(guess):
    if guess in answer:
        new_blanks = ""
        # Usage of a for loop to iterate through each index of the answer and checks if the guess equals the letter in that position
        for i in range(len(answer)):
            if guess == answer[i]:
                new_blanks += guess + " "
            else:
                new_blanks += blanks[i * 2] + " "
        return new_blanks
    else:
        return blanks

# This person prints out the corresponding person based on the number of guesses the user has left
def show_person():
    if guesses_left == 6:
        print(six_guesses_person)
    elif guesses_left == 5:
        print(five_guesses_person)
    elif guesses_left == 4:
        print(four_guesses_person)
    elif guesses_left == 3:
        print(three_guesses_person)
    elif guesses_left == 2:
        print(two_guesses_person)
    elif guesses_left == 1:
        print(one_life_person)
    elif guesses_left == 0:
        print(zero_guesses_person)
        
# This function prints out the user's previous guesses and the result of their most recent guess, then it asks the user for their guess
def get_guess():
    global letters_guessed, previous_guess
    # This prints out the list letters_guessed, using the join method
    print("Letters guessed:", (", ").join(letters_guessed))
    print(f"Previous guess: {previous_guess}")
    if previous_guess in answer and previous_guess != "":
        print("Result: Yes")
    elif previous_guess == "":
        print("Result: None")
    else:
        print("Result: No")
    # Usage of a while loop to continue to ask the user for a guess until they input a single letter that they haven't already guessed
    while True:
        # Usage of user text input to get the user's guess
        guess = input("Enter a lowercase letter you would like to guess: ")
        if not guess.islower() or len(guess) > 1:
            print("Guesses must be a single lowercase letter! Try again!")
        elif guess in letters_guessed:
            print("You have already guessed that letter! Try again!")
        else:
            # Adding the user's guess to the previously initialized list letters_guessed
            letters_guessed.append(guess)
            letters_guessed.sort()
            previous_guess = guess
            break
    return guess

# This function prints out the counter of guesses and calls on the functions show_person and get_guess in order to print the person and take the users guess while the user hasn't won or lost
def play_game():
    global guesses_left, blanks
    counter = 1
    # Usage of a while loop to continue the game until the user runs out of guesses or guesses every letter in the word
    while guesses_left > 0 and "_" in blanks:
        print()
        print("************* Guess", counter, "*************")
        print()
        print("Here is the current state of your person and word:")
        # Call of the function show_person() to show the person
        show_person()
        print(blanks)
        print()
        guess = get_guess()
        # This checks if the user's guess is in the answer, and prints out that it is
        if guess in answer:
            print("That letter is in the answer!")
        # If the user's guess isn't in the answer, the variable guesses_left is decremented by 1
        else:
            print("Sorry, that is not in the answer!")
            guesses_left -= 1
        # Call of the function update_blanks with the user's guess inputted as a parameter, the value that is returned will be the new value of the variable blanks
        blanks = update_blanks(guess)
        counter += 1
    show_person()
    print(blanks)
    # This checks to see if the user has won by checking if there are no longer underscores in the variable blanks, meaning the user has guessed every letter
    if "_" not in blanks:
        show_win()
    elif guesses_left == 0:
        show_loss()

# This function takes in the user's previously entered difficulty choice as a parameter, and selects the answer from the list that corresponds with their choice. It also defines the blanks variable, based on the length of the answer
def choose_answer(difficulty):
    global answer, blanks
    # In this case, the user has chosen easy difficulty, so the answer is randomly selected from the list easy_answers
    if difficulty == "easy":
        answer = random.choice(easy_answers)
    # If the user chooses medium difficulty, the answer is randomly chosen from the list medium_answers
    elif difficulty == "medium":
        answer = random.choice(medium_answers)
    # If the user chooses hard difficulty, the answer is randomly chosen from the list hard_answers
    elif difficulty == "hard":
        answer = random.choice(hard_answers)
    blanks = "_ " * len(answer)
    
def choose_difficulty():
    # Usage of a while loop to continue asking the user to input their difficulty choice until they enter a valid option
    while True:
        # Usage of user text input to choose the difficulty of the game
        difficulty = input("Would you like an easy, medium, or hard word? ").lower()
        if difficulty == "easy" or difficulty == "medium" or difficulty == "hard":
            # Call of the function choose_answer() with the parameter of the user's difficulty choice
            choose_answer(difficulty)
            break
        else:
            print("That wasn't an option! Try again!")
            
# This function prints out an introductory message to the user and calls on the choose_difficulty and play_game functions to start the game
def introduction():
    print("Welcome to hangman!")
    print("The game will select a random word that you will have to guess by guessing letters you think will be in the word.")
    print("If the letter you guess is in the word, it will replace one or more of the blanks. The locations of the letters will correspond to its position within the word.")
    print("If it isn't, another body part of the person will be drawn. If the person's full body is shown, you lose! You are able to make six incorrect guesses until you lose.")
    choose_difficulty()
    print("Ok! Let's begin!")
    print(f"The word will have {len(answer)} letters")
    play_game()

# Call of the function introduction to start the game
introduction()