from random import choice
import os

#List of words to randomly choose from
hangman_list = ['about', 'above', 'abuse', 'accept', 'accident', 'accuse', 'across', 'activist', 'actor', 'administration', 'admit', 'adult', 
                 'advertise', 'advise', 'affect', 'afraid', 'after', 'again', 'against', 'agency', 'aggression', 'agree', 'agriculture', 'force', 
                 'airplane', 'airport', 'album', 'alcohol', 'alive', 'almost', 'alone', 'along', 'already', 'although', 'always', 'ambassador', 'amend', 
                 'ammunition', 'among', 'amount', 'anarchy', 'ancestor', 'ancient', 'anger', 'animal', 'anniversary', 'announce', 'another', 'answer', 
                 'apologize', 'appeal', 'appear', 'appoint', 'approve', 'archeology', 'argue', 'around', 'arrest', 'arrive', 'artillery', 'assist', 'astronaut', 
                 'astronomy', 'asylum', 'atmosphere', 'attach', 'attack', 'attempt', 'attend', 'attention', 'automobile', 'autumn', 'available', 'average', 
                 'avoid', 'awake', 'award', 'balance', 'balloon', 'ballot', 'barrier', 'battle', 'beauty', 'because', 'become', 'before', 'begin', 'behavior', 
                 'behind', 'believe', 'belong', 'below', 'betray', 'better', 'between', 'biology', 'black', 'blame', 'bleed', 'blind', 'block', 'blood', 'border', 
                 'borrow', 'bottle', 'bottom', 'boycott', 'brain', 'brave', 'bread', 'break', 'breathe', 'bridge', 'brief', 'bright', 'bring', 'broadcast', 'brother', 
                 'brown', 'budget', 'build', 'building', 'bullet', 'burst', 'business', 'cabinet', 'camera', 'campaign', 'cancel', 'cancer', 'candidate', 'capital', 
                 'capture', 'career', 'careful', 'carry', 'catch', 'cause', 'ceasefire', 'celebrate', 'center', 'century', 'ceremony', 'chairman', 'champion', 'chance', 
                 'change', 'charge', 'chase', 'cheat', 'cheer', 'chemicals', 'chemistry', 'chief', 'child', 'children', 'choose', 'circle', 'citizen', 'civilian', 
                 'civil', 'rights', 'claim', 'clash', 'class', 'clean', 'clear', 'clergy', 'climate', 'climb', 'clock', 'close', 'cloth', 'clothes', 'cloud',
				 'coalition', 'coast', 'coffee', 'collapse', 'collect', 'college', 'colony', 'color', 'combine', 'command', 'comment', 'committee', 'common', 
                 'communicate', 'community', 'company', 'compare', 'compete', 'complete', 'complex', 'compromise', 'computer', 'concern', 'condemn', 'condition', 
                 'conference', 'confirm', 'conflict', 'congratulate', 'Congress', 'connect', 'conservative', 'consider', 'constitution', 'contact', 'contain', 
                 'container', 'continent', 'continue', 'control', 'convention', 'cooperate', 'correct', 'corruption', 'cotton', 'count', 'country', 'court', 'cover', 
                 'crash', 'create', 'creature', 'credit', 'crime', 'criminal', 'crisis', 'criticize', 'crops', 'cross', 'crowd', 'crush', 'culture', 'curfew', 
                 'current', 'custom', 'customs', 'damage', 'dance', 'danger', 'daughter', 'debate', 'decide', 'declare', 'decrease', 'defeat', 'defend', 'deficit', 
                 'define', 'degree', 'delay', 'delegate', 'demand', 'democracy', 'demonstrate', 'denounce', 'depend', 'deplore', 'deploy', 'depression', 'describe', 
                 'desert', 'design', 'desire', 'destroy', 'detail', 'detain', 'develop', 'device', 'dictator', 'different', 'difficult', 'dinner', 'diplomat', 'direct', 
                 'direction', 'disappear', 'disarm', 'disaster', 'discover', 'discrimination', 'discuss', 'disease', 'dismiss', 'dispute', 'dissident', 'distance', 
                 'divide', 'doctor', 'document', 'dollar', 'donate', 'double', 'dream', 'drink', 'drive', 'drown', 'during', 'early', 'earth', 'earthquake', 'ecology', 
                 'economy', 'education', 'effect', 'effort', 'either', 'elect', 'electricity', 'embassy', 'embryo', 'emergency', 'emotion', 'employ', 'empty', 'enemy', 
                 'energy', 'enforce', 'engine', 'engineer', 'enjoy', 'enough', 'enter', 'environment', 'equal', 'equipment', 'escape', 'especially', 'establish', 
                 'estimate', 'ethnic', 'evaporate', 'event', 'every', 'evidence', 'exact', 'examine', 'example', 'excellent', 'except', 'exchange', 'excuse', 'execute', 
                 'exercise', 'exile', 'exist', 'expand', 'expect', 'expel', 'experience', 'experiment', 'expert', 'explain', 'explode', 'explore', 'export', 'express', 
                 'extend', 'extra', 'extraordinary', 'extreme', 'extremist', 'factory', 'false', 'family', 'famous', 'father', 'favorite', 'federal', 'female', 'fence', 
                 'fertile', 'field', 'fierce', 'fight', 'final', 'financial', 'finish', 'fireworks', 'first', 'float', 'flood', 'floor', 'flower', 'fluid', 'follow', 
                 'force', 'foreign', 'forest', 'forget', 'forgive', 'former', 'forward', 'freedom', 'freeze', 'fresh', 'friend', 'frighten', 'front', 'fruit', 'funeral', 
                 'future', 'gather', 'general', 'generation', 'genocide', 'gentle', 'glass', 'goods', 'govern', 'government', 'grain', 'grass', 'great', 'green', 'grind', 
                 'ground', 'group', 'guarantee', 'guard', 'guerrilla', 'guide', 'guilty', 'happen', 'happy', 'harvest', 'headquarters', 'health', 'heavy', 'helicopter', 
                 'hijack', 'history', 'holiday', 'honest', 'honor', 'horrible', 'horse', 'hospital', 'hostage', 'hostile', 'hotel', 'house', 'however', 'human', 'humor', 
                 'hunger', 'hurry', 'husband', 'identify', 'ignore', 'illegal', 'imagine', 'immediate', 'immigrant', 'import', 'important', 'improve', 'incident', 
                 'incite', 'include', 'increase', 'independent', 'individual', 'industry', 'infect', 'inflation', 'influence', 'inform', 'information', 'inject', 'injure', 
                 'innocent', 'insane', 'insect', 'inspect', 'instead', 'instrument', 'insult', 'intelligence', 'intelligent', 'intense', 'interest', 'interfere', 
                 'international', 'Internet', 'intervene', 'invade', 'invent', 'invest', 'investigate', 'invite', 'involve', 'island', 'issue', 'jewel', 'joint', 'judge', 
                 'justice', 'kidnap', 'knife', 'knowledge', 'labor', 'laboratory', 'language', 'large', 'laugh', 'launch', 'learn', 'leave', 'legal', 'legislature', 
                 'letter', 'level', 'liberal', 'light', 'lightning', 'limit', 'liquid', 'listen', 'literature', 'little', 'local', 'lonely', 'loyal', 'machine', 'magazine', 
                 'major', 'majority', 'manufacture', 'march', 'market', 'marry', 'material', 'mathematics', 'matter', 'mayor', 'measure', 'media', 'medicine', 'member', 
                 'memorial', 'memory', 'mental', 'message', 'metal', 'method', 'microscope', 'middle', 'militant', 'military', 'militia', 'mineral', 'minister', 'minor', 
                 'minority', 'minute', 'missile', 'missing', 'mistake', 'model', 'moderate', 'modern', 'money', 'month', 'moral', 'morning', 'mother', 'motion', 'mountain', 
                 'mourn', 'movement', 'movie', 'murder', 'music', 'mystery', 'narrow', 'nation', 'native', 'natural', 'nature', 'necessary', 'negotiate', 'neighbor', 
                 'neither', 'neutral', 'never', 'night', 'noise', 'nominate', 'normal', 'north', 'nothing', 'nowhere', 'nuclear', 'number', 'object', 'observe', 'occupy', 
                 'ocean', 'offensive', 'offer', 'office', 'officer', 'official', 'often', 'operate', 'opinion', 'oppose', 'opposite', 'oppress', 'orbit', 'order', 
                 'organize', 'other', 'overthrow', 'paint', 'paper', 'parachute', 'parade', 'pardon', 'parent', 'parliament', 'partner', 'party', 'passenger', 'passport', 
                 'patient', 'peace', 'people', 'percent', 'perfect', 'perform', 'period', 'permanent', 'permit', 'person', 'persuade', 'physical', 'physics', 'picture', 
                 'piece', 'pilot', 'place', 'planet', 'plant', 'plastic', 'please', 'plenty', 'point', 'poison', 'police', 'policy', 'politics', 'pollute', 'popular', 
                 'population', 'position', 'possess', 'possible', 'postpone', 'poverty', 'power', 'praise', 'predict', 'pregnant', 'present', 'president', 'press', 
                 'pressure', 'prevent', 'price', 'prison', 'private', 'prize', 'probably', 'problem', 'process', 'produce', 'profession', 'professor', 'profit', 'program', 
                 'progress', 'project', 'promise', 'propaganda', 'property', 'propose', 'protect', 'protest', 'prove', 'provide', 'public', 'publication', 'publish', 
                 'punish', 'purchase', 'purpose', 'quality', 'question', 'quick', 'quiet', 'radar', 'radiation', 'radio', 'railroad', 'raise', 'reach', 'react', 'ready', 
                 'realistic', 'reason', 'reasonable', 'rebel', 'receive', 'recent', 'recession', 'recognize', 'record', 'recover', 'reduce', 'reform', 'refugee', 'refuse', 
                 'register', 'regret', 'reject', 'relations', 'release', 'religion', 'remain', 'remains', 'remember', 'remove', 'repair', 'repeat', 'report', 'represent', 
                 'repress', 'request', 'require', 'rescue', 'research', 'resign', 'resist', 'resolution', 'resource', 'respect', 'responsible', 'restaurant', 'restrain', 
                 'restrict', 'result', 'retire', 'return', 'revolt', 'right', 'river', 'rocket', 'rough', 'round', 'rubber', 'rural', 'sabotage', 'sacrifice', 'sailor', 
                 'satellite', 'satisfy', 'school', 'science', 'search', 'season', 'second', 'secret', 'security', 'seeking', 'seize', 'Senate', 'sense', 'sentence', 
                 'separate', 'series', 'serious', 'serve', 'service', 'settle', 'several', 'severe', 'shake', 'shape', 'share', 'sharp', 'sheep', 'shell', 'shelter', 
                 'shine', 'shock', 'shoot', 'short', 'should', 'shout', 'shrink', 'sickness', 'signal', 'silence', 'silver', 'similar', 'simple', 'since', 'single', 
                 'sister', 'situation', 'skeleton', 'skill', 'slave', 'sleep', 'slide', 'small', 'smash', 'smell', 'smoke', 'smooth', 'social', 'soldier', 'solid', 
                 'solve', 'sound', 'south', 'space', 'speak', 'special', 'speech', 'speed', 'spend', 'spill', 'spirit', 'split', 'sport', 'spread', 'spring', 'square', 
                 'stand', 'start', 'starve', 'state', 'station', 'statue', 'steal', 'steam', 'steel', 'stick', 'still', 'stone', 'store', 'storm', 'story', 'stove', 
                 'straight', 'strange', 'street', 'stretch', 'strike', 'strong', 'structure', 'struggle', 'study', 'stupid', 'subject', 'submarine', 'substance', 
                 'substitute', 'subversion', 'succeed', 'sudden', 'suffer', 'sugar', 'suggest', 'suicide', 'summer', 'supervise', 'supply', 'support', 'suppose', 
                 'suppress', 'surface', 'surplus', 'surprise', 'surrender', 'surround', 'survive', 'suspect', 'suspend', 'swallow', 'swear', 'sweet', 'sympathy', 
                 'system', 'target', 'taste', 'teach', 'technical', 'technology', 'telephone', 'telescope', 'television', 'temperature', 'temporary', 'tense', 
                 'terrible', 'territory', 'terror', 'terrorist', 'thank', 'theater', 'theory', 'there', 'these', 'thick', 'thing', 'think', 'third', 'threaten', 
                 'through', 'throw', 'tired', 'today', 'together', 'tomorrow', 'tonight', 'torture', 'total', 'touch', 'toward', 'trade', 'tradition', 'traffic', 
                 'tragic', 'train', 'transport', 'transportation', 'travel', 'treason', 'treasure', 'treat', 'treatment', 'treaty', 'trial', 'tribe', 'trick', 'troops', 
                 'trouble', 'truce', 'truck', 'trust', 'under', 'understand', 'unite', 'universe', 'university', 'unless', 'until', 'urgent', 'usual', 'vacation', 
                 'vaccine', 'valley', 'value', 'vegetable', 'vehicle', 'version', 'victim', 'victory', 'video', 'village', 'violate', 'violence', 'visit', 'voice', 
                 'volcano', 'volunteer', 'wages', 'waste', 'watch', 'water', 'wealth', 'weapon', 'weather', 'weigh', 'welcome', 'wheat', 'wheel', 'where', 'whether', 
                 'which', 'while', 'white', 'whole', 'willing', 'window', 'winter', 'withdraw', 'without', 'witness', 'woman', 'wonder', 'wonderful', 'world', 'worry', 
                 'worse', 'worth', 'wound', 'wreck', 'wreckage', 'write', 'wrong', 'yellow', 'yesterday', 'young']

