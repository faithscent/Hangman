import random

class Hangman:

    '''
    A Hangman Game that asks the user for a letter and checks if it is in the word.
    It starts with a default number of lives and a random word from the word_list.

    
    Parameters:
    ----------
    word_list: list
        List of words to be used in the game
    num_lives: int
        Number of lives the player has
    
    Attributes:
    ----------
    word: str
        The word to be guessed picked randomly from the word_list
    word_guessed: list
        A list of the letters of the word, with '_' for each letter not yet guessed apple
        For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']
        If the player guesses 'p', the list would be ['_', 'p', 'p', '_', '_']
    num_letters: int
        The number of UNIQUE letters in the word that have not been guessed yet
    num_lives: int
        The number of lives the player has
    list_letters: list
        A list of the letters that have already been tried

    Methods:
    -------
    check_letter(letter)
        Checks if the letter is in the word.
    ask_letter()
        Asks the user for a letter.
    '''
    word = ''
    word_guessed =[]
    num_letter = len(set(word))
    num_lives =0
    list_letters =[]

    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)
        print(f'The mystery word has {len(self.word)} characters')

        for i in range(len(self.word)):
            self.word_guessed.append('_') 
        
        print(f'{self.word_guessed}')
        

    def check_letter(self, letter) -> None:

        '''
        Checks if the letter is in the word.
        If it is, it replaces the '_' in the word_guessed list with the letter.
        If it is not, it reduces the number of lives by 1.

        Parameters:
        ----------
        letter: str
            The letter to be checked

        '''
        
        if letter in self.word:

            self.list_letters.append(letter)

            for i in range(0,len(self.word)):
                if letter == self.word[i]:
                    self.word_guessed[i] = self.word[i]

            print(self.word_guessed)

            if self.word_guessed != list(self.word):
                self.ask_letter()
            else:
                print(f'congratulations you won!')
                print(f'word is {self.word}')


        elif letter not in self.word:
            self.num_lives -= 1
            self.num_letter -= 1
            self.list_letters.append(letter)

            print('List of tried letters: ', self.list_letters)
            print('number of lives: ', self.num_lives)
            print(f'{letter} is not in the word')

            if self.num_lives != 0:
                self.ask_letter()
            else:
                print(f'You ran out of lives. The word was {self.word}')


    def ask_letter(self):

        '''
        Asks the user for a letter and checks two things:
        1. If the letter has already been tried
        2. If the character is a single character
        If it passes both checks, it calls the check_letter method.
        '''

        letter = input("Please, enter just one character: \n")
    
        check = True
        
        while check:

            if len(letter) == 1 and letter.isalpha() == True: 
                if letter not in self.list_letters:
                    self.check_letter(letter)

                    check = False

                else:
                    print(f"{letter} was already tried")
                    letter = input("Please, enter just one character: \n")

            else:
                letter = input("Please, enter just one character: \n")


def play_game(word_list):
    game = Hangman(word_list, num_lives=5)
    game.ask_letter()

 
if __name__ == '__main__':
    word_list = ['apple', 'banana', 'orange', 'pear', 'strawberry', 'watermelon']
    play_game(word_list)
