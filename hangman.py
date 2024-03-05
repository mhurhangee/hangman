from random import choice
import os
import hangman_dictionary

#Prompts player input and cleans the input
def player_guess():
    player_letter_input = input("\nGuess a letter:  ")
    player_letter_clean = player_letter_input.strip().lower()
    return player_letter_clean

#clears terminal to make game clearer
def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

#Start of the game
def play_hangman(players_choosen_lives):
    #Initialising variables for each game, e.g. keeping track of score, previous guesses, lives and the display
    message = ''
    display_of_guesses = ''
    list_of_guesses = []
    successful_guess = 0
    win = False

    #Chooses a random word from the list
    hangman_word = choice(hangman_dictionary.words)

    #set lives to be player choosen amount
    if players_choosen_lives == 'w':
        lives = len(hangman_word)
    elif players_choosen_lives == 'u':
        lives = len(set(hangman_word))
    elif players_choosen_lives in range(1,11):
        lives = players_choosen_lives
    else:
        lives = 7


    #Builds the display of the word e.g. "_ _ _ _"
    for i in range(len(hangman_word)):
        display_of_guesses += ' _'
    display_of_guesses += ' :   Guessed letters:' 

    #Game loop whilst not dead otherwise display death message
    while lives > 0:
        clear()

        #checks if game has been won. If so, breaks loop to start again.
        if successful_guess ==  len(hangman_word):
            win = True
            print('WINNER!!!\n')
            print(f'You saved the man by guessing {hangman_word.upper()}!!!\n')
            print('''
                \\O/
                 |
                / \\
                ''')
            break
        
        #The display for each round of the game
        print(message) #message is related to the previous input. e.g. if the input was a correct guess or not
        print(f'Lives remaining: {lives}')    
        print(hangman_dictionary.drawings[lives]) #hangman drawing
        print('\n\n' + display_of_guesses)
        guessed_letter = player_guess() #ask for player to guess a letter

        #checks that input is the correct format (a single letter) and sets appropriate message 
        if len(guessed_letter) > 1:
            message = 'Only guess one letter at a time.\n'
            continue
        elif guessed_letter not in hangman_dictionary.a_to_z:
            message = 'Only guess letters (a to z)\n'
            continue
        #check if letter has been already guessed
        elif guessed_letter in list_of_guesses:
            message = f'Already guessed the letter {guessed_letter}. Guess again.\n'
            continue
        #then checks if input letter is in the word
        #if so, append to list of guesses, update the display, and no. of successful guesses
        elif guessed_letter in hangman_word:
            list_of_guesses.append(guessed_letter)
            message = 'Congrats! You got a letter.\n'

            #update the _ _ _ hangman display with the correct letter in the correct place
            #achieved by forming a temporary display and updating the string
            positions = [pos+1 for pos, char in enumerate(hangman_word) if char == guessed_letter]
            for position in positions:
                temp_display_of_guesses = display_of_guesses[:position*2-1] + guessed_letter + display_of_guesses[position*2:]
                display_of_guesses = temp_display_of_guesses
                #Update if success was successful for each time the letter appears, e.g. L in hello would score 2
                successful_guess += 1
            display_of_guesses += ' ' + guessed_letter
            continue
        #if not, prompt to guess again and lose a life
        else:
            list_of_guesses.append(guessed_letter)
            lives -=1
            message = 'Unlucky guess again\n'
            display_of_guesses += ' ' + guessed_letter
            continue
    
    #Only executes if lives == 0, i.e. the game is lost.  Show losing message and keep track of overall score
    if lives == 0:
        clear()
        print(hangman_dictionary.drawings[lives])
        print(f'\nYou killed the man by failing to guess {hangman_word.upper()}!!!\n')
        win = False
        
    return win

#Loop that manages whether to initialise the game or not based on the players input
def main():
    #scores[0] is overall wins and scores[1] is overall loses
    scores = [0,0]

    #Welcome message
    print('\nWelcome to Hangman!')

    #Play again loop
    while True:
        #show overall scores if not the first game
        if sum(scores) > 0:
            print(f'The current score is {scores[0]} wins and {scores[1]} losses.')

        #ask play if they would like to play again and    
        input_play_again = input('\nWould you like to play Hangman? Y or N  ')
        input_play_again_clean = input_play_again.strip().lower()

        #Player would like to play again
        if input_play_again_clean == 'y' or input_play_again_clean == 'yes':
            while True:
                #ask how many lives they would like and
                clear()
                print('Enter the number of lives you would like')
                print('->Leave blank for the default 7 lives OR')
                print('->Enter a number between 1 and 10 OR')
                print('->Enter W for lives equal to the number of letters OR')
                print('->Enter U for lives equal to the number of unique letters')
                num_of_lives = input('--->Take your pick: \n ')
                if num_of_lives == '':
                    lives = 7
                    break
                elif num_of_lives.lower() == 'w':
                    lives = 'w'
                    break
                elif num_of_lives.lower() == 'u':
                    lives = 'u'
                    break
                elif int(num_of_lives) in range(1,11):
                    lives = int(num_of_lives)
                    break
                else:
                    continue

            last_game = play_hangman(lives)

            #keep track of overall score
            if last_game == True: 
                scores[0] += 1 #win
            else: 
                scores[1] += 1 #loss
            continue
        
        #Player does not want to play again
        elif input_play_again_clean == 'n' or input_play_again_clean == 'no':
            print('\nThank you for playing\n Goodbye!')
            break

        #incorrect input, ask again
        else:
            print('\nPlease enter Y(es) or N(o)')
            continue

if __name__ == '__main__':
    main()