#alphabet to check entry is correct
a_to_z = 'abcdefghijklmnopqrstuvwxyz'

#hangman drawings, index corresponds to lives remaining
drawings = [
    '''
  _____
  |   |
  |   O
  |  /|\\
  |  / \\
__|___''',
    '''
  _____
  |   |
  |   O
  |  /|\\
  |  / 
__|___''',
    '''
  _____
  |   |
  |   O
  |  /|\\
  |   
__|___''',
    '''
  _____
  |   |
  |   O
  |  /|
  |   
__|___''',
        '''
  _____
  |   |
  |   O
  |   |
  |   
__|___''',
        '''
  _____
  |   |
  |   O
  |   
  |   
__|___''',
        '''
  _____
  |   |
  |   
  |   
  |   
__|___''',
        '''
  _____
  |   
  |   
  |   
  |   
__|___''',
        '''
  
  |   
  |   
  |   
  |   
__|___''',
        '''
 
     
    
  |   
  |   
__|___''',
        '''




__|___''',
        '''

        
        
        

_______''',
        '''

        
        
        

_'''
    ]




#Prompts player input and cleans the input
def player_guess():
    player_letter_input = input("Guess a letter:  ")
    player_letter_clean = player_letter_input.strip().lower()
    return player_letter_clean

#clears terminal to make game clearer
def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

#Start of the game
def play_hangman(players_choosen_lives):
    #Initialising variables for each game. Keeping track of score, lives and the display
    #lives = 7
    message = ''
    display_of_guesses = ''
    list_of_guesses = []
    successful_guess = 0
    win = False

    #Chooses a random word from the list
    hangman_word = choice(hangman_list)

    #set lives to be choosen amount
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
        print(drawings[lives]) #hangman drawing
        print('\n\n' + display_of_guesses)
        guessed_letter = player_guess() #ask for player to guess a letter

        #checks that input is the correct format (a single letter) and sets appropriate message 
        if len(guessed_letter) > 1:
            message = 'Only guess one letter at a time.\n'
            continue
        elif guessed_letter not in a_to_z:
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
        print(drawings[lives])
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
                print('Leave blank for the default 7 lives OR')
                print('Enter a number between 1 and 10 OR')
                print('Enter W for lives equal to the number of letters OR')
                print('Enter U for lives equal to the number of unique letters')
                num_of_lives = input('Take your pick: \n ')
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