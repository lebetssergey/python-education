import sys
from random import choice


def read_to_list(file):
    """ This function allows read a *.txt as list """
    file = open(file, 'r', encoding='utf-8')
    lines = file.readlines()
    lines = [line.strip('\n') for line in lines]
    file.close()
    return lines


def write_to_file(current_word):
    """ This function allows write to file  """
    file = open("previous.txt", "a", encoding='utf-8',)
    file.write(current_word + '\n')
    file.close()


#  Create a start menu with choice of options
start = int(input('\nPlease make a choice \n1 - Welcome to Animal Planet \n2 - View previous words \n3 - Exit\n'))

if start == 1:
    #  Tuple, which include a stage of game, tuples,they are everywhere
    HANGMAN = (
        """
         ------
         |    |
         |
         |
         |
         |
         |
        ----------
        """,
        """
         ------
         |    |
         |    0
         |
         |
         |
         |
        ----------
        """,
        """
         ------
         |    |
         |    0
         |    |
         | 
         |   
         |    
        ----------
        """,
        """
         ------
         |    |
         |    0
         |   /|
         |   
         |   
         |   
        ----------
        """,
        """
         ------
         |    |
         |    0
         |   /|\\
         |   
         |   
         |     
        ----------
        """,
        """
         ------
         |    |
         |    0
         |   /|\\
         |   /
         |   
         |    
        ----------
        """,
        """
         ------
         |    |
         |    0
         |   /|\\
         |   / \\
         |   
         |   
        ----------
        """
    )
    # Create a number of maximum attempts
    mistakes = len(HANGMAN)
    # Read a new words from file
    word_list = read_to_list('dictionary.txt')
    word = choice(word_list)
    # write a current word into file
    write_to_file(word)
    # Create a frame of word
    frame = '_' * len(word)
    # Create a counter of wrong attempts
    wrong_counter = 0
    # list of used letters
    used_letters = []
    # List of used words
    used_words = []

    # Main loops of game
    while wrong_counter < mistakes and frame != word:
        print(HANGMAN[wrong_counter])
        print('\nUsed letters is :\n', used_letters)
        print('\nCurrent state of word:\n', frame)
        # input a new letter
        guess = input('\nInput a letter: ')
        # Case when letter is already used
        while guess in used_letters:
            print('This letter is already guessed', guess)
            guess = input('Input a letter: ')
        # Create a list with guessed letters
        used_letters.append(guess)

        if guess in word:
            print('\nWell done \'' + guess + '\' This letter is in the word1')
            # Draw a new frame when letter is guessed
            new = ''
            for i in range(len(word)):
                if guess == word[i]:
                    new += guess
                else:
                    new += frame[i]
            frame = new
        else:
            print('\nSorry \'' + guess + '\' This letter is not in the current word.')
            wrong_counter += 1

    if wrong_counter == mistakes:
        print('\nGame over')
    else:
        print('\nYou Win!')
        used_state = True

    print('\nOriginal word is : \'' + word + '\'')


elif start == 2:
    print(*read_to_list('previous.txt'))
elif start == 3:
    print('Exit')
    sys.exit(0)